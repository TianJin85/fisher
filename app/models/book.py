# -*- encoding: utf-8 -*-
"""
@File    : book.py
@Time    : 2019/10/16 23:12
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from sqlalchemy import Column, String, Integer


from app.models.base import db


class Book(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30),default='未名')
    binding = Column(String(20))
    publisher = Column(String(20))
    pages = Column(String(20))
    pudbate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass