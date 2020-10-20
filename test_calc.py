#!/bash/bin/env
# -*- coding:utf8 -*-

# author: jack wu
# fuction : test calculator

import pytest,yaml
from calculator import Calc
from common.readYaml import *




class TestCalc(object):

    def setup_class(self):
        self.cc = Calc()



    def teardown_class(self):
        pass


    # @pytest.fixture(scope='module')
    # def operate(self):
    #     self.cc = Calc()
    #     print('开始计算')
    #     yeild
    #     print('结束计算')

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect',get_data()['add_data'])
    def test_add(self, a, b, expect,operate_fixture):
        result = self.cc.add(a,b)
        assert result == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expect',get_data()['add_float_data'])
    def test_add_float(self, a, b, expect):
        """根据小数的的最高位来确定最终结果的小数位数，多余位数四舍五入"""
        result = self.cc.add(a, b)
        a_point_num = len(str(a).split('.')[1])     # a小数点的位数
        b_point_num = len(str(b).split('.')[1])     # b小数点的位数
        if  a_point_num >= b_point_num:
            assert_result = round(result, a_point_num)
        else:
            assert_result = round(result, b_point_num)
        assert assert_result == expect

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('a, b, expect', get_data()['minus_data'])
    def test_minus(self, a, b, expect):
        result = self.cc.minus(a, b)
        assert result == expect

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('a, b, expect', get_data()['minus_float_data'])
    def test_minus_float(self, a, b, expect):
        result = self.cc.minus(a, b)
        a_point_num = len(str(a).split('.')[1])  # a小数点的位数
        b_point_num = len(str(b).split('.')[1])  # b小数点的位数
        if a_point_num >= b_point_num:
            assert_result = round(result, a_point_num)
        else:
            assert_result = round(result, b_point_num)
        assert assert_result == expect

    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('a, b, expect', get_data()['mul_data'])
    def test_multiple(self, a, b, expect):
        result = self.cc.multiple(a, b)
        assert result == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, expect', get_data()['div_data'])
    def test_divide(self, a, b, expect):

        result = self.cc.divide(a, b)
        if len(str(result).split('.')[1]) > 16:
            assert_result = round(result,16)
        else:
            assert result == expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b',get_data()['div_zero_data'])
    def test_divide_divisor_is_zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.cc.divide(a, b)

        try:
            result = self.cc.divide(a,b)
        except ZeroDivisionError :
            print('除数不能为零')







if __name__ == '__main__':
    pytest.main(['-v','-s',''])

