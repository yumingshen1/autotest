# -*- coding:utf-8 -*-
# @Time : 2021/11/14 20:53
# Auther : shenyuming
# @File : handle_path.py
# @Software : PyCharm

'''
    需求： 代码在任意路经，都可以获取项目的绝对路径

'''
import os

# print(__file__)     ##当前文件所在路径
# print(os.path.dirname(__file__))       ##当前文件所在的目录
# print(os.path.dirname(os.path.dirname(__file__)))   ## 一层层往回找，找到工程路径

## 工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(project_path)

## 配置路径
config_path = os.path.join(project_path,'configs')
# print(config_path)

## 测试数据路径
testdata_path = os.path.join(project_path,'data')
# print(testdata_path)

## 测试报告路径
report_path = os.path.join(project_path,f'outFiles/report/tmp')
# print(report_path)

## 日志路径
log_path = os.path.join(project_path,r'outFile/logs')
# print(log_path)