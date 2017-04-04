import numpy as ny;
import math

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
    print(rtn_dict)

def count_feature(dataSet_list, col, key_feature):
    feature_list = [x[col] for x in dataSet_list]
    tmp_dict = {};
    for feature in feature_list:
        tmp_dict[feature] = tmp_dict.get(feature,0) + 1

    i = len(feature_list)
    for key,value in tmp_dict.items():
            tmp_dict[key] = (float)(tmp_dict[key]) / len(feature_list)
            tmp_dict[key]= round(tmp_dict[key],4)
    """
    """
    return tmp_dict
    rtn_dict[key_feature] = tmp_dict
    return rtn_dict

def create_dict_for_feature(dataSet_list, featureName_list):
    rtn_dict = spilt_feature(dataSet_list, -1, 'label')
    feature_len = len(dataSet_list[0])-1
    tmp_dict = {}
    for k,v in rtn_dict.items():
        for i in range(feature_len):
            tmp_dict['col' + str(i)] = count_feature(v,i,"col")
        tmp_dict[k] = count_feature(dataSet_list,-1,"label")
        rtn_dict[k]= tmp_dict.copy()
    return(rtn_dict)

def get_possivevalue(dataSet_dict, labelValue, featureName, featureValue):
    if labelValue in dataSet_dict.keys():
        tmp_dict = dataSet_dict[labelValue]
        if featureName in tmp_dict.keys():
            tmp_dict = tmp_dict[featureName]
            if featureValue in tmp_dict:
                return tmp_dict[featureValue]
    return 0;

def check_possive(dataSet_dict, datacheck_list):
    dict_rtn = {}
    for k,v in dataSet_dict.items():
        i = 0
        """
        possive_f = 1.0
        for val in datacheck_list:
            possive_f *= get_possivevalue(dataSet_dict,k,'col'+str(i),val);
            i+=1
        possive_f *= get_possivevalue(dataSet_dict,k,k,k);
        """
        possive_f = 0.0
        for val in datacheck_list:
            possive_f += math.log(get_possivevalue(dataSet_dict, k, 'col' + str(i), val));
            i+=1
        possive_f += math.log(get_possivevalue(dataSet_dict,k,k,k));

        dict_rtn[k] = possive_f
    return dict_rtn

dateset = [
    # {'c': {0: 'yes', 1: 'no', 2: 'no', 3: 'no'}}
    [1, 1, 0, 1, 'yes'],
    [1, 1, 0, 3, 'yes'],
    [3, 0, 0, 1, 'yes'],
    [2, 1, 1, 0, 'no'],
    [0, 3, 2, 1, 'no'],
    [1, 0, 3, 2, 'no'],
]
data_study= [
    [1,1,0,1],
    [0,0,1,0],
    [1,0,1,0],
    [1,0,0,1],
    [0,1,0,1],
    [0,1,1,0],
    [0,1,0,0],
    [0,0,1,1],
]
data_study_dict={}
data_check_study=[1,0,1]

def demo_study():
    data_study_dict = create_dict_for_feature(data_study,-1)
    i = check_possive(data_study_dict, data_check_study)
    print i;

    pass


def demo():
    color = spilt_feature(dataSet_list=dateset,col=0, key_feature='color')
    color = create_dict_for_feature(dateset,['a'])
    style = count_feature(dataSet_list=dateset,col=4, key_feature='style')
    print(color)
    print get_possivevalue(color,'yes','col2',1)

    print style

demo_study();
