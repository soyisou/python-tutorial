# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
装饰器：
    。装饰器可能会同时装饰多个函数，因此为了增加装饰器的通用性(可以装饰多个类型的函数)，可以将参数
     变为可变参数，即给不给参数均可
    。对于关键字参数，*args不会接收关键字参数，但可以使用 **args来接收
    注：python装饰器(decorator)在实现的时候，被装饰后的函数其实已经是另外一个函数了(函数名等函数属性发生了改变)
'''
# def decorator(func):
#     count = 0
#     def wrapper():
#         nonlocal count  # nonlocal: 非本地的，非局部的
#         # 先调用show函数  func = show
#         func()
#         count += 1
#         print('第{}次调用{}函数'.format(count, func.__name__))
#
#     return wrapper
#
# @decorator
# def show():
#     print('正在使用show函数···')
#
# for i in range(3):
#     show()
#
# print(show.__name__)

# 完美模板
def decorator(func):  # 要装饰谁，func就是谁
    # 到底需不需要参数？有点蒙圈了···为了能够做到可变性，因此需要改为可变参数，给不给均可~
    def wrapper(*args, **kwargs):  # args--->(), (6,)
        # 先调用show函数  func = show
        func(*args, **kwargs)  # 相当于对 show，test本身的调用 --> 在调用的时候加*，相当于拆包
        print('调用{}函数'.format(func.__name__))

    return wrapper

@decorator
def show():  # 不需要参数
    print('正在使用show函数···')

@decorator
def test(n):  # 需要参数
    print('------>调用test函数:', n)

@decorator
def test1(a, b=8):
    print('------>调用test函数:', a, b)

# show()
test(2)
# test1(a=5, b=3)

