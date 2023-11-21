# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
死锁：
    。两把锁
    。申请锁的顺序不当
开发过程中使用线程，在线程间共享多个资源的时候，

如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
尽管死锁很少发生，但是一旦发生就会造成应用的停止相应，程序不做任何事情！

避免死锁：
1. 重构代码 --- 别让死锁交叉使用
2. 使用 timeout参数，超时自动释放
'''
from threading import Thread, Lock, current_thread
import time

# def task1(lock1, lock2):
#     if lock1.acquire():  # 拿到锁返回True，否则返回False
#         print('{}获取到lock1锁···'.format(current_thread().name))
#         for i in range(5):
#             print('{}--------->{}'.format(current_thread().name, i))
#             time.sleep(0.01)
#         if lock2.acquire():
#             print('{}获取到lock2锁···'.format(current_thread().name))
#             lock2.release()
#         lock1.release()
#
# def task2(lock1, lock2):
#     if lock2.acquire():  # 拿到锁返回True，否则返回False
#         print('{}获取到lock2锁···'.format(current_thread().name))
#         for i in range(5):
#             print('{}---->{}'.format(current_thread().name, i))
#             time.sleep(0.01)
#         if lock1.acquire():
#             print('{}获取到lock1锁···'.format(current_thread().name))
#             lock1.release()
#         lock2.release()
#
# if __name__ == '__main__':
#     # 创建两把锁
#     lock1 = Lock()
#     lock2 = Lock()
#     # 创建线程
#     t1 = Thread(target=task1, args=(lock1, lock2))
#     t2 = Thread(target=task2, args=(lock1, lock2))
#     # 启动线程
#     t1.start()
#     t2.start()
#
#     # 思考：出现了死锁，怎么处理呢？

def task1(lock1, lock2):
    if lock1.acquire():  # 拿到锁返回True，否则返回False
        print('{}获取到lock1锁···'.format(current_thread().name))
        for i in range(5):
            print('{}--------->{}'.format(current_thread().name, i))
            time.sleep(0.01)
        if lock2.acquire(timeout=2):
            print('{}获取到lock2锁···'.format(current_thread().name))
            lock2.release()
        lock1.release()

def task2(lock1, lock2):
    if lock2.acquire():  # 拿到锁返回True，否则返回False
        print('{}获取到lock2锁···'.format(current_thread().name))
        for i in range(5):
            print('{}---->{}'.format(current_thread().name, i))
            time.sleep(0.01)
        if lock1.acquire(timeout=2):
            print('{}获取到lock1锁···'.format(current_thread().name))
            lock1.release()
        lock2.release()

    # 思考：为什么两个都需要加时间？因为不能肯定那个先被执行哦~ 谁先达到阻塞的2s，谁就先释放呗！
    # 思考：目前给两个lock.acquire()加上了时间限制，虽然有一个if语句不会被执行，但至少保证已经有一个能够执行啦！

if __name__ == '__main__':
    # 创建两把锁
    lock1 = Lock()
    lock2 = Lock()
    # 创建线程
    t1 = Thread(target=task1, args=(lock1, lock2))
    t2 = Thread(target=task2, args=(lock1, lock2))
    # 启动线程
    t1.start()
    t2.start()
