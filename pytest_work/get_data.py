#!/usr/bin/env python
# __*__ coding:utf-8 __*__
# @Time : 2021/4/7 6:27 下午
# @Author : shicheju
# @File : get_data.py
import yaml


def get_data():

    with open("/Users/chenhongxiu/Desktop/py_automation/work/pytest_work/data.yaml",encoding="UTF-8") as  f:
        data=yaml.safe_load(f)
    return data