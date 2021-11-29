# -*- coding:utf-8 -*-
# @Time : 2021/11/14 15:32
# Auther : shenyuming
# @File : baseApi.py
# @Software : PyCharm
import traceback

import requests,os
from utils.handle_yml import get_yaml_data
from utils.handle_path import config_path
import inspect
from configs.config import HOST
from utils.handle_loguru import log

class BaseAPI:
    ##每个继承基类的子类都调用初始化方法，初始化方法将数据配置文件读取

    def __init__(self,inToken=None):
        if inToken:
            self.header = {'Authorization':inToken}
        else:
            self.header = None
            '''
                除了登录外其他接口都需要token，所以在初始化方法中判断，登录不需要借口token=none， 其他接口需要token，
            '''

        ## 获得数据后取 调用基类的子类的类名字，因为yaml文件每个模块数据是按类名字写入的字典格式数据，
        ## 用类名当键，字典中用键的名字可以取到对应的数据
        conpath = os.path.join(config_path,'apiConfig.yml')   #'../configs/apiConfig.yml'
        self.data = get_yaml_data(conpath)[self.__class__.__name__]


    ## 封装请求，post，get等四种请求类型都在requests.request中，因为四类请求方式最后都是返回的request所以直接用rewuest

    def request_send(self,data=None,json=None,params=None,file=None,id=''):
        ## 初始化方法中获得的 self.data 是整个模块的数据，例如整个登录的模块的
        ## 登录中有多个小模块方法， 每个方法只取自己需要的值，
        try:
            methodName = inspect.stack()[1][3]   ## inspect.stack()[1][3] 固定写法，意思是谁调用当前函数，就返回会谁的函数名

            # print(self.data[methodName])
            # print(type(self.data[methodName]))
            ## 将数据剥离 , 获取的类作为键， 只取键对应的值
            path,method = self.data[methodName].values()
            resp = requests.request(method=method,url=f'{HOST}{path}'+str(id),data=data,json=json,params=params,files=file,headers=self.header)
            # print("响应体的编码：--->",resp.encoding)
            # resp.encoding = 'gbk'  ## 修改响应体的编码
            return resp.json()
        except Exception as E:
            print('错误信息--->',E)
            #日志
            log.error(traceback.format_exc())
            raise E

    ## 新增接口
    def add(self):
        pass

    ## 删除接口
    def delete(self):
        pass

    ## 更新接口
    def update(self,inDate):
        return self.request_send(data=inDate)

    ##查询接口
    def query(self,inData):
       return self.request_send(params=inData)



 # 文件上传数据格式固定写法，userfile = {'变量名':(文件名,文件对象(打开文件后的对象),文件类型)}
    #如果上传多个图片，用多个键值对
    #如果多个文件在一个变量，值里面是元组套元组

    ### 文件上传
    def file_upload(self,fileDir):
        fileName = fileDir.split('/')[-1]
        fileType = fileDir.split('.')[-1]
        userFile = {'file':(fileName,open(fileDir,mode='rb'),fileType)}
        return self.request_send(file=userFile)

'''
断言
'''
class ApiAssert:
    @classmethod
    def define_api_assert(self,result,condition,exp_result):
        try:
            if condition == '=':
                assert result == exp_result
            elif condition == 'in':
                assert result in exp_result
        except Exception as error:
            # 日志
            log.error(traceback.format_exc())
            raise error

