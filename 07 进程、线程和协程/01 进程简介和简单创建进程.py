# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
多任务：
    。聊天
    。写代码
    。听歌

并发、并行：
你吃饭吃到一半，电话来了，你一直吃完后才去接，这就说明你不支持并发，也不支持并行。 --- 串行
你吃饭吃到一半，电话来了，你停了下来，去接了电话，接完后继续吃饭，这说明你支持并发。 --- 并发
你吃饭吃到一半，电话来了，你一边打电话一边吃饭，这说明你支持并行。 --- 并行
并发的关键是你有处理多个任务的能力，不一定要同时，并行的关键是你有同时处理多个任务的能力。

编程处理多任务，如何实现？
多任务操作系统使用某种任务调度策略允许两个或者更多进程并发共享一个处理器时，事实上处理器在某一时刻只会给
一件任务提供服务。因为任务调度机制保证不同任务之间的切换速度十分迅速，因此给人多个任务同时运行的错觉。多
任务系统中，有 3个功能单位：任务、进程和线程。

Python实现多任务：
    进程
    线程
    携程
    进程 > 线程 > 协程

同步：sychronization
异步：asynchronous
'''

from multiprocessing import Process
import time

def program():
    for i in range(1, 6):
        print('正在写代码第{}行···'.format(i))
        time.sleep(0.5)  # 0.5s

def listen_music():
    musics = ['逆战', '凉凉', '撸起袖子加油干']
    for i in musics:
        print('正在听: {}'.format(i))
        time.sleep(0.5)  # 0.5s

def weichat(user):
    name = '詹姆斯'
    for i in  range(1, 6):
        print('{}正在跟{}聊天, 第{}句'.format(user, name, i))
        time.sleep(0.5)  # 0.5s

if __name__ == '__main__':
    p1 = Process(target=program)
    p2 = Process(target=listen_music)
    p3 = Process(target=weichat, args=('王宁',))

    # 思考1：已经创建了两个进程对象，怎么才能够让他们并发呢？
    p1.start()
    p2.start()
    p3.start()

    # 思考2：直接调用两个进程，结果还是串行的，为什么呢？ 因为你的处理器太快了！因此可以在程序里面加个延迟

    # 思考3：如果还想听歌呢？ 参数怎么传过去呢？ 不传参数会报错，但是其他两个进程依然能够正常运行。

    # 思考4：如何给weichat传参呢？  使用args

    # 思考5：这三个程序是并行呢，还是并发呢？  尽管共用一个控制台，但对于进程而言三个进程是并行的！