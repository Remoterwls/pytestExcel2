#!usr/bin/env python
# encoding:utf-8
'''
__Author__: Jack Wu
__function__：
'''
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from app.del_contacts.address_list_page import AddressListPage
from app.del_contacts.base_page import BasePage


class HomePage(BasePage):


    def goto_address_book(self)-> AddressListPage:
        self.find_and_click('xpath',"//*[@text='通讯录']")
        return AddressListPage(self.driver)

