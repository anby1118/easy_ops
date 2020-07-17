"""
-*- coding: utf-8 -*-
@Time    : 2020-07-17 15:28
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : api.py
"""

from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse, marshal_with, fields

from models.school import Student
from models.base import db

from serializer.school import students_schema, student_schema

api_bp = Blueprint('api1', __name__, url_prefix='/api1/')
api = Api(api_bp)

# 定义标准化返回的格式
student_result_fields = {
    "status": fields.String,
    "data": fields.Nested({
        'stu_name': fields.String,
        'stu_age': fields.Integer,
        'stu_id': fields.Integer
    }),
    "message": fields.String
}

students_resource_fields ={
"status": fields.String,
    "data": fields.List(fields.Nested({
        'stu_name': fields.String,
        'stu_age': fields.Integer,
        'stu_id': fields.Integer
    })),
    "message": fields.String
}

# 定义视图： 功能view
class StudentListView(Resource):
    def __init__(self):
        # 定义个解析器
        self.parse = reqparse.RequestParser()

        self.parse.add_argument('id', type=int, help='id参数不正确', required=True, trim=True)
        self.parse.add_argument('name', type=str, help='用户名验证错误', required=True, trim=True)
        self.parse.add_argument('age', type=int, help='年龄参数不正确', required=True, trim=True)

    def get(self):
        all_students = Student.query.all()
        # 序列化学生信息
        all_students_ser = students_schema.dump(all_students)
        context = {
            "status": "0000",
            "data": all_students_ser
        }
        return context
    @marshal_with(student_result_fields)
    def post(self):
        args = self.parse.parse_args()

        id = args.get('id')
        name = args.get('name')
        age = args.get('age')

        student = Student(stu_id=id, stu_name=name, stu_age=age)

        db.session.add(student)
        db.session.commit()

        context = {
            "status": "0000",
            "data": student,
            "message": "操作成功！"
        }
        return context

# 注册路由
api.add_resource(StudentListView, '/student/')