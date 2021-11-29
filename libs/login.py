# -*- coding:utf-8 -*-
# @Time : 2021/11/14 16:23
# Auther : shenyuming
# @File : login.py
# @Software : PyCharm

from common.baseApi import BaseAPI
from configs.config import NAME_PSW
from utils.handle_data import MD5_login
import copy
from utils.decorator import show_timethree

# NAME_PSW = {'username':'ka0518','password':'xintian'}


'''
登录模块的作用：
    本身的登录自动化
    业务接口需要token
'''
class Login(BaseAPI):
    @show_timethree  ## 用例执行时间装饰器
    def login(self,inData,getToken=False):  #自定义一个变量token默认是false, 调用时如果不传值就是false，如果传true就返回token
        inData = copy.copy(inData)      ##复制数据，
        inData['password'] = MD5_login(inData['password']) ##加密
        resData = self.request_send(inData)    ## 发送请求

        if getToken:
            return resData['data']['token']
        else:
            return resData
        # print(resData.text)

if __name__ == '__main__':
    print(Login().login(NAME_PSW))

#,getToken=True