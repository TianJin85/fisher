# -*- encoding: utf-8 -*-
"""
@File    : gift.py
@Time    : 2019/10/31 15:55
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from app.models.base import db, Base

from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationships


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationships('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)