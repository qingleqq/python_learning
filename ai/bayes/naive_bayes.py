import numpy as ny;

def get_data():
    feather_label_list = []
    return feather_label_list

def Pretreatment(data_list):
    rtn_list= data_list;
    return rtn_list

def spilt_list(dataSet_list, col, compare):
    #dataSet_list = ny.array(dataSet_list)
    feature_list = [x[col] for x in dataSet_list]
    rtn_list = []
    for val in dataSet_list:
        if val[col] == compare:
            tmp_list = val[0:col]
            #tmp_list.extend(val[col + 1:])
            rtn_list.append(tmp_list)
    return rtn_list

def spilt_feature(dataSet_list, col, key_feature):
    rtn_dict = {}
    feature_list = [x[col] for x in dataSet_list]
    feature_list = set(feature_list)
    tmp_dict = {}
    for feature in feature_list:
        tmp_list = spilt_list(dataSet_list,col,feature)
        tmp_dict[feature] = tmp_list
    return tmp_dict
    rtn_dict[key_feature] = tmp_dict
    print rtn_dict

def count_feature(dataSet_list, col, key_feature):
    rtn_dict = {}
    feature_list = [x[col] for x in dataSet_list]
    tmp_dict = {};
    for feature in feature_list:
        tmp_dict[feature] = tmp_dict.get(feature,0) + 1
    """
    for key in tmp_dict.keys():
        if sum(feature_list) == 0:
            print 'here'
        else:
            tmp_dict[key] = tmp_dict[key] / sum(feature_list)
    """
    return tmp_dict
    rtn_dict[key_feature] = tmp_dict
    return rtn_dict

def create_dict_for_feature(dataSet_list, featureName_list):
    rtn_dict = spilt_feature(dataSet_list, -1, 'label')
    tmp_dict = {}
    for k,v in rtn_dict.items():
        for i in range(4):
            tmp_dict['col' + str(i)] = count_feature(v,i,"col")
        rtn_dict[k]= tmp_dict.copy()
    print rtn_dict

dateset = [
    # {'c': {0: 'yes', 1: 'no', 2: 'no', 3: 'no'}}
    [1, 1, 0, 1, 'yes'],
    [1, 1, 0, 3, 'yes'],
    [3, 0, 0, 1, 'yes'],
    [2, 1, 1, 0, 'no'],
    [0, 3, 2, 1, 'no'],
    [1, 0, 3, 2, 'no'],
]

def demo():
    color = spilt_feature(dataSet_list=dateset,col=0, key_feature='color')
    create_dict_for_feature(dateset,['a'])
    style = count_feature(dataSet_list=dateset,col=4, key_feature='style')


    print style

demo();
