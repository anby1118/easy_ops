"""
-*- coding: utf-8 -*-
@Time    : 2020-07-11 15:46
@Author  : Kate
@E-mail  : kate1118@163.com
@Group   : https://www.sanchuangedu.cn/
@File    : view.py
"""
from flask import Blueprint, render_template
from models import data


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
