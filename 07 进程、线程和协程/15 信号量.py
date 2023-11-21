# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
线程的信号量
    。在 Python的内部有个计数器 counter

信号量的实现方式：
    在内部有一个 counter计数器，每当我们 s.acquire()一次，计数器就进行减 1处理。每当我们 s.release()一次，
计数器就进行加 1处理，当计数器为 0的时候，其他线程就处于等待状态，counter的值就是同一时间可以开启线程的个数。

建议使用 with
    。with s:
        。包含了 s.acquire() 和 s.release()  --- 推荐使用该写法
'''
from threading import Thread, current_thread, Semaphore  # 信号量
# from multiprocessing import Semaphore, Process
import time

# def task(s):
#     s.acquire()  # counter 减 1
#     for i in range(5):
#         print('{}扫地中···{}'.format(current_thread().name, i))
#         time.sleep(1)
#     s.release()  # counter 加 1
#
# if __name__ == '__main__':
#     # 创建信号量
#     s = Semaphore(4)
#
#     for i in range(10):
#         t = Thread(target=task, args=(s,))
#         t.start()

# with 怎么用呢？

def task(s):
    # s.acquire()  # counter 减 1
    with s:  # 包含了acquire() 和 release()  --- 推荐使用该写法
        for i in range(5):
            print('{}扫地中···{}'.format(current_thread().name, i))
            time.sleep(1)
    # s.release()  # counter 加 1

if __name__ == '__main__':
    # 创建信号量
    s = Semaphore(4)

    for i in range(10):
        t = Thread(target=task, args=(s,))
        t.start()