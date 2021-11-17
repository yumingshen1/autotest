# -*- coding:utf-8 -*-
# @Time : 2021/11/14 20:14
# Auther : shenyuming
# @File : test_login.py
# @Software : PyCharm
'''
    测试文件执行条件
        该业务层代码封装OK
        需要自动化测试用例-- 数据驱动
'''

from libs.login import Login
from utils.handle_excel3 import get_excel_data
import pytest,allure,os
from utils.handle_path import report_path
from common.baseApi import ApiAssert

@allure.epic('项目')
@allure.feature('登陆模块')
class TestLogin:
    @pytest.mark.parametrize('title,inBody,expData',get_excel_data('登录模块','login','标题','请求参数','响应预期结果'))
    @allure.title("{title}")
    def test_login(self,title,inBody,expData):

        res = Login().login(inBody)

        assert res['msg'] == expData['msg']

if __name__ == '__main__':
    pytest.main(['test_login.py','-s','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure server {report_path}')