# -*- coding:utf-8 -*-
# @Time : 2021/11/14 16:29
# Auther : shenyuming
# @File : shop.py
# @Software : PyCharm

from common.baseApi import BaseAPI
from libs.login import Login
from configs.config import NAME_PSW
from utils.handle_path import testdata_path
import os

class Shop(BaseAPI):
    ## 列出店铺
    ## 跟新店铺

    ## 更新店铺 ， ID需要修改值，字典建去改值； 需要上传图片信息，该图片信息就是上传图片接口的返回值realFileName字段

    def update(self,inDate,shopID,fileInfo):
        if inDate['id'] == 'id不存在':  ## 修改时和用例编写约定一个不存在的ID，在这里进行不存在ID的判断
            inDate['id'] = 000
        else:
            inDate['id'] = shopID

        ## 文件更新
        inDate['image_path'] = fileInfo
        inDate['image'] = f'/file/getImgStream?fileName={fileInfo}'
        return super(Shop,self).update(inDate)
        ## (Shop,self) 表示Shop类的实例，的父类的update方法

if __name__ == '__main__':
    _token = Login().login(NAME_PSW,getToken=True)  ## 调用登录为获取token
    par = {"page": "1", "limit": "10"}
    # 实例商品类，调用基类中的实例方法列出店铺，返回数据，
    shop = Shop(_token)
    res1 = shop.query(par)
    print(res1)
    ## 获取店铺的ID
    shopID = res1['data']['records'][0]['id']
    print(shopID)

    ## 上传文件
    res2 = shop.file_upload(os.path.join(testdata_path,'ss.jpg'))
    print(res2)
    ## 获取文件信息
    fileInfo = res2['data']['realFileName']
    print(fileInfo)

    ## 更新店铺
    ## 先拿个值测试下是否通
    inDate ={
            "name": "新修改的名字",
            "address": "上海市静安区秣陵街道303号路",
            "description": "营养还是蒸的好",
            "id": f"{shopID}",
            "Phone": "13176876632",
            "rating": "6.0",
            "recent_order_num":100,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
        }
    res3 = shop.update(inDate,shopID,fileInfo)
    print(res3)