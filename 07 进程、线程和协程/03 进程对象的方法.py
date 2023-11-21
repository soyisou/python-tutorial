# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
p = Process(target=callable)

进程对象可以访问方法
    run()  # run运行任务，但是不是在子进程中，CPU没有单独分配进程资源
    start()  # 启动进程，且系统分配了单独的进程资源
    terminate()  # 终止进程，但资源可能还未释放
    join()  # 阻塞主进程中的代码实现
    close()  # target完成之后，调用 close()关闭系统资源
    is_alive()  # 判断 target任务是否完成，如果任务完成则为 False，没有完成True（可理解为进程是否是活动的）

进程池 Pool
    。思考：如果需要的进程数量比较多怎么办，比如，100个，都手动创建？   no 用进程池！
    。阻塞式
    。非阻塞式
'''
from multiprocessing import Process
import time
import os

def task1():  # 4个4个出来
    for i in range(5):
        print('洗衣服', i, os.getpid(), os.getppid())
        time.sleep(0.5)

def task2(n):
    for i in range(n):
        print('劳动最光荣！', i, os.getpid(), os.getppid())
        time.sleep(0.5)

if __name__ == '__main__':
    p1 = Process(target=task1)
    p2 = Process(target=task2, args=(6,))

    # run运行任务，但是不是在子进程中，CPU没有单独分配进程资源
    # p1.run()  # 仅仅是运行动作，但是没有单独分配进程资源
    # p2.run()

    # start
    p1.start()  # 底层会调用run方法
    p2.start()

    for i in range(10):
        if i == 3:
            p1.terminate()  # 终止进程
        elif i == 4:
            p2.terminate()
            # p2.close()  # 释放资源  放在此位置，报错！  思考1：可以放在哪里呢？
        time.sleep(0.5)
        print('main: ', i)


    print('p1是否活着：', p1.is_alive())
    if p2.close():  # 释放资源，类似于文件操作的close
        print('p2是否活着：', p2.is_alive())
    else:
        print('p2已经彻底关闭了！')
