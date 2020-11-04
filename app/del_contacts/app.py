#!usr/bin/env python
# encoding:utf-8
'''
__Author__: Jack Wu
__function__：
'''

from appium import webdriver
from app.del_contacts.base_page import BasePage
from app.del_contacts.home_page import HomePage


class App(BasePage):

    def start(self):
        """
        启动app
        :return:
        """
        if self.driver == None:
           url = 'http://localhost:4723/wd/hub'

           caps = {}
           caps["platformName"] = "Android"
           caps["deviceName"] = "hogwarts"
           caps["appPackage"] = "com.tencent.wework"
           caps["appActivity"] = ".launch.LaunchSplashActivity"
           # noReset 保留缓存， 比如登录状态
           caps["noReset"] = "True"
           caps["dontStopAppOnReset"] = "true"
           caps['skipDeviceInitialization'] = 'true'
           caps['skipServerInstallation'] = 'true'
           self.driver = webdriver.Remote(url,caps)
           self.driver.implicitly_wait(15)
        else:
           self.driver.launch_app()
        # 停留在start状态上
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.launch_app()

    def goto_home(self):
        """
        进入主页
        :return: HomePage
        """
        return HomePage(self.driver)

    def get_page_source(self):
        return self.driver.page_source
