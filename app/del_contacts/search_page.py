#!usr/bin/env python
# encoding:utf-8
'''
__Author__: Jack Wu
__function__：
'''
import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions

from app.del_contacts.base_page import BasePage


class SearchPage(BasePage):



    def get_member_count(self,keyword):
        time.sleep(0.5)
        from selenium.webdriver.support.wait import WebDriverWait
        self.find_and_input('id','com.tencent.wework:id/ghu',keyword)
        # loctor = (MobileBy.XPATH,f'//*[@class="android.widget.ListView"]//*[@text="{keyword}"]')
        # WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(loctor))
        time.sleep(1.5)
        result = len(self.finds('xpath',f'//*[@class="android.widget.ListView"]//*[@text="{keyword}"]'))
        print('获取的指定删除的成员个数：',result)
        print(time.time)
        return result

    def back_address_book_page(self):
        self.find_and_click('id','com.tencent.wework:id/hxb')
        from app.del_contacts.address_list_page import AddressListPage
        return AddressListPage(self.driver)