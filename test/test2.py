# -*- encoding: utf-8 -*-
import threading
import time

from werkzeug.local import Local

"""
@File    : test2.py
@Time    : 2019/10/22 22:03
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""

# 原理 字典 保存数据
# 操作数据
# werkzeug local Local 字典

class A:
    b = 1

my_obj = Local()

my_obj.b = 1

def worker():
    # 新线程
    my_obj.b = 2
    print('in new thread b is:' + str(my_obj.b))


new_t = threading.Thread(target=worker,name='qiyue_thread')
new_t.start()
time.sleep(1)

# 主线程
print('in main thread b is' + str(my_obj.b))



