import numpy as ny
import matplotlib.pyplot as plt
from math import log


# 计算最后一列（label）的熵。输入格式为：[[feature0,feature1,featuren,..,lable],[feature0,feature1,featuren,..,lable]]
def cal_entropy_list(dataSet_array, col=-1):
    dataSet_array = ny.array(dataSet_array)
    dict_label = {}
    for key in dataSet_array[:, col]:
        dict_label[key] = dict_label.get(key, 0) + 1
    sumlabel = sum(dict_label.values())
    p_sum = 0
    for val in dict_label.values():
        p_x = val / sumlabel
        p_sum -= (p_x * log(p_x, 2))
    return p_sum

# 如果dataset中的第col列中的值等于compare的值,则将相等的这一行整行抽出，并隐去compare 。
# 返回所有相等所在行组成的新的列表1
# 输入格式为：[[feature0,feature1,featuren,..,lable],[feature0, feature1,
# featuren,.., lable]]


def spilt_list(dataSet_list, col, compare):
    #dataSet_list = ny.array(dataSet_list)
    feature_list = [x[col] for x in dataSet_list]
    rtn_list = []
    for val in dataSet_list:
        if val[col] == compare:
            tmp_list = val[0:col]
            tmp_list.extend(val[col + 1:])
            rtn_list.append(tmp_list)
    return rtn_list


def get_best_spilt(dateSet_array, label):
    collen = len(dateSet_array[0])
    best_col = 0
    min_entropy = 0xfffff
    rtn_dict = {}
    for i in range(collen - 1):
        feature_list = [x[i] for x in dateSet_array]
        feature_onlyone_list = set(feature_list)
        pi = 0
        tmp_dict = {}
        for feature in feature_onlyone_list:
            subDataset_list = spilt_list(dateSet_array, i, feature)
            #tmp_dict[label[i]+'_'+str(feature)] = subDataset_list
            tmp_dict[feature] = subDataset_list
            pi += cal_entropy_list(subDataset_list)
        print('col%d=%f' % (i, pi))
        if pi < min_entropy:
            rtn_dict = tmp_dict.copy()
            min_entropy = pi
            best_col = i

    # return best_col, min_entropy,rtn_dict
    bestlabel = label[best_col]
    del(label[best_col])
    fin_dict = {bestlabel: rtn_dict}
    return bestlabel, min_entropy, fin_dict

def create_tree_node(dataSet_array, label):
    bestcol, entropy, subDataset = get_best_spilt(dataSet_array, label)
    subDataset_dict = subDataset[bestcol]
    for k, v in subDataset_dict.items():
        if cal_entropy_list(v) == 0:
            tmp = v[0]
            tmp1 = v[-1]
            subDataset_dict[k] = v[0][-1]
        else:
            subDataset_dict[k] = create_tree_node(v, label)
    return subDataset


desciion_node = dict(boxstyle='sawtooth', fc=0.8)
leaf_node = dict(boxstyle='rand4', fc=0.8)
arrow = dict(arrowstyle='<-')


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    pass


def plot_node(feature, keyname, nodestyle):
    pass


def plot_leaf():
    pass


def plot_tree(tree_dict):
    pass


"""
dateset = [
    [1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no'],
]

"""

dateset = [
    # {'c': {0: 'yes', 1: 'no', 2: 'no', 3: 'no'}}
    [1, 1, 0, 1, 'yes'],
    [1, 1, 0, 3, 'yes'],
    [2, 1, 1, 0, 'no'],
    [0, 3, 2, 1, 'no'],
    [1, 0, 3, 2, 'no'],
    [3, 0, 0, 1, 'yes'],
]


def demo():
    ret = []

    print(cal_entropy_list(dateset))

    rtn_list = spilt_list(dateset, 0, 1)
    rtn = cal_entropy_list(rtn_list)
    print(rtn_list)
    print('====================')
    bestcol, rtn, best_dict = get_best_spilt(
        dateset, ['a', 'b', 'c', 'd', 'label'])
    print(bestcol, rtn)
    print(best_dict)
    rtn_dict = create_tree_node(dateset, ['a', 'b', 'c', 'd', 'label'])

    print(rtn_dict)


demo()
