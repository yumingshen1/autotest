# -*- coding:utf-8 -*-
# @Time : 2021/11/14 23:51
# Auther : shenyuming
# @File : handle_excel3.py
# @Software : PyCharm
"""
---------------版本 v3.0---------------
需求：
    1- 需要对测试用例进行挑选
        全部：1，2，3，4，5
        挑选出：优先级高/特定用例bug回归
分析需求：
    用例挑选的方式：
        1- 全部 all
        2- 只选择某一个用例  tc001
        3- 连续的用例  tc003-tc005
        4- 复合型  ['tc003','tc007-tc009','tc010']
解决方案：

测试反馈：
    函数调用的参数传递的太多！
        get_excel_data(fileDir,'登录模块','Login','URL','标题','前置条件')
版本迭代建议：

"""
"""
---------------版本 v4.0---------------
需求：    
    函数调用的参数传递的太多！
        get_excel_data(fileDir,'登录模块','Login','URL','标题','前置条件')
分析需求：
    配置文件出去
        ini
        yaml
解决方案：
    尽可能使用代码去识别获取！

测试反馈：
版本迭代建议：
"""


##  只读不写，不用写类了，

import xlrd
from utils.handle_path import testdata_path
import os
import json
'''
excelDir,文件路径
sheetNanme,子sheet名字
caseName,用例编号，判断sheet中是否存入其他模块的用例，
*args 为方便用例运行时取值的列，不定列
'''

def get_excel_data(sheetNanme,caseName,*args,runCase=['all'],excelDir=None):

    excelDir = os.path.join(testdata_path,'test_devolop.xls')

    ## 定义list，存放传入的参数和预期结果
    resList = []
    ##打开一个文件
    workbook = xlrd.open_workbook(excelDir,formatting_info=True)  # formatting_info=True ----> 保持原样式

    ## 获取对应需要操作的子表
    workSheet = workbook.sheet_by_name(sheetNanme)

    ###  取出所有的列名
    colIndexList =[] ## 定义空的list， 存放数据行名称
    for i in args:
        colIndexList.append(workSheet.row_values(0).index(i))
    print(colIndexList)

    ## ----兼容用户输入的用例编号 ---> 全部的编号，001，001--003，
    runlist = [] ## 运行用例列表
    if 'all' in runCase:
        runlist = workSheet.col_values(0)
    else:
        for one in runCase:
            if '-' in one:
                start,end = one.split('-')
                for i in range(int(start),int(end)+1):
                    runlist.append(caseName+f'{i:0>3}')
            else:
                runlist.append(caseName+f'{one:0>3}')

## -----  获取对应的需求数据-------
    rowIndex = 0          ## 定义行的初始值
    for one in workSheet.col_values(0):
        if caseName in one and one in runlist:    ## 判断需要测试的模块是否有其他模块的测试用例，用编号去判断,one in runlist判断用例是否在输入的runcase内
            ## 遍历列编号
            ## 定义list存放 每一次循环的数据
            getColData = []
            for num in colIndexList:
                tmp = workSheet.cell(rowIndex,num).value
                if is_json(tmp):        ##判断是否是json
                    tmp = json.loads(tmp)
                getColData.append(tmp)      ##遍历的列数据存入list
            resList.append(list(getColData))  ## 将数据存入list [(请求1，响应1),(请求2，响应2)]
        rowIndex += 1 # 取完一次+1

    # for i in resList:
    #     print(i)

    return resList


##-----参数传递，Excel的请求参数获取后是json，不能直接使用，需要转换为字典

def is_json(inData):
    try:
        json.loads(inData)
        return True
    except:
        return False


if __name__ == '__main__':
    filepath = os.path.join(testdata_path,'test_devolop.xls')
    get_excel_data(filepath,'登录模块','Login','标题','请求参数','预期结果',runCase=['2','4-6']) ## 传入data地址，sheet名字，测试用例编号, 取得列名

    # get_excel_data(filepath,'登录模块', 'Login', '标题', '请求参数', '预期结果', runCase=['2', '4-6'])  ## 传入data地址，sheet名字，测试用例编号, 取得列名
       ###  filepath 不用传值了，是因为在上面写成缺省值，写死了路径了
