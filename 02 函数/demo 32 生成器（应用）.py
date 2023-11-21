# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
推导式：
    。列表推导式
    。集合推导式
    。字典推导式

    注：无元组推导式

生成器：
    。推导式
    。函数 yield

generator
    。g.next()
    。g.send(value)

next(g)

迭代器，生成器，可迭代的

next(g生成器对象, default)

函数 + yield：
    。注意：
        。定义函数 + 添加关键字：yield
        。调用函数得到的是一个生成器对象
            g = func()  --> g 就是生成器对象
        。结合 next(g)
            。只要遇到 yield，则会将其后面的值返回，并且暂停
            。下一次再调用 next(g) ---> 从暂停位置执行
        。如果函数有返回值，返回值的内容会作为[生成器里面的元素取完之后的]报错信息：StopIteration(返回值内容)

生成器总结：
    。产生方式
    。next(g) <==> g.__next__()    g.send(value)
    。应用：
        。协程
        。进程
        。线程

生成器应用：
    。多任务切换
'''
# 通过函数输入斐波那契数列: 1, 1, 2, 3, 5, 8, 13, 21
def func1(n):
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a + b

    # return 'over'

g = func1(7)

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

print('=' * 50)

'''
生成器应用：
    。多任务切换
'''

def study():
    for i in range(5):
        print('---学习中---', i)
        yield

def listen_music():
    for i in range(5):
        print('---听歌中---', i)
        yield

def weichat():
    for i in range(5):
        print('---聊天中---', i)
        yield

# 思考：怎么听歌，学习，聊天交替呢？  可以加 yield (暂停)

g1 = study()

g2 = listen_music()

g3 = weichat()

while True:
    try:
        g1.__next__()
        g2.__next__()
        g3.__next__()
    except:
        pass