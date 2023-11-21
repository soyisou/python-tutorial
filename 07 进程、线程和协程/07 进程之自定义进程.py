# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
自定义进程
    。两个自定义类实现网上图片的下载和本地的保存

进程
    from multiprocessing import Process
    创建进程的方式：
        。方式一：p1 = Process()
        。方式二：自定义进程
            class xxxProcess(Process):
                def __init__(self):
                    Process.__init__(self)
                    ···

                # 重写父类的fun方法
                def run(self):
                    进程的任务

    方法：
        。 run()
        。 start()
        。 join()
        。 close()
        。 terminate()
        。 is_alive()

    全局变量：
        。每个进程中都会存在一份全局变量

    进程池：
        。pool = Pool(max_num)
        。为进程池添加任务：
            。非阻塞式  apply_async()  --> 底层：队列实现，一次性将任务加入队列
            。阻塞式： apply()  --> 一个任务一个任务的执行（类似于串行）

    进程间通信：
        。 queue = Queue(number)
        。默认都是阻塞的：
            。queue.put(timeout=seconds)  # 设置阻塞时间
            。queue.get(timeout=seconds)  # 设置阻塞时间
'''
from multiprocessing import Process, Queue
import requests
import os
import time

#
class DownloadProcess(Process):
    def __init__(self, images, queue):
        Process.__init__(self)
        self.images = images
        self.queue = queue

    # 重写父类的run方法
    def run(self):  # 所有的动作都是放在run里面执行
        # 往队列里放置图片
        for image_url in self.images:
            response = requests.get(image_url)
            image_data = response.content
            self.queue.put(image_data)
            # 测试：
            # self.queue.get()
            # filename = os.path.split(image_url)[1]
            # print('下载{}完毕！'.format(filename))
        # 因为只有一个进程，可以从此处直接关闭即可！可以么？ --- 不行！因为队列中的元素还没有取出来，关闭不了！
        # self.queue.close()  # 当队列中没有元素的时候，即队列为空，才能将队列关闭！

class SaveImageProcess(Process):
    def __init__(self, queue):
        Process.__init__(self)
        self.queue = queue

    # 重写父类的run方法
    def run(self):
        count = 0
        while True:
            try:
                image_data = self.queue.get(timeout=5)
                # 获取文件名
                filename = 'img' + str(count) + '.jpg'
                with open('images/' + filename, 'wb') as ws:
                    ws.write(image_data)
                count += 1
                print('保存{}完毕！'.format(filename))
            except Exception as err:
                print('没有更多数据啦！')
                # 公共队列中，没有元素了，关闭公用队列
                self.queue.close()  # 当队列中没有元素的时候，即队列为空，才能将队列关闭！
                break

if __name__ == '__main__':
    # 图片url
    images = [
        "https://pics6.baidu.com/feed/242dd42a2834349b080b783c023c4ec837d3be52.jpeg?token=47cb46e2132b9b317cdb1a982e6a7577",
        "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg3.doubanio.com%2Fview%2Fphoto%2Fl%2Fpublic%2Fp2542501066.jpg&amp;refer=http%3A%2F%2Fimg3.doubanio.com&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=jpeg?sec=1639994564&amp;t=752a23a6fdea08fb15f6bb0ffcd07f50"
    ]
    # 队列元素个数
    q1 = Queue(2)  # 共用队列
    dlprocess = DownloadProcess(images, q1)
    svprocess = SaveImageProcess(q1)

    # 照样通过start启动自定义进程  --- 我们只是重写了父类Process的run方法
    dlprocess.start()
    svprocess.start()

    for i in range(5):
        if dlprocess.is_alive():
            print('进程是活跃的:', i)
        else:
            print('进程结束了！')
            dlprocess.close()
            break
        time.sleep(0.5)