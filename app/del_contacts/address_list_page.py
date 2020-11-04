#!usr/bin/env python
# encoding:utf-8
'''
__Author__: Jack Wu
__function__：
'''

import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app.del_contacts.base_page import BasePage



class AddressListPage(BasePage):

    def del_contact(self,keyword):
        """
            删除联系人
        :return: None
        """
    # 点击搜索按钮
        self.find_and_click('id','com.tencent.wework:id/hxw')
    # 输入关键字并搜索
        self.find_and_input('id','com.tencent.wework:id/ghu',keyword)
    # 获取结果并点击
        self.find_and_click('id','com.tencent.wework:id/dkf')
    # 点击编辑按钮
        self.find('id','com.tencent.wework:id/hxm').click()
    # 点击编辑成员
        self.find_and_click('id','com.tencent.wework:id/b91')
    # 点击删除按钮
        self.find_and_click('id','com.tencent.wework:id/eh7')
    # 点击确认删除
        self.find_and_click('id','com.tencent.wework:id/bjp')

        from app.del_contacts.search_page import SearchPage
        return SearchPage(self.driver)

    def goto_search_page(self):
        self.find_and_click('id','com.tencent.wework:id/hxw')
        from app.del_contacts.search_page import SearchPage
        return SearchPage(self.driver)





