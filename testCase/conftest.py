# -*- coding:utf-8 -*-
# @Time : 2021/11/23 15:14
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm

'''
作用域： 只作用于所在包,
 autouse设置true不需要import调用，pytest运行测试类会自动调用，
 autouse设置false 需要手动调用，默认是false ,
    有返回值的调用：
    没有返回值的调用：在需要的文件的类上方@pytest.mark.usefixtures('函数名')
'''
import pytest
from libs.login import Login
from configs.config import NAME_PSW
from libs.shop import Shop

@pytest.fixture(scope='session',autouse=True) ## autouse=true 会自动调用
def start_runing():
    print("自动化之执行前先运行开始，，，")
    yield       ##没有返回值，
    print("自动化运行后调用的，，，，")

@pytest.fixture(scope='class')
def shenym():
    print('没有autouse，没有返回值的fixture')


## -----登录操作------
##  有返回值的fixture，直接使用函数名就是代表返回值，  login_init == token
@pytest.fixture(scope='session')
def login_init():
    print('-----用户登录操作--没有自动调用但有返回值--')
    token = Login().login(NAME_PSW,getToken=True)
    yield token   ## yiled 相当于 teardown ,返回数据后还可以再继续往下执行
    print("---可以继续登录完成后的---")

## -----店铺实例操作-----
@pytest.fixture(scope='class')
def shop_init(login_init):   ## 直接写入登录的函数，就是传入登录返回的token
    print('店铺实例创建开始---')
    shopObject = Shop(login_init)
    yield shopObject
    print('店铺实例创建完成---')