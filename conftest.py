#!/bash/bin/env
# -*- coding:utf8 -*-

# author: jack wu
# fuction : test calculator


import pytest
from test_calc import TestCalc
from calculator import Calc


@pytest.fixture(scope='module')
def operate_fixture():
    cc = Calc()
    print('【开始计算】')
    yield cc
    print('【结束计算】')


