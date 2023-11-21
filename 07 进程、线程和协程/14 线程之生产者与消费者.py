# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
线程间通信
    生产者与消费者
        。生产者  线程
        。消费者  线程
'''
from threading import Thread, current_thread
from queue import Queue
import time
import random

def producer(queue):
    print('{}开门啦！'.format(current_thread().name))
    foods = ['红烧狮子头', '香肠烤饭', '蒜蓉生蚝', '酸辣土豆丝', '肉饼']
    for i in range(1, 11):
        food = random.choice(foods)
        print('{}正在制作中···'.format(food))
        time.sleep(1)  # 阻塞
        print('加工完成，可以上菜了！')
        queue.put(food)
    # 说明菜放完了
    queue.put(None)

def consumer(queue):
    print('{}来吃饭了'.format(current_thread().name))
    while True:
        food = queue.get()
        if food:  # 有菜
            print('正在享用美食:{}'.format(food))
            time.sleep(1)  # 阻塞
        else:
            print('{}把饭店吃光了，走人···'.format(current_thread().name))
            break

if __name__ == '__main__':
    # 创建管道
    queue = Queue()
    # 创建线程
    t1 = Thread(target=producer, name='老家肉饼', args=(queue,))
    t2 = Thread(target=consumer, name='赵丽颖', args=(queue,))

    # 启动线程
    t1.start()
    t2.start()