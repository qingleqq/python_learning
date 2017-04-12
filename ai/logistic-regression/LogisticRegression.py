import numpy as ny


def get_data():
    feature_list = []
    label_list = []
    return feature_list, label_list


def vector_dot(vector_0, vector_1):
    rtn_vector = [ i_vector_0 * i_vector_1 for i_vector_0, i_vector_1 in zip( vector_0, vector_1)]
    return sum(rtn_vector)


def sigmoid(feature_list, w_list):
    return 1.0 / (1 + ny.math.exp(-1 * sum(feature_list*w_list)))


def next_weight(feature_list, label_list, weight_list):
    feature_array = ny.array(feature_list)
    label_array = ny.array(label_list)
    feature_num_row,feature_num_col = feature_array.shape()
    weight_array = ny.ones(feature_num_row)
    rtn_next_w = []
    alpha = 0.003
    while True:
        for j in range(feature_num_row):
            """
            sum_v = 0
            for i in range(feature_num_col):
                sum_v += (sigmoid(feature_array[i],weight_array)-label_array[i])*feature_array[i,y]
            weight_array[j] = weight_array[j] - alpha*sum_v
            """
            rtn_next_w[j] = weight_array[j] + alpha*\
                                              ((sigmoid(feature_array,weight_array)-label_array)
                                               *feature_array[:,j])
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

test_vector()