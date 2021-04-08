#!/usr/bin/env python
# __*__ coding:utf-8 __*__
# @Time : 2021/4/8 11:10 上午
# @Author : shicheju
# @File : get_data.py

import yaml

def get_data():

    with open("./data.yaml",encoding="UTF-8") as f:
        data=yaml.safe_load(f)
    return data

def get_aniaml_datas():

    cat_values=get_data()["cat"]
    dog_values=get_data()['dog']
    return cat_values,dog_values
