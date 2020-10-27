#!/bash/bin/env
# -*- coding:utf8 -*-

# author: jack wu

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from poweixin.page.page_index import PageIndex


class AddMemberPage(PageIndex):
    driver:WebDriver

    def add_member(self,name,account,phone):
        # 输入名字

        self.find(By.CSS_SELECTOR,'#username').send_keys(name)
        # 输入账号
        self.find(By.CSS_SELECTOR,'#memberAdd_acctid').send_keys(account)
        # 输入手机号
        self.find(By.CSS_SELECTOR,'#memberAdd_phone').send_keys(phone)
        # 保存
        self.find(By.CSS_SELECTOR,'a.js_btn_save').click()
        return True

    def get_member(self):
        base_ele = self.finds(By.CSS_SELECTOR, 'tr>td:nth-child(2)')
        loc = (By.CSS_SELECTOR, 'tr>td:nth-child(2)')
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
        member_list = []
        for i in range(len(base_ele)):
            member_list.append(base_ele[i].text)
        return member_list

