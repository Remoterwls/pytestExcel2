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
        pass

    def test_del_contact_success(self):
        self.home.goto_address_book().del_contact()
        assert 'demo2' not in self.app.get_page_source()

if __name__ == '__main__':
    pytest.main(['-s','-v',''])








