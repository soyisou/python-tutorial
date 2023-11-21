# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''

'''

import os
import time
from threading import Thread, current_thread, Lock
from multiprocessing import Process

number = 0

def task(lock):
    global number
    lock.acquire()  # 握住此锁
    for i in range(1000000):
        number += 1
    lock.release()  # 释放此锁

if __name__ == '__main__':
    lock = Lock()  # Lock是个类
    # 创建进程
    t1 = Thread(target=task, name='1号窗口', args=(lock,))
    t2 = Thread(target=task, name='2号窗口', args=(lock,))
    t3 = Thread(target=task, name='3号窗口', args=(lock,))

    # 启动进程
    t1.start()
    t2.start()
    t3.start()

    # 阻塞主线程
    t1.join()
    t2.join()
    t3.join()

    # 加锁的运算时间和不加锁的运算时间肯定不一样，加锁时间要变慢一些哦~
    print('number:', number)  # number: 3000000

    # 思考：为什么计算数小的时候，结果是我们需要的数，但是当数字比较大的时候，结果就可能不是我们需要的数了呢？
    '''
    Python的GIL锁跟运算量和阻塞时间有关
    python线程只要拿到cpu执行权，就默默地为cpu资源上一把锁[全局共享锁]，其他线程都进不去了，只能等待着。
    只有阻塞的时候，才会往外交锁！
    '''