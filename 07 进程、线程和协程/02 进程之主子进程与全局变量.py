# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
Process类
    。创建进程
        p = Process(target=callable, name='', args=tuple,kwargs={})
    。启动进程
        p.start()
    。获取当前进程号
        os.getid()  # 获取当前进程号
        os.getpid()  # 获取主进程号

    。主子进程：
        。程序一启动的时候就会有一个主进程，而在主进程里面，可以开启子进程。
        。主进程
            。执行的时候，默认的进程称为主进程
        。子进程
            。在主进程中可以开启子进程
                p1 = Process(target=callable, args=tuple)

    。全局变量
        。如果是全局变量，则每个进程都会拥有一份，各自操作各自的全局变量，互不影响！

    。阻塞主进程
        。子进程.join()
        。阻塞主进程后面的代码

'''
from multiprocessing import Process
import time
import os

# 用于测试
print('--->top', os.getpid())
# number = 100

def task1():
    global number
    number -= 10  # 加载的是全局变量中的number 100 该资源不同于全局变量和task2中的number
    print('task1--->number', number)
    for i in range(5):
        print('洗衣服', i, os.getpid(), os.getppid())
        time.sleep(0.5)

# 测试2：
number = 100

def task2(n):
    for i in range(n):
        print('劳动最光荣！', i, os.getpid(), os.getppid())
        time.sleep(0.5)
    global number
    number -= 8  # 加载的是全局变量中的number 100  该资源不同于全局变量和task1中的number
    print('task2--->number', number)

if __name__ == '__main__':
    print('main--->start', os.getpid())
    # 创建进程
    p1 = Process(target=task1)
    p2 = Process(target=task2, args=(5,))

    # 启动进程  -- 注意：只要启动进程，全局变量就会再加载一遍！
    p1.start()
    p2.start()

    # 思考3：如何先让子进程执行呢？ 可以使用 join()

    # 阻塞主进程后面的代码执行
    p1.join()
    p2.join()

    print('main--->end', os.getpid())
    # 思考2：如果子进程都执行完了，main中的number是多少，会不会受到子进程的影响？
    print('main--->number', number)

    # 思考1：为什么每次执行都是 main的进程号先出来呢？

    # 思考4：如果改变number的位置，比如：将number放在task1和task2之间，会不会影响number的值呢？ 不会！