# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
进程间通信之下载图片

p = Process(target=callable, name='', args=tuple, kwargs=dict)
'''
# 导入Process和Queue
from multiprocessing import Process, Queue
import time
import requests
import os

# 两个进程之间的通信，下载和保存

# 从网上下载图片
def download(images, queue):  # 下载完后，将文件放入队列中
    for image_url in images:
        response = requests.get(image_url)
        image_data = response.content
        queue.put(image_data)

# 将图片保存到本地
def save_file(queue):  # 将文件从队列中取出
    count = 0
    while True:
        try:
            image_data = queue.get(timeout=5)
            # 获取文件名
            filename = 'img' + str(count) + '.jpg'
            with open('images/' + filename, 'wb') as ws:
                ws.write(image_data)
            count += 1
            print('保存{}完毕！'.format(filename))
        except Exception as err:
            print('没有更多数据啦！')
            break

if __name__ == '__main__':
    # 图片url
    images = [
        "https://pics6.baidu.com/feed/242dd42a2834349b080b783c023c4ec837d3be52.jpeg?token=47cb46e2132b9b317cdb1a982e6a7577",
        "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fphoto%2Fl%2Fpublic%2Fp2542501066.jpg&amp;refer=http%3A%2F%2Fimg3.doubanio.com&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=jpeg?sec=1639994564&amp;t=752a23a6fdea08fb15f6bb0ffcd07f50"
        ]
    # 队列元素个数
    q1 = Queue(2)
    # 创建进程
    p1 = Process(target=download, args=(images, q1))
    p2 = Process(target=save_file, args=(q1,))

    # 初始时间
    start = time.time()  # 开始时间戳

    # 启动进程
    p1.start()
    p2.start()

    # 阻塞主进程
    p1.join()
    p2.join()

    # 结束时间
    end = time.time()  # 结束时间戳


    print('用时:{}'.format(end - start - 5))  # 要减去while里面的等待时间5s哦~

# 思考：能够自定义进程？
