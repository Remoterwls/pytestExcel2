#!/bash/bin/env
# -*- coding:utf8 -*-

# author: jack wu


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageIndex:
    base_url = ''
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            options = Options()
            options.debugger_address = 'localhost:9222'
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self.base_url != '':
            self.driver.get(self.base_url)

    def find(self,*loctor):
        ele = self.driver.find_element(*loctor)
        self.driver.implicitly_wait(10)
        return ele
        # if ele:
        #     self.driver.implicitly_wait(3)
        #     return ele
        # else:
        #     WebDriverWait(self.driver,5,1).until(EC.visibility_of_element_located(ele))
        #     return ele


    def finds(self,*loctor):
        eles = self.driver.find_elements(*loctor)
        self.driver.implicitly_wait(10)
        return eles
        # if eles:
        #     self.driver.implicitly_wait(3)
        #     return eles
        # else:
        #     WebDriverWait(self.driver,5,1).until(EC.visibility_of_element_located(ele))
        #     return eles





