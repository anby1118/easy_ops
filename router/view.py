"""
-*- coding: utf-8 -*-
@Time    : 2020-07-11 15:46
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : view.py
"""
from flask import Blueprint, render_template
from models.school import Student
from models.base import db
from serializer.school import students_schema, student_schema

view_bp = Blueprint('view', __name__, url_prefix='/view/')

# 注册路由/index
# pp.route(路由规则)
# 路由规则支持正则
# 路由要写在app.run()之前
@view_bp.route("index", methods=["POST", "GET"])
def index():
    return "this is index."

def home():
    return "this is home."

view_bp.add_url_rule('home',view_func=home)

# /view/student  GET   null     list
view_bp = Blueprint('api', __name__, url_prefix='/api/')
# 查询所有学生信息
@view_bp.route("/students/", methods= ["GET"])
def get_students():
    all_students = Student.query.all()
    # 序列化学生信息
    all_students_ser = students_schema.dump(all_students)
    context = {
        "status": "0000",
        "data": all_students_ser
    }
    return context
# 指定id删除学生信息
@view_bp.route("/student/<id>/", methods= ["DELETE"])
def delete_student(id):
    try:
        student = Student.query.filter_by(stu_id=id).first()
        db.session.delete(student)
        db.session.commit()
        context = {
            "status": "0000",
            "data": str(student),
            "message": "删除成功"
        }
    except:
        context = {
            "status": "0001",
            "data": [],
            "message": "操作出错！"
        }
    return context