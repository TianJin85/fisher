# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2019/10/31 22:38
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from . import web
from flask import session, make_response

@web.route('/set/cookie')
def set_cookie():
    response = make_response('Hello MR.7')
    response.set_cookie('name', 'MR.7', 100)

    return response


