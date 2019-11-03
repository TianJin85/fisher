# -*- encoding: utf-8 -*-
"""
@File    : gift.py
@Time    : 2019/10/31 15:55
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import current_app

from app.Spider.yushu_book import YuShuBook
from app.models.base import db, Base

from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationships


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationships('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        # 链式调用
        # 主体
        # 子函数
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            Gift.create_datetime).limit(
            current_app.config['RECENT_BOOKCOUNT']).distinct().all()
        return recent_gift