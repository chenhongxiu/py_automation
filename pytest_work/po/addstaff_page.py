#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time:   2021/4/27 15:58
#@Author: shicheju
#@File:   addstaff_page.py

from selenium.webdriver.common.by import By

from work.pytest_work.po.bases import Bases



class AddMember(Bases):


    def addmenber(self,name,id,phone):
        #局部导入
        from work.pytest_work.po.contact_page import Contact
        # self.driver.find_element_by_id("username").send_keys(name)
        # self.driver.find_element_by_id("memberAdd_acctid").send_keys(id)
        # self.driver.find_element_by_id("memberAdd_phone").send_keys(phone)
        # self.driver.find_element_by_css_selector(".qui_btn.ww_btn.js_btn_save").click()
        self.find(By.ID,"username").send_keys(name)
        self.find(By.ID,"memberAdd_acctid").send_keys(id)
        self.find(By.ID,"memberAdd_phone").send_keys(phone)
        self.find_and_click(By.CSS_SELECTOR,".qui_btn.ww_btn.js_btn_save")
        return Contact(self.driver)


