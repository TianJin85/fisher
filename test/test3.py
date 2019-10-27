# -*- encoding: utf-8 -*-
from werkzeug.local import LocalStack
"""
@File    : test3.py
@Time    : 2019/10/22 22:22
@Author  : Tianjin
@Email   : tianjincn@163.com
@Softwafre: PyCharm
"""

s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)