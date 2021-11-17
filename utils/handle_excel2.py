# -*- coding:utf-8 -*-
# @Time : 2021/11/14 22:57
# Auther : shenyuming
# @File : handle_excel2.py
# @Software : PyCharm
# -*- coding:utf-8 -*-
# @Time : 2021/11/14 20:35
# Auther : shenyuming
# @File : handle_excel.py
# @Software : PyCharm


"""
---------------版本 v2.0---------------
需求：
    1- 需要传递一个对应的接口的筛选的条件
    2- 提供扩展性  以后可能需要获取用例标题
分析需求：
解决方案：
    1- 我们不清楚后续需要获取哪些列数据--可以考虑使用可变数量参数  *args
测试反馈：
版本迭代建议：

"""
##  只读不写，不用写类了，

import xlrd
from utils.handle_path import testdata_path
import os

'''
excelDir,文件路径
sheetNanme,子sheet名字
caseName,用例编号，判断sheet中是否存入其他模块的用例，
*args 为方便用例运行时取值的列，不定列
'''

def get_excel_data(excelDir,sheetNanme,caseName,*args):
    ## 定义list，存放传入的参数和预期结果
    resList = []

    ##打开一个文件
    workbook = xlrd.open_workbook(excelDir,formatting_info=True)  # formatting_info=True ----> 保持原样式

    ##获取所有的子表名
    #sheets = workbook.sheet_names()
    # print(sheets)

    ## 获取对应需要操作的子表
    workSheet = workbook.sheet_by_name(sheetNanme)

    ## 获取一列数据
    #print(workSheet.col_values(0))

    ## 获取一行数据
    #print(workSheet.row_values(0))

    ## 获取单元格数据 cell(行，列)
    #print(workSheet.cell(0,0).value)


    # --------v2.0新增功能--------------------
    # args---元组类型  ('URL'，‘标题’,'请求体')
    """
    需求分析：用户传入需要获取的列 ，代码去获取对应的列的单元格数据
    方案：
        1- 用户可以这样去调用函数  直接传递列编号 1,3,5,6---> args
            get_excel_data(excelDir,sheetName,caseName,1,3,5,6)
            感受：
                1-代码可读性差
                2- 你内部代码操作起来是方便的
        2- 用户可以这样去调用函数  直接传递-'URL'，‘标题’,'请求体'---> args
            get_excel_data(excelDir,sheetName,caseName,'URL'，‘标题’,'请求体')
            感受：
                1-代码可读性好，好理解业务需求
                2- 你内部代码操作起来是不方便： 需要把列名--转化为---列编号
    """
    ###  取出所有的列名
    colIndexList =[] ## 定义空的list， 存放数据行名称
    for i in args:
        colIndexList.append(workSheet.row_values(0).index(i))
    print(colIndexList)


## -----  获取对应的需求数据-------
    rowIndex = 0          ## 定义行的初始值
    for one in workSheet.col_values(0):
        if caseName in one:                         ## 判断需要测试的模块是否有其他模块的测试用例，用编号去判断
            ## 遍历列编号
            ## 定义list存放 每一次循环的数据
            getColData = []
            for num in colIndexList:
                tmp = workSheet.cell(rowIndex,num).value
                getColData.append(tmp)

            resList.append(list(getColData))  ## 将数据存入list [(请求1，响应1),(请求2，响应2)]
        rowIndex += 1 # 取完一次+1

    for i in resList:
        print(i)


"""
---------------版本 v2.0---------------
数据处理的思维：
    1- 直接获取数据，在登录的业务代码去转化
    2- 在获取数据的 源头就把数据搞好！
测试反馈：
    1- 外卖自动化业务代码，都需要字典类型---excel获取出来是字符串类型
        1- 像url  不是json---不需要转化
        2- 像请求的body，是json ---需要转化
    2- 做测试--冒烟测试--不是全部去执行所有的用例---用例执行筛选！

    pytest框架的定制化执行：
        1- -mark  指定对应的接口跑自动化---不能选择里面具体某一条用例
        2- 数据层定制  数据驱动，我们筛选出我们需要执行的用例条数
"""

if __name__ == '__main__':
    filepath = os.path.join(testdata_path,'test_devolop.xls')
    get_excel_data(filepath,'登录模块','Login','请求参数','响应预期结果') ## 传入data地址，sheet名字，测试用例编号



