# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
闭包 --- 一个函数包含另一个函数，内部函数引用了外部函数，返回值是内部函数名

装饰器：
    。闭包 + 外层函数参数是函数对象  --> 装饰器
'''
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         print('涂点粉···')
#         print('涂点口红···')
#         print('变成小萝莉···')
#     return wrapper
#
# # 函数装饰器
# @decorator
# def girl():
#     print('俺是大妈···')
#
# girl()

# 类装饰器
# class decorator:  # 类名有的是首字母小写, 我们为了保持一致也将装饰器小写
#     def __init__(self, func):
#         self.func = func
#
#     # 魔术方法 __call
#     def __call__(self, *args, **kwargs):
#         self.func(*args, **kwargs)
#         print('涂点粉···')
#         print('涂点口红···')
#         print('变成小萝莉···')
#
# @decorator  # step1: 创建对象 d = decorator(girl)  step2: 赋值 girl = d [girl 是个对象]
# def girl():
#     print('俺是大妈···')
#
# 对象怎么能直接调用呢？  需要借助魔术方法 __call__
# girl()  # girl 在调用的时候执行的就是 __call__



# 思考：如果 decorator 有参数怎么办呢？

# 类装饰器
class decorator:  # 类名有的是首字母小写, 我们为了保持一致也将装饰器小写
    # 接收装饰器参数
    def __init__(self, args):
        self.args = args  # 装饰器参数，是可以在内部使用的
        # print(self.args)

    # 魔术方法 __call
    def __call__(self, *args, **kwargs):  # *args 是接收的函数对象
        # 定义内部类
        class inner_class:  # 写成函数也是可以的
            def __init__(self, func):
                # 接收函数参数
                self.func = func

            # 定义内层函数[wrapper]
            def __call__(self, *args, **kwargs):
                self.func(*args, **kwargs)
                print('涂点粉···')
                print('涂点口红···')
                print('变成小萝莉···')

        # __call__的返回值会给 girl
        return inner_class(*args)   # 内部类对象 *args就是刚接收的函数对象


@decorator(10)  # step1: 创建对象 d = decorator(10)  step2: 赋值 girl = d [girl 是个对象]
def girl():
    print('俺是大妈···')

girl()  # girl 在调用的时候执行的就是 __call__
# print(girl)  # <__main__.decorator.__call__.<locals>.inner_class object at 0x0000027B60A98D88>

'''
执行步骤：(个人总结)
1. 装饰器部分  ----  从 @decorator 处执行        
    。step1: 创建一个 decorator 对象 d    
    。step2: 接收装饰器的参数  
    。step3: 将被修饰的函数，指向刚刚创建的对象 d  
     
2. 调用girl()  # 由 __call__实现
    。step1: 接收函数名
    。step2: 调用原函数
    。step3: 执行装饰部分

'''