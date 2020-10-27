#!/bash/bin/env
# -*- coding:utf8 -*-

# author: jack wu
from poweixin.page.basePage import BasePage
import pytest


class TestAddMember:

    def setup_class(self):
        self.base = BasePage()

    def teardown_class(self):
        pass

    @pytest.mark.parametrize('name,account,phone',[['jack400','12094','18900006609']])
    def test_add_member(self,name,account,phone):
        addmember = self.base.goto_add_member()
        addmember.add_member(name,account,phone)
        result=addmember.get_member()
        # result = self.base.goto_add_member().get_member()
        assert name in result


