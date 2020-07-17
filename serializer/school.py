"""
-*- coding: utf-8 -*-
@Time    : 2020-07-17 15:01
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : school.py.py
"""

from .base import ma
from models.school import Student

# 定义一个学生的序列化器
class StudentSchema(ma.Schema):
    class Meta:
        model = Student
        # 取模型里的字段
        fields = ('stu_id', 'stu_name', 'stuage')

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)