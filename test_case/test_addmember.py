#!/usr/bin/env python
# __*__ coding:utf-8 __*__
# @Time : 2021/4/28 5:41 下午
# @Author : shicheju
# @File : test_addmember.py


import pytest
import allure

from work.po.main_page import MainPage


class TestAddMember:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass


    @allure.story("测试通讯录页面添加成员")
    @pytest.mark.parametrize("name,id,phone",[("shicheju","101701","15800000001")])
    def test_add_member1(self,name,id,phone):
        ele=self.main.goto_contact().click_add_member().addmenber(name,id,phone).get_member()
        assert phone in ele

    @pytest.mark.skip
    @allure.story("测试首页添加成员")
    @pytest.mark.parametrize("name,id,phone",[("shicheju2", "101702", "15800000002")])
    def test_add_member2(self, name, id, phone):
        ele = self.main.goto_addmember().addmenber(name,id,phone).get_member()
        assert phone in ele