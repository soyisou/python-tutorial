# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
装饰器案例
注：python装饰器(decorator)在实现的时候，被装饰后的函数其实已经是另外一个函数了(函数名等函数属性发生了改变)
'''
# 定义装饰器函数
def decorator(func):  # func = house
    def wrapper():
        func()  # 此时的func就是 house()
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('可以住了···')

    return wrapper

@decorator
def house():
    print('空的毛坯房···')

# print(house)  # <function decorator.<locals>.wrapper at 0x000001D10ED558B8>
house()

# house已经不是house了 ！
# print(house.__name__)  # wrapper

'''
执行步骤: (个人总结)
1. 从 @decorator 处开始执行
    。顺序执行decorator函数内部所有可被执行的语句
    。返回内层函数名
    。将被装饰的函数名指向内层函数名
2. 顺序执行被装饰的函数
    。执行原来的外部函数 [不执行也可]
    。执行新增的装饰内容
'''