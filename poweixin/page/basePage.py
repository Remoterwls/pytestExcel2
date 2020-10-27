#!/bash/bin/env
# -*- coding:utf8 -*-

# author: jack wu

from selenium.webdriver.common.by import By

from poweixin.page.add_member_page import AddMemberPage
from poweixin.page.page_index import PageIndex


class BasePage(PageIndex):

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, '.ww_indexImg.ww_indexImg_AddMember').click()
        return AddMemberPage(self.driver)

