import time
import threading


def sing():
    for i in range(3):
        print("singing...%d" % i)
        time.sleep(1)


def dance():
    for i in range(3):
        print('dancing...%d' % i)
        time.sleep(1)


if __name__ == '__main__':
    '''
    1.普通调用执行结果：
    singing...0
    singing...1
    singing...2
    dancing...0
    dancing...1
    dancing...2
    '''
    # 1. 普通调用
    # sing()
    # dance()

    # 2. 使用多线程
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    '''
    2. 启用多线程执行结果：
    singing...0
    dancing...0
    singing...1
    dancing...1
    dancing...2
    singing...2
    '''
