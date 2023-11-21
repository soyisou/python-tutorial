# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
进程间的通信
    。进程间相互平行，各自拥有各自的资源
    。在两个进程中间搭建一个队列, 一个往里放，一个往外取
队列：
    。特点：FIFO
    。放置：put()
    。取出：get()
'''
from multiprocessing import Process, Queue

queue = Queue(3)  # 个数
queue.put('馒头1')
queue.put('馒头2')
queue.put('馒头3')
print(queue.full())  # 表示有没有满

# 队列已满，无法放进去！等待，等待队列中的元素被取出，然后再往里面添加！
print(queue.qsize())  # 3
# print(queue.get())  # 取馒头1  --  队列依然是堵着的
# print(queue.get())  # 取馒头2
try:
    queue.put('馒头4', timeout=2)  # 等待3s，如果还放不进去，就不再往里面放了
    queue.put('馒头5', timeout=2)  # 等待3s，如果还放不进去，就不再往里面放了
except:
    print('存放馒头失败！')

while True:  # 馒头1、馒头2、馒头3正常取出！
    try:
        print(queue.get(timeout=1))  # 如果1s后取不出，则不再取，报异常
    except:
        print('队列为空，取不出东西！')
        break

# 注意：只要涉及文件操作，都认为是耗时操作！

# 两个进程之间的通信，下载和保存

def download(url, queue):  # 下载完后，将文件放入队列中
    pass

def save_file(queue):  # 将文件从队列中取出
    pass