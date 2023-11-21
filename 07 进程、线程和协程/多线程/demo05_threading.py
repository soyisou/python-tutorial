import threading
import time

'''
小结：
1. 想要执行一个单独的任务，那么就需要创建一个新的线程。
2. 在python中使用threading模块中的Thread类，就可以创建一个对象。这个对象标记着一个线程，创建出来的线程默认是不会被执行的。
3.调用这个线程对象的start方法，就可以让这个新的线程开始执行代码。至于这个线程去执行哪里的代码，要看再用Tread创建对象的时候，给target参数传递的是哪个
函数的引用，即将来线程就会执行target参数指定的那个函数。
4.如果想要在一个程序中有多个任务一起运行，那么就想办法创建多个Thread对象即可。
'''


def task_1():
    while True:
        print(11111111)
        time.sleep(1)


def task_2():
    while True:
        print(3333333)
        time.sleep(0.2)


# 使用threading模块中的Thread创建一个对象
t1 = threading.Thread(target=task_1)
t2 = threading.Thread(target=task_2)

# 调用这个实例对象的start方法让这个线程开始执行
t1.start()
t2.start()

while True:
    print(22222222)
    time.sleep(1)
