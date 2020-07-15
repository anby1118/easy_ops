"""
-*- coding: utf-8 -*-
@Time    : 2020-07-11 14:58
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : secure.py
"""
import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

PassWord = '123456'

DEBUG = True
ENV = "development"

# 使用sqlite创建数据库
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')