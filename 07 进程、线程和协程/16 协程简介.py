# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
进程： Process
线程： Thread
协程： Coroutine -- 微线程
    。协程是在线程里出现的
'''
# 如果没有加线程，默认在主线程之中完成。

def eat():
    for i in range(5):
        print('坤坤喜欢吃肉饼···', i)
        yield  # yield后面什么都不跟，默认返回空值

def listen_music():
    for i in range(5):
        print('坤坤喜欢听《麻婆豆腐》···', i)
        yield

if __name__ == '__main__':
    g1 = eat()  # g1 生成器对象
    g2 = listen_music()  # g2 生成器对象

    while True:
        try:
            next(g1)
            next(g2)
        except StopIteration:
            break

    # 以上操作，便在一个线程中做到了两个任务之间的切换了。
    # 思考1：以上两个操作，并没有出现耗时操作（下载、保存文件），能不能让一个任务出现阻塞的时候，另一个赶紧补上呢？从而让该线程不停呢？
    # 思考2：假如该线程中有一个任务出现堵塞，那么整个线程便出现堵塞，即便有其他任务，也不会执行，有没有改进的方法呢？
    # 思考3：可以加个判断，但是比较麻烦，有没有更好的解决方案呢？ 有！


