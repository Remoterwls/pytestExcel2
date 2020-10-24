#!usr/bin/env python
# encoding:utf-8

"""
__Author__: Jack Wu
__function__：dd

"""
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddContacts(object):

    def setup(self):
        self.url = "https://work.weixin.qq.com/wework_admin/frame"
        self.file_path = r"C:\Users\jackw\Desktop\通讯录信息导入.xlsx"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        with shelve.open('cookies') as db:
            cookies = db['cookie']
        self.driver.get(self.url)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def teardown(self):
        self.driver.quit()

    def test_add_contacts(self):
        add_cont_button_css = '.ww_indexImg.ww_indexImg_Import'
        upload_file_css = '.ww_fileImporter_fileContainer_uploadInputMask'
        upload_botton_css = '.ww_fileImporter_submitWrap > a'
        self.driver.find_element(By.CSS_SELECTOR, add_cont_button_css).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, upload_file_css).send_keys(self.file_path)
        self.driver.find_element(By.CSS_SELECTOR,upload_botton_css)
        assert_ele = '.ww_fileImporter_fileContainer_fileNames'
        result = self.driver.find_element(By.CSS_SELECTOR,assert_ele).text
        print(result)
        assert result == '通讯录信息导入.xlsx'


