# -*- coding:utf-8 -*-
# @Time : 2021/11/14 20:35
# Auther : shenyuming
# @File : handle_excel.py
# @Software : PyCharm

'''
    -------v1.0--------
    分析需求：
    1- 获取具体哪些数据
        1- 用例标题
        2- 请求body
        3- 预期响应结果
    2- 需要返回什么类型
        1- 客户需要把读取的数据给test_login()   使用的是pytest--数据驱动的方法
            [(),(),()]
    解决方案：
    1- 操作execcl库是什么
        1- xlrd  xlwt  操作xx.xls----选定
            xlrd 读操作
            xlwt 写操作---新建一个文件
            xlutils 写操作  在已有的excel文件里修修改（写）
        2- openpyxl   操作xx.xlxs
        3- panda  大数据场景

'''
##  只读不写，不用写类了，

import xlrd
from utils.handle_path import testdata_path
import os

def get_excel_data(excelDir,sheetNanme=None):
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

## -----  获取对应的需求数据-------
    rowIndex = 0          ## 定义行的初始值
    for one in workSheet.col_values(0):
        reqBody = workSheet.cell(rowIndex,9).value   ## 获得请求的参数
        respBody = workSheet.cell(rowIndex,11).value  ## 获得响应结果
        resList.append((reqBody,respBody))  ## 将数据存入list [(请求1，响应1),(请求2，响应2)]
        rowIndex += 1 # 取完一次+1

    for i in resList:
        print(i)

"""
---------------版本 v1.0---------------
测试反馈：
    1- 如果里面有非这个接口需要的用例，会导致自动化测试失败
    2- 如果后续需要获取其他列数据---没有办法-只能改代码！
版本迭代建议：
    1- 需要传递一个对应的接口的筛选的条件 
    2- 提供扩展性  以后可能需要获取用例标题
"""




if __name__ == '__main__':
    filepath = os.path.join(testdata_path,'test_devolop.xls')
    get_excel_data(filepath,'登录模块')



