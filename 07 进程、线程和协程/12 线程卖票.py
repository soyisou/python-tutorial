# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
线程共享数据的不安全性
'''
from threading import Thread, current_thread, Lock
import time

ticket = 10

def sale_ticket(lock):
    global ticket
    while True:
        lock.acquire()  # 加锁   拿到锁和整个卖票的过程一气呵成
        if ticket > 0:
            # lock.acquire()  # 加锁 报错！因为看到有票，我就进入了，但是拿不到锁，因此在等待，不管怎样已经进入if语句了，因此就可能出现负值
            print('{}正在卖第{}张票'.format(current_thread().name, ticket))
            ticket -= 1
            lock.release()  # 解锁
            time.sleep(0.1)  # 睡觉不属于共享的动作！
        else:
            print('票卖光了！')
            lock.release()  # 解锁
            break

    # 思考：锁lock放在哪个位置呢？ 能不能加到while循环外面？肯定不行了，那样的话都是线程1抢到了！


if __name__ == '__main__':
    lock = Lock()
    # 创建线程
    t1 = Thread(target=sale_ticket, name='1号窗口', args=(lock,))
    t2 = Thread(target=sale_ticket, name='2号窗口', args=(lock,))
    t3 = Thread(target=sale_ticket, name='3号窗口', args=(lock,))
    t4 = Thread(target=sale_ticket, name='4号窗口', args=(lock,))

    # 启动线程
    t1.start()
    t2.start()
    t3.start()
    t4.start()

