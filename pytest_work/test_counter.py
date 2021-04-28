#!/usr/bin/env python
# __*__ coding:utf-8 __*__
# @Time : 2021/4/7 5:15 下午
# @Author : shicheju
# @File : test_counter.py


import pytest

from get_data import get_data


class TestCounter:


    @pytest.mark.parametrize("a,b,expect",get_data()['add_int']['data'],ids=get_data()['add_int']['ids'])
    def test_add_int(self,get_counter,a,b,expect):
        assert get_counter.add(a,b) == expect

    @pytest.mark.parametrize("a,b,expect", get_data()['add_float']['data'], ids=get_data()['add_float']['ids'])
    def test_add_float(self,a,b,expect,get_counter):
        assert round(get_counter.add(a,b),2) == expect

    @pytest.mark.parametrize("a,b,expect", get_data()['div']['data'], ids=get_data()['div']['ids'])
    def test_div(self, get_counter, a, b, expect):
        assert get_counter.div(a, b) == expect

    @pytest.mark.parametrize("a,b",[[1,0]])
    def test_div_error(self,get_counter, a, b):
        with pytest.raises(ZeroDivisionError):
            get_counter.div(a,b)


