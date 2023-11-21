# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
next(g生成器对象, default)

函数 + yield：
    。注意：
        。定义函数 + 添加关键字：yield
        。调用函数得到的是一个生成器对象
            g = func()  --> g 就是生成器对象
        。结合 next(g)
            。只要遇到 yield，则会将其后面的值返回，并且暂停
            。下一次再调用 next(g) ---> 从暂停位置执行


函数：
    。__next__(): 同系统函数 next(g)
        。g.__next()  <==> next(g)  --> 以上均可得到下一个元素
    。send():  # 每次调用的时候需要向生成器中传值
        。注意：send(None) 第一次必须传空值，
              send(值)  以后便可以传值了

    斐波那契数列：
        。1, 1, 2, 3, 5, 8, 13, 21

    素数：只能被自身和 1 整除的数
        。1, 2, 3, 5, 7, 11, 13 ···


'''
list2 = [1, 2, 4, 5, 6, 4, 3, 6, 4, 6, 9]
g = (x for x in list2 if x % 2 == 0)
print(next(g))
print(next(g))
print(next(g))

def func():
    sum = 0
    for i in range(5):
        x = yield i  # 作用：1. return i    2. 暂停
        print('----->x:', x)
        sum += (x + i)
        print('----->sum:', sum)

g = func()  # 调用函数
# print(g)  # <generator object func at 0x000002107183CAC8>
print('=' * 50)

# print(next(g))  # next() 系统函数
# print(next(g))
# print(next(g))

# g.close()
# print(next(g))

# g.__next__()  # 同 next(g)
# print(g.__next__())  # 类似于 next(g) g.next() --> g自身带的函数
g.send(None)  # 即便是第一次送值，也是接不到的，因此送一个 None
g.send(8)
g.send(2)
