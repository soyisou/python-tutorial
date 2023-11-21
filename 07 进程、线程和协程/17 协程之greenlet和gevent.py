# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
以上操作，便在一个线程中做到了两个任务之间的切换了。
思考1：以上两个操作，并没有出现耗时操作（下载、保存文件），能不能让一个任务出现阻塞的时候，另一个赶紧补上呢？从而让该线程不停呢？
思考2：假如该线程中有一个任务出现堵塞，那么整个线程便出现堵塞，即便有其他任务，也不会执行，有没有改进的方法呢？
思考3：可以加个判断，但是比较麻烦，有没有更好的解决方案呢？ 有！

greenlet
gevent

二者区别：gevent底层是拿greenlet来做的.
'''
'''
greenlet的使用
'''
# from greenlet import greenlet
#
# def eat():
#     for i in range(5):
#         print('坤坤喜欢吃肉饼···', i)
#         g2.switch()
#
# def listen_music():
#     for i in range(5):
#         print('坤坤喜欢听《麻婆豆腐》···', i)
#         g1.switch()
#
# if __name__ == '__main__':
#     # 创建greenlet对象
#     g1 = greenlet(eat)
#     g2 = greenlet(listen_music)
#
#     # 此处先调用，即为了保证有一个先运行
#     g1.switch()  # 底层使用的是生成器完成动作

    # 思考：在eat()和listen_music()中还需要手动增加switch(),有没有更好的方法，实现自动化呢？

'''
gevent的使用
    。好处：猴子补丁
        。如果没有猴子补丁不会实现自动切换
        。只有有猴子补丁才能实现自动切换
'''
from gevent import monkey
import gevent
import time

# 思考3：使用协程的时候，gevent的猴子补丁是干啥的？  可以认为在所有耗时操作上贴个标签，表示它是耗时操作！不打补丁它是不认识的，只有打了补丁，它才认识。
monkey.patch_all()  # 必须要先打补丁！这样的话，在用gevent去执行的时候就知道哪些是耗时的啦！

def eat():
    for i in range(5):
        print('坤坤喜欢吃肉饼···', i)
        time.sleep(0.1)  # 已经被monkey.patch_all标记为耗时操作了

def listen_music():
    for i in range(5):
        print('坤坤喜欢听《麻婆豆腐》···', i)
        time.sleep(0.1)

if __name__ == '__main__':
    # 创建，并启动greenlet对象
    g1 = gevent.spawn(eat)
    g2 = gevent.spawn(listen_music)

    # 思考1：以上的操作，已经启动了，为何程序没有效果呢？因为必须加上join()! 为什么呢？因为主线程只要结束了
    #       它就跟着over啦！因此，必须要先阻塞主线程！

    # 需要先使用join()，阻塞主线程
    g1.join()
    g2.join()

    print('----over----')

    # 思考2：sleep()是个耗时动作，怎么实现在eat的sleep时，自动切换到listen_music呢？
