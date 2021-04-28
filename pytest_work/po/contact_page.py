#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time:   2021/4/27 16:12
#@Author: shicheju
#@File:   contact_page.py
import time

from selenium.webdriver.common.by import By

from work.pytest_work.po.addstaff_page import AddMember
from work.pytest_work.po.bases import Bases


class Contact(Bases):

    def click_add_member(self):
        time.sleep(3)
        while True:
            # 解元组
            self.find_and_click(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
            ele_num = len(self.finds(By.ID, "username"))
            if ele_num > 0:
                break
        return AddMember(self.driver)

    def get_member(self):
        time.sleep(1)
        ele_list = []
        ele_num = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        for value in ele_num:
            ele_list.append(value.get_attribute("title"))
        return ele_list
