#!/bash/bin/env
# -*- coding:utf8 -*-

# author: jack wu
# fuction : get data

import yaml

# class GetData(object):

def get_data():

    with open(r"./calc.yaml") as f:
        datas = yaml.safe_load(f)

        # add_data = datas["add"]
        # add_float_data = datas['add_float']
        # minus_data = datas["minus"]
        # minus_float_data = datas["minus_float"]
        # mul_data = datas["multiple"]
        # div_data = datas["divide"]
        # div_zero_data = datas["divisor_is_zero"]
        data_dict = {"add_data":datas['add'],"add_float_data":datas['add_float'],
                     "minus_data":datas['minus'],"minus_float_data":datas['minus_float'],
                     "mul_data":datas['multiple'],"div_data":datas['divide'],
                     "div_zero_data":datas['divisor_is_zero']}
    return data_dict
# [add_data,add_float_data,minus_data,minus_float_data,mul_data,div_data,div_zero_data]

print(get_data()['add_data'])
print(get_data()['add_float_data'])
