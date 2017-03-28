import pandas
import numpy as ny
import matplotlib.dates as dates
import matplotlib.finance as f
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import logging

k_mean_dataSet = [[1, 2], [1, 3], [2, 5], [10, 23], [13, 22], [11, 24]]
k_mean_lable = ['a', 'a', 'a', 'b', 'b', 'b']
k_mean_dataX = [1, 5]


# 返回字典，lable值越小越接近

def k_mean_class0(intx, dataset, labels, k):
    dataset_size = len(dataset) / len(dataset[0])
    intx_array = ny.tile(intx, int(dataset_size))
    intx_len = []
    for a in dataset:
        tmp = ny.array(a) - ny.array(intx)
        tmp **= 2
        tmp = ny.sum(tmp)
        tmp **= 0.5
        intx_len.append(tmp)
    labelsx_list = ny.argsort(intx_len)
    label_k_list = []  # = ny.array([labels,labelsx_list])
    i = 0
    while i < dataset_size:
        label_k_list.append([labels[i], labelsx_list[i]])
        i += 1

    '''
    dictl = {}
    i = 0
    while i < len(intx_len):
        # 以大小的index相加，最后结果越小就越接近，不直接使用距离相加，可以防止部分噪声问题。
        dictl[labels[i]] = dictl.get(labels[i], 0) + labelsx_list[i]
        i += 1
    return min(dictl, key=dictl.get)
    '''
    label_k_list_tmp = sorted(label_k_list, key=lambda val: val[1])
    label_k_list_tmp = ny.array(label_k_list_tmp)
    i += 1
    pass
    return


def k_mean_class1(intx, dataset, labels, k):
    dataSet_array = ny.array(dataset)
    intX_array = ny.array(intx)
    row_len, col_len = dataSet_array.shape

    tmp_array = dataSet_array - intX_array
    tmp_array **= 2
    #sum_array = ny.array(sum(tmp_array[:, x] for x in range(col_len)))
    sum_array = tmp_array.sum(axis=1)
    # tmp_array = ny.argsort(sum_array ** 0.5)
    tmp_array = sum_array ** 0.5
    rtn_array = ny.array([[labels[i], tmp_array[i]] for i in range(row_len)])
    rtn_array = ny.array(sorted(rtn_array, key=lambda val: val[1]))
    rtndict = {}
    for i in range(k):
        key = rtn_array[i, 0]
        rtndict[key] = rtndict.get(key, 0) + 1
    rtnlist = sorted(rtndict, key=lambda val: val[1])
    return sorted(rtndict, key=lambda val: val[1])[-1]


def file2matrix(filename):
    rtnMatrix = []
    rtnLable = []
    fd = open(filename)
    i = 0
    while True:
        line = fd.readline()
        if line is None:
            pass
            # break
        tmp = line.split('\t')
        if tmp[0].isnumeric():
            rtnMatrix.append([float(i) for i in tmp[:-1]])
            rtnLable.append(tmp[-1])
        else:
            print(tmp)
            break
    rtnMatrix = ny.array(rtnMatrix)
    rtnMatrix.shape = [-1, 3]
    # rtnMatrix = rtnMatrix.reshape((-1, 3))
    return rtnMatrix, rtnLable


def auto_one(val):
    val_list = list(val)
    val_max = max(val_list)
    val_min = min(val_list)
    diff = val_max - val_min
    i = 0
    for val_cell in val_list:
        val_list[i] = (val_cell - val_min) / diff
        i += 1
    val = val_list
    return val_list


def checkresult(list_god, list_rtn):
    dtlen = len(list_god)
    r = 0
    w = 0
    for i in range(dtlen):
        if list_god[i] == list_rtn[i]:
            r += 1
        else:
            w += 1
    return w / (r + w)


def demo():
    matrix_list, lable_list = file2matrix('datingTestSet.txt')

    # auto_one(matrix_list[:, 0]);
    matrix_list[:, 0] = auto_one(matrix_list[:, 0])
    matrix_list[:, 1] = auto_one(matrix_list[:, 1])
    matrix_list[:, 2] = auto_one(matrix_list[:, 2])
    if 0 == 0:
        data_train_list = matrix_list[0:-100, :]
        lable_train_list = lable_list[0:-100]
        data_test_list = matrix_list[-100:-1, :]
        label_test_list = lable_list[-100:-1]
    else:
        data_train_list = matrix_list[100:, :]
        lable_train_list = lable_list[100:]
        data_test_list = matrix_list[0:100, :]
        label_test_list = lable_list[:100]

    lable_test_rtn_list = []
    for val in data_test_list:
        lable_test_rtn_list.append(
            k_mean_class1(
                val,
                data_train_list,
                lable_train_list,
                3))
    # rtn = k_mean_class0(data_test_list, data_train_list, lable_train_list, 20)
    lable_test_rtn_array = ny.array(lable_test_rtn_list)
    lable_test_array = ny.array(label_test_list)
    print(checkresult(label_test_list, lable_test_rtn_list))

    return


demo()
k_mean_class0(k_mean_dataX, k_mean_dataSet, k_mean_lable, 5)
