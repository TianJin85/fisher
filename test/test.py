# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2019/10/21 21:45
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import threading
import time


def worker():
    print('i am thread')
    tht = threading.current_thread()
    time.sleep(100)
    print(tht.getName())


new_t = threading.Thread(target=worker)
new_t.start()

t = threading.current_thread()
print(t.getName())


