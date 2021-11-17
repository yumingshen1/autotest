# -*- coding:utf-8 -*-
# @Time : 2021/11/14 17:38
# Auther : shenyuming
# @File : handle_data.py
# @Software : PyCharm

import hashlib

## md5加密
def MD5_login(str):
    pwd = hashlib.md5()
    pwd.update(str.encode(encoding='utf-8'))
    return pwd.hexdigest()