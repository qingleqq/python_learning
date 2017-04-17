import numpy as ny

import re


def get_data(filename):
    rtnMatrix = []
    rtnLable = []
    fd = open(filename)
    re_cmp = re.compile(r'^[+-]{0,1}\d*\.{0,1}\d*\t[+-]{0,1}\d*\.{0,1}\d*\t[01]\r\n$')
    i = 0;
    while True:

        line = fd.readline()
        if line is None:
            break
        k = re_cmp.findall(line)
        if len(k) != 0:
            tmp = line.split('\t')
            tmplist = [1]
            tmplist.extend([float(val) for val in tmp[:-1]])
            rtnMatrix.append(tmplist)
            rtnLable.append(int(tmp[-1]))
        else:
            print(tmp)
            break

    rtnMatrix = ny.array(rtnMatrix)
    rtnMatrix.shape = [-1, 3]
    # rtnMatrix = rtnMatrix.reshape((-1, 3))
    return rtnMatrix, rtnLable

def pre_tread(feature_array):
    num_samples, num_features = feature_array.shape
    rtn_list = []
    for i in range(num_features):
        tmp = feature_array[:,i];
        max_v = max(tmp)
        min_v = min(tmp)
        rtn_list.append((tmp-min_v)/(max_v-min_v))
    rtn_array = ny.array(rtn_list).transpose()
    return rtn_array

def sigmoid(feature_matrix, w_matrix):
    #tmp = (feature_matrix*w_matrix)
    tmp = 1.0 / (1 + ny.exp(-1*(feature_matrix*w_matrix)))
    return tmp

def per_step(feature_matrix, weight_matrix, label_matrix):
    label_matrix = label_matrix.transpose()
    sigmoid_matrix = sigmoid(feature_matrix, weight_matrix.transpose())
    diff_matrix = label_matrix - sigmoid_matrix
    rtn_matrix = feature_matrix.transpose() * diff_matrix
    return rtn_matrix

    """
    sum_v = 0
    for i in range(feature_num_col):
        sum_v += (sigmoid(feature_array[i],weight_array)-label_array[i])*feature_array[i,y]
    weight_array[j] = weight_array[j] - alpha*sum_v
    """
def compute_weight(feature_list, label_list):
    feature_matrix = ny.matrix(feature_list)
    label_matrix = ny.matrix(label_list)
    sample_num, feature_num = feature_matrix.shape
    weight_array =  ny.ones(feature_num)
    weight_matrix =  ny.matrix(weight_array)
    alpha = 0.001

    for i in xrange(500):
        tmp = alpha * per_step(feature_matrix,weight_matrix,label_matrix)
        rtn_next_w =  weight_matrix + tmp.transpose()
        weight_matrix = rtn_next_w

    print weight_matrix
    return 0


def test_vector():
    vector0 = ny.linspace(1,20,20)
    vector1 = ny.linspace(start=2, stop=20, num=10,endpoint=1)
    vector0.shape = -1,10
    vector3 = vector0*vector1
    vector3_1 = vector0[0]*vector1
    tmp = vector0[:,1]
    vector3_2 = vector0*tmp
    tmp = sum(vector3)

    vector4 = (vector0-vector1)
    vector5 = (vector1+vector0)

    print(tmp,vector4)

def demo():
    #match = re.compile('[^+-]{0,1}\d{0,}\.\d{0,}$')
    r'^\d+&'
    feature_array,label_array = get_data('/opt/qingleqq/work/app/python_study/python_learning/ai/logistic-regression/testSet.txt')
    #feature_array = pre_tread(feature_array)
    #print (feature_array,label_array);

    compute_weight(feature_array,label_array)


demo();
#test_vector()