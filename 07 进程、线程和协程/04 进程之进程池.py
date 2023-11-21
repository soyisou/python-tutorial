# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
进程池 Pool
    。思考：如果需要的进程数量比较多怎么办，比如，100个，都手动创建？   no 用进程池！
    。阻塞式  --- 一次性将多个任务都添加到进来，底层通过队列实现
    。非阻塞式  --- 进程池中完成一个任务之后，才能完成下一个任务！[有点类型串行的感觉]

    注：进程池有两种添加方式，一种是阻塞式，一种是非阻塞式
'''

# apply_async()

# from multiprocessing import Pool
# import os
# import time
#
# def task1():
#     print('洗衣服', os.getpid(), os.getppid())
#     time.sleep(0.5)
#     return '我是进程:' + str(os.getpid())
#     # return 可以返回处理后得到的数据，如：   --- 由进程干的
#     # response = requests.get()
#     # return response.content
#
# # 回调函数  --- 先做任务，完成任务，返回结果。相当于干完活后，报告一声干完活了！callback是由主进程干的！
# def callback(msg):  # msg就是task1扔回来的返回值！
#     print('{}，洗衣服任务完成！'.format(msg))  # 思考：msg哪来的？
#     # callback可以各子进程返回的数据下载到本地等，如：将子进程下载的图片保存到本地
#
# if __name__ == '__main__':
#     # 进程池
#     pool = Pool(4)  # 初始化进程数为4，表示最多容纳4个进程
#     # 非阻塞式    --- 为什么叫做非阻塞式的呢？ 有多少任务，进程池就接收多少任务，底层通过队列来保存每一个任务
#     for i in range(10):
#         pool.apply_async(task1, callback=callback)  # 往进程池放任务,没有该任务则创建
#         # 思考：当放完4个进程，即进程池满了后会怎样？   其他进程先等待，直到四个进程有执行完毕的，才进入！
#
#     # 注意：进程池的存活时间是依赖主进程的！主进程over，则进程池也就over了，因此需要阻塞主进程
#
#     # 此处不表示释放资源，而表示添加任务结束，即进程池关闭！
#     pool.close()
#     # 阻塞主进程
#     pool.join()
#
#     print('main over!')




# apply()

from multiprocessing import Pool
import os
import time

def task1():  # 一个一个出来
    for i in range(5):
        print('洗衣服', i, os.getpid(), os.getppid())
        time.sleep(0.5)

if __name__ == '__main__':
    # 进程池
    pool = Pool(4)  # 初始化进程数为4，表示最多容纳4个进程
    # 阻塞式  -- 为何称为阻塞式？ 加入一个任务进入进程池，若无则新建，该任务未做完，其他任务不能进来！即：
    for i in range(10):  # 虽然是进程池，但当前任务没干完，其他任务依然进不来！[有点类似于串行个感觉]
        # 10个任务   # 阻塞式： 进程池一个任务完成之后，才能做下一个任务！
        pool.apply(task1)  # 没有回调函数
        # 测试
        print('--------------->', i)
        # 思考：当放完4个进程，即进程池满了后会怎样？   其他进程先等待，直到四个进程有执行完毕的，才进入！

    # 注意：进程池的存活时间是依赖主进程的！主进程over，则进程池也就over了，因此需要阻塞主进程

    # 此处不表示释放资源，而表示添加任务结束，即进程池关闭！
    pool.close()
    # 阻塞主进程
    pool.join()

    print('main over!')