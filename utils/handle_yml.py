# -*- coding:utf-8 -*-
# @Time : 2021/11/14 15:52
# Auther : shenyuming
# @File : handle_yml.py
# @Software : PyCharm

import yaml

def get_yaml_data(fileDir):
    #文件在磁盘，需要通过open函数在内存打开
    with open(fileDir,encoding='utf-8') as fo:
        return yaml.safe_load(fo.read())    ##使用yaml加载方法到文件的内容，yaml.safe_load安全加载，是什么数据返回什么数据

## 读取yaml的测试用例
def get_yaml_caseData(fileDir):
    resList = []
    res = get_yaml_data(fileDir)
    for one in res:
        resList.append((one['detail'],one['data'],one['resp']))
    return resList

if __name__ == '__main__':
    #TODO   以后修改成代码获取路径
    # res = get_yaml_data('../configs/apiConfig.yml')
    # res = get_yaml_data('../data/datamodo.yml')
    res = get_yaml_caseData('../data/loginCase.yml')

    print(res)