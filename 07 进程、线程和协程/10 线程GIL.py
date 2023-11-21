# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
Python如何创建一个线程
    。方法一：t1 = Thread(target=task1)
    。方法二：自定义线程

    run()
    start()
    join()
    name: 默认的名字 -- Thread-n，如：Thread-1, Thread-2··· 当然也可以设置名字，通过 name参数
    current_thread().name  获取当前线程的名字
    is_alive()

    # 思考3：如果是自定义线程呢？  通过__init__方法！

共享数据
    。如果有全局变量，则每个进程都是共享的

GIL

'''

# import os
# import time
# from threading import Thread, current_thread
# from multiprocessing import Process

# def task1():
#     # 思考2：怎么在函数里面获取线程的名字？  通过current_thread().name
#     for i in range(5):
#         print('{}洗衣服'.format(current_thread().name), i, os.getpid(), os.getppid())
#         time.sleep(0.5)
#
# def task2(n):
#     for i in range(n):
#         print('{}劳动最光荣！'.format(current_thread().name), i, os.getpid(), os.getppid())
#         time.sleep(0.5)
#
# # 思考1：如果完成这两个任务，通过两个进程来完成的话，有点太浪费了，有没有更高效的方法呢？
#
# if __name__ == '__main__':  # 只要一运行，就会出现主线程，所有的动作都是在主线程中完成。
#     print('mian:', os.getpid())
#     # 创建线程对象
#     t1 = Thread(target=task1, name='警察')
#     t2 = Thread(target=task2, args=(6,), name='小偷')
#
#     # 启动线程
#     t1.start()
#     t2.start()
#
#     # 阻塞主线程
#     t1.join()
#     t2.join()
#
#     # 运行在主进程的主线程中
#     for i in range(3):  # 前两个任务未完成，是不会执行主线程的，因为主线程被阻塞了
#         print('t1:', t1.is_alive())  # False
#         print('t2:', t2.is_alive())  # False
#         print('main:', i)
#         time.sleep(0.5)  # 交锁


# 共享线程

import os
import time
from threading import Thread, current_thread
from multiprocessing import Process

# 全局变量
ticket = 10

def sale_ticket():
    global ticket

    while True:
        if ticket > 0:
            print('{}正在卖第{}张火车票！'.format(current_thread().name, ticket), os.getpid())
            ticket -= 1  # 票数减1
            time.sleep(0.1)  # 延迟 -- 交锁
        else:
            break

if __name__ == '__main__':
    # 创建进程
    t1 = Thread(target=sale_ticket, name='1号窗口')
    t2 = Thread(target=sale_ticket, name='2号窗口')
    t3 = Thread(target=sale_ticket, name='3号窗口')

    # 启动进程
    t1.start()
    t2.start()
    t3.start()

    # 思考1：为何终端窗口，偶尔会有重复购票的情况呢？


