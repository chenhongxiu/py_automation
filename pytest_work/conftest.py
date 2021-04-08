#!/usr/bin/env python
# __*__ coding:utf-8 __*__
# @Time : 2021/4/7 5:52 下午
# @Author : shicheju
# @File : conftest.py



import pytest

from work.pytest_work.counter import Counter


@pytest.fixture()
def get_counter():
    counter=Counter()
    print("开始计算")
    yield counter
    print("结束计算")





