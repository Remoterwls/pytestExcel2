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


    def del_contact(self):
        """
            删除联系人
        :return: None
        """
    # 点击搜索按钮
        self.find_and_click('id','com.tencent.wework:id/hxw')
    # 输入关键字并搜索
        self.find_and_input('id','com.tencent.wework:id/ghu','demo2')
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

    def get_del_result(self):
        # # 元素找到了，返回一个False,有超时就返回一个true
        # from selenium.common.exceptions import TimeoutException
        # try:
        #     self.find('id','com.tencent.wework:id/dkf')
        #     return False
        # except TimeoutException:
        #     return True
        # self.find_and_input('id', 'com.tencent.wework:id/ghu', 'demo2')
        loctor = (By.XPATH,'//*[@text="无搜索结果"]')
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(*loctor))
        result = self.find('xpath','//*[@text="无搜索结果"]').get_attribute('text')
        # print(result)
        return result







