#!usr/bin/env python
# encoding:utf-8
'''
__Author__: Jack Wu
__function__：
'''

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver:WebDriver = None):
        self.driver = driver

    def find(self, type, value):
        if type == 'xpath':
            ele = self.driver.find_element(MobileBy.XPATH,value)
        elif type == 'css':
            ele = self.driver.find_element(MobileBy.CSS_SELECTOR,value)
        elif type == 'id':
            ele = self.driver.find_element(MobileBy.ID, value)
        return ele

    def find_and_input(self,type,value,text):
        self.driver.find_element(type,value).send_keys(text)

    def finds(self,type,value):
        if type == 'xpath':
            ele = self.driver.find_elements(MobileBy.XPATH,value)
        elif type == 'css':
            ele = self.driver.find_elements(MobileBy.CSS_SELECTOR,value)
        elif type == 'class_name':
            ele = self.driver.find_element(MobileBy.CLASS_NAME,value)
        return ele

    def find_not_exist(self,type,value):
        if type == 'id':
            return WebDriverWait(self.driver,10,1).until_not(lambda x:x.find_elements(MobileBy.ID,value))


    def find_and_click(self,type,value):
        if type == 'id':
            element = self.driver.find_element(MobileBy.ID,value)
            element.click()
        elif type == 'xpath':
            element = self.driver.find_element(MobileBy.XPATH,value)
            element.click()
        elif type == 'css':
            element = self.driver.find_element(MobileBy.CSS_SELECTOR,value)
            element.click()

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')


