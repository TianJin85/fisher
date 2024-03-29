# -*- encoding: utf-8 -*-
"""
@File    : user.py
@Time    : 2019/10/31 15:55
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from sqlalchemy import Column, Integer, Boolean, Float, String
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.Spider.yushu_book import YuShuBook
from app.libs.helper import is_isbn_or_key
from app.models.base import Base
# from app import login_manager
from app.models.gift import Gift
from app.models.wish import Wish
from flask_login import login_manager


class User(UserMixin, Base):
    # __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(50), unique=True, nullable=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) !='isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn()
        if not yushu_book.first:
            return False

        # 不允许一个用户同时赠送多本相同的图书
        # 一个用户不可能同时成为赠送者和所要者

        # 既不是增送清单，以不在心愿清单才能添加
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False


@login_manager.token_loader
def get_user(uid):
    return User.query.get(int(uid))
