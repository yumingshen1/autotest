# -*- coding:utf-8 -*-
# @Time : 2021/11/14 15:32
# Auther : shenyuming
# @File : baseApi.py
# @Software : PyCharm


import requests
from utils.handle_yml import get_yaml_data
import inspect
from configs.config import HOST

class BaseAPI:
    ##每个继承基类的子类都调用初始化方法，初始化方法将数据配置文件读取
    def __init__(self):
        ## 获得数据后取 调用基类的子类的类名字，因为yaml文件数据是按类名字写入的字典格式数据，
        ## 用类名当键，字典中用键的名字可以取到对应的数据
        self.data = get_yaml_data('../configs/apiConfig.yml')[self.__class__.__name__]


    ## 封装请求，四种请求类型都在requests.request中，因为四类请求方式最后都是返回的request所以直接用rewuest

    def request_send(self,data=None):
        ## 初始化方法中获得的 self.data 是整个模块的数据，例如整个登录的模块的
        ## 登录中有多个小模块方法， 每个方法只取自己需要的值，
        try:
            methodName = inspect.stack()[1][3]   ## inspect.stack()[1][3] 固定写法，意思是谁调用当前函数，就返回会谁的函数名

            print(self.data[methodName])
            print(type(self.data[methodName]))
            ## 将数据剥离 , 获取的类作为键， 只取键对应的值
            path,method = self.data[methodName].values()
            resp = requests.request(method=method,url=f'{HOST}{path}',data=data)

            return resp.json()
        except Exception as e:
            print('错误信息--->',e)
            raise e

class ApiAssert:
    def define_api_assert(self,result,condition,exp_result):
        try:
            if condition == '=':
                assert result == exp_result
            elif condition == 'in':
                assert result in exp_result
        except Exception as error:
            raise error

