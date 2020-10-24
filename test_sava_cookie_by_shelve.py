#!usr/bin/env python
# encoding:utf-8
'''
__Author__: Jack Wu
__function__：Use cookies to bypass login and add contacts
'''
import shelve

import pytest, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSeleniumCookies(object):

    """
    command_line method: chrome --remote-debugging-port=9222
    127.0.0.1 = localhost
    port is changeable

    """

    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown(self):
        self.driver.quit()

    def test_get_cookie(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        return cookies

    def test_save_cookies(self):
        print(self.driver.get_cookies())
        with shelve.open('cookies') as db:
             db['cookie'] = self.test_get_cookie()

    @pytest.mark.skip
    def test_assert_data_dir(self):
        pass





