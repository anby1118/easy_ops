"""
-*- coding: utf-8 -*-
@Time    : 2020-07-11 17:27
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : data.py
"""

from sqlalchemy import Column, Integer, String

from .base import db
class Article(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(128), nullable=True)
    ip = Column(Integer, nullable=True)