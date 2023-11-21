# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''

'''

import os
import time
from threading import Thread, current_thread
from multiprocessing import Process

number = 0

def task():
    global number
    for i in range(1000000):
        number += 1

if __name__ == '__main__':
    # 创建进程
    t1 = Thread(target=task, name='1号窗口')
    t2 = Thread(target=task, name='2号窗口')
    t3 = Thread(target=task, name='3号窗口')

    # 启动进程
    t1.start()
    t2.start()
    t3.start()

    # 阻塞主线程
    t1.join()
    t2.join()
    t3.join()

    print('number:', number)  # number: 300

    # 思考：为什么计算数小的时候，结果是我们需要的数，但是当数字比较大的时候，结果就可能不是我们需要的数了呢？
    '''
    Python的GIL锁跟运算量和阻塞时间有关
    python线程只要拿到cpu执行权，就默默地为cpu资源上一把锁[全局共享锁]，其他线程都进不去了，只能等待着。
    只有阻塞的时候，才会往外交锁！
    '''