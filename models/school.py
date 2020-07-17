"""
-*- coding: utf-8 -*-
@Time    : 2020-07-17 10:19
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : school.py
"""

from sqlalchemy import Column, Integer, String

from .base import db
class Student(db.Model):
    stu_id = Column(Integer, primary_key=True, autoincrement=True)
    stu_name = Column(String(20), nullable=False)
    stu_age = Column(Integer, nullable=False)
