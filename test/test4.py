# -*- encoding: utf-8 -*-
"""
@File    : test4.py
@Time    : 2019/10/27 21:24
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""

class NoneLocal:
    def __int__(self, v):
        self.v = v

n = NoneLocal(1)