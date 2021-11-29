# -*- coding:utf-8 -*-
# @Time : 2021/11/29 21:33
# Auther : shenyuming
# @File : decorator.py
# @Software : PyCharm

'''
每条用例的执行时间
'''

#----方案一----
import time

def test1():
    print('---开始测试----')
    starttime = time.time()
    time.sleep(1)
    endtime = time.time()
    print("方案一的时间是===》",endtime-starttime)
'''
问题：
    不方便维护每条用例，
    后续需求是改代码，
'''

#  ----- 方案二-------新增功能单独写---
#  调用用例，用例函数作为方法传入，
def show_time(func):
    print('---开始测试----')
    starttime = time.time()
    func()
    endtime = time.time()
    print("方案二的时间是===》",endtime-starttime)
'''
    问题：
        新增功能分开写了，但是调用时调用的是新增功能的函数，不是用例函数
'''


# --方案3--不修改原代码--不更改调用方式---装饰器技术----

def show_timetwo(func):  ##外函数
    def inner():    ## 内函数
        print('---开始测试----')
        starttime = time.time()
        func()          ## 调用外函数 ，内部函数调用外部函数变量为闭包
        endtime = time.time()
        print("方案三的时间是===》", endtime - starttime)
    return inner       ## 返回内函数对象
'''
问题：
    闭包函数好用，但是每个函数都得加代码
'''

### ----方案4---最优化---装饰器---语法糖--
def show_timethree(func):  ##外函数
    def inner(*args,**kwargs):    ## 内函数 ， 如果调用的函数有参数，内函数也要加一样的参数
        print('---开始测试----')
        starttime = time.time()
        res = func(*args,**kwargs)          ## 调用外函数 ，内部函数调用外部函数和变量为闭包 ， 如果调用的函数有参数，被调用的外部函数也要加一样的参数
        endtime = time.time()
        print("方案四的时间是===》", endtime - starttime)
        return res  ## 返回inner函数的返回值
    return inner       ## 返回内函数对象

@show_timethree
def test2():
    print('测试用例2----')
    time.sleep(1)
@show_timethree
def test3():
    print('测试用例3---')
    time.sleep(1)

@show_timethree         ## 可以有带参数的函数，测试用例有参数时在装饰器的内函数和内涵式中调用外部函数方法中也要加入响应的参数
def test4(*args,**kwargs):
    print('测试用例4----',args)
    time.sleep(1)



if __name__ == '__main__':
    # test1()
    # show_time(test1)   ## 方案二，是调用了其他的函数

    # test1 = show_timetwo(test1)  # 方案三，传入函数对象赋值给同名函数变量
    # test1()  ## 在调用

    test2()        ## 方案4
    test3()
    test4(100)   ## 方案4 带参数的函数
