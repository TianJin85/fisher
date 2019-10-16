# -*- encoding: utf-8 -*-
"""
@File    : book.py
@Time    : 2019/10/16 20:17
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
        q = StringField(DataRequired(), validators=[Length(min=1, max=30)])
        page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)