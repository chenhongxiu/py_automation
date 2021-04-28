#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Time:   2021/4/27 15:59
#@Author: shicheju
#@File:   bases.py

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Bases:

    _base_url = ""

    def __init__(self, _driver_base: WebDriver = None):
        if _driver_base is None:
            opt = webdriver.ChromeOptions()
            # 设置debug地址
            opt.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(5)

        else:
            self.driver = _driver_base
        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self,by,locator):
        """
        封装driver.find_element元素定位方法
        :return:
        """
        return self.driver.find_element(by,locator)

    def find_and_click(self,by,locator):
        ele: WebElement=self.find(by,locator)
        ele.click()
        return ele

    def finds(self,by,locator):
        return self.driver.find_elements(by,locator)
