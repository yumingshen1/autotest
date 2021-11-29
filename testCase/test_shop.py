# -*- coding:utf-8 -*-
# @Time : 2021/11/22 19:59
# Auther : shenyuming
# @File : test_shop.py
# @Software : PyCharm

import pytest
import allure,os
from utils.handle_excel3 import get_excel_data
from utils.handle_path import report_path,testdata_path
from common.baseApi import ApiAssert
from libs.shop import Shop

## 定义跳过的skip
no_ready = pytest.mark.skip(reason='店铺的列出接口后端没有实现，暂时不运行！')  ## 自定义无条件跳过，其他方法上可以直接 @no_ready

# @pytest.mark.usefixtures('shenym')  ##没有返回值的的调用
@allure.epic('learning')
@allure.feature('店铺模块')
@pytest.mark.shop       ## 起名字用于-m参数时选择运行用例
class TestShop:
    # 1 - 列出店铺
    @allure.story('列出店铺')
    @pytest.mark.parametrize('title,inBody,expData', get_excel_data('我的商铺', 'listshopping', '标题', '请求参数', '响应预期结果'))
    @allure.title('{title}')
    @pytest.mark.shop_list   ## 起名字用于-m参数时选择运行用例
    @no_ready   ##定义的跳过skip
    def test_shop_list(self,title,inBody,expData,shop_init):
        res = shop_init.query(inBody)
    #  - 断言
        ApiAssert.define_api_assert(res["code"],'=',expData["code"])


    # # 2- 更新店铺
    @allure.story('更新店铺')
    @pytest.mark.parametrize('title,inBody,expData', get_excel_data('我的商铺', 'updateshopping', '标题', '请求参数', '响应预期结果'))
    @allure.title('{title}')
    @pytest.mark.shop_update         ## 起名字用于-m参数时选择运行用例
    def test_shop_update(self,shop_init,title,inBody,expData):
        with allure.step('1-登录+创建店铺'):
            pass
        with allure.step('2-获取店铺id'):
            res = shop_init.query({"page": "1", "limit": "10"})
            shopID = res['data']['records'][0]['id']
        with allure.step('3-文件上传操作'):
            res2 = shop_init.file_upload(os.path.join(testdata_path, 'ss.jpg'))
            fileInfo = res2['data']['realFileName']
        with allure.step('4-更新店铺'):
            res2 = shop_init.update(inBody,shopID,fileInfo)
        with allure.step('5-断言'):
            ApiAssert.define_api_assert(res2['code'],'=',expData['code'])

if __name__ == '__main__':
    pytest.main(['test_shop.py', '-s', '--alluredir', f'{report_path}', '--clean-alluredir'])
    os.system(f'allure serve {report_path}')