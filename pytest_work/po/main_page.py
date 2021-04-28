#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time:   2021/4/27 15:42
#@Author: shicheju
#@File:   main_page.py


import time
from selenium.webdriver.common.by import By

from work.pytest_work.po.addstaff_page import AddMember
from work.pytest_work.po.bases import Bases
from work.pytest_work.po.contact_page import Contact


class MainPage(Bases):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_contact(self):
        time.sleep(2)
        self.find_and_click(By.ID,"menu_contacts")
        return Contact(self.driver)


    def goto_addmember(self):

        self.find_and_click(By.CSS_SELECTOR,".js_service_list .index_service_cnt_itemWrap:nth-child(1)")
        return AddMember(self.driver)