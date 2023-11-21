# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
functools模块：  ---> 函数的工具模块
    。reduce()
    。partial()
    。偏函数(Partial function)是通过一个函数的部分参数预先绑定为某些值，从而得到一个新的具有
      较少可变参数的函数。
    。wraps()
        。python装饰器(decorator)在实现的时候，被装饰后的函数其实已经是另外一个函数了(函数名等函数属性发生了改变)
         为了不影响，python的functools包中提供了一个叫 wraps的 decorator来消除这样的副作用
        。wraps()消除装饰器带来的一些副作用
            。获取对象名：
                。house.__name__  --> 获取函数名
                。house.__doc__   --> 获取文档注释
            。如果不加 @wraps()获取的则是装饰后的名字，出现了不一致的情况！
'''
from functools import wraps
# 定义装饰器函数
def decorator(func):  # func = house
    @wraps(func)  # 仍然可以用装饰器，但是消除了装饰器所带来的的副作用！比如，在拿它的名字和文档出现的不一致性！
    def wrapper(*args, **kwargs):
        '''
        我是一个内部函数 wrapper
        :param args:
        :param kwargs:
        :return: wrapper
        '''
        func()  # 此时的func就是 house()
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('可以住了···')

    return wrapper

@decorator
def house():
    '''
    原始函数house
    :return: None
    '''
    print('空的毛坯房···')

house()  # 仍然可以用装饰器，但是消除了装饰器所带来的的副作用！比如，在拿它的名字和文档出现的不一致性！

# print(house.__name__)  # 显示 house,不加 @wraps(func)则显示的是 wrapper
print(house.__doc__)  # document 文档注释 --> 该处显示的是 wrapper的文档注释