# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
Python 如何创建一个线程？
    。方法一：自定义线程
        。定义一个类，继承Thread
        。重写：__init__[可选]
        。重写：run()[必写]
        。启动线程
    。方法二：t1 = Thread(target=task1)
'''
# from threading import Thread
# import os
# import time

# def task1():
#
#     for i in range(5):
#         print('洗衣服', i, os.getpid(), os.getppid())
#         time.sleep(0.5)
#
# def task2(n):
#     for i in range(n):
#         print('劳动最光荣！', i, os.getpid(), os.getppid())
#         time.sleep(0.5)
#
# # 思考：如果完成这两个任务，通过两个进程来完成的话，有点太浪费了，有没有更高效的方法呢？
#
# if __name__ == '__main__':  # 只要一运行，就会出现主线程，所有的动作都是在主线程中完成。
#     print('mian:', os.getpid())
#     # 创建线程对象
#     t1 = Thread(target=task1)
#     t2 = Thread(target=task2, args=(6,))
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
#         time.sleep(0.5)

# 自定义线程
from threading import Thread
import os
import time

class MyThread(Thread):
    # 思考：如何在自定义线程中获取线程的名字？
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(5):
            print('{}正在打印:{}'.format(self.name, i))
            time.sleep(0.1)

if __name__ == '__main__':
    # 创建线程
    t1 = MyThread(name='小明')
    t2 = MyThread(name='小花')
    t3 = MyThread(name='二狗')

    # 启动线程
    t1.start()
    t2.start()
    t3.start()

    # 注意：调度是由操作系统完成的，是随机调度的。
