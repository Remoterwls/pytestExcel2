#!usr/bin/env python
# encoding:utf-8

'''
__Author__: Jack Wu
__function__：
'''

import pytest
from app.del_contacts.app import App


class TestDelContact:

    def setup_class(self):
        self.app = App()

    def teardown_class(self):
        self.app.restart()

    def setup(self):
        self.home = self.app.start().goto_home()

    def teardown(self):
        self.app.stop()

    def test_del_contact_success(self):
        keyword = 'demo6'
        # 通讯录页面
        goto_address = self.home.goto_address_book()
        # 搜索页面
        search_page = goto_address.goto_search_page()
        # 删除指定成员名前搜索结果
        before = search_page.get_member_count(keyword)
        # 返回到通讯录页面
        back_address = search_page.back_address_book_page()
        # 删除成员并回到搜索页面
        search_page = back_address.del_contact(keyword)
        # 删除指定成员名后搜索结果
        after = search_page.get_member_count(keyword)
        assert after == before - 1


if __name__ == '__main__':
    pytest.main(['-s','-v',''])








