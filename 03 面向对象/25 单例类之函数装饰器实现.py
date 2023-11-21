# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
单例类之函数装饰器装饰类实现
'''
# 函数装饰器装饰类
def decorator(clss):
    # 单例
    _instance = {}

    def wrapper(*args, **kwargs):
        # 判断类是否在字典里面
        if clss not in _instance:
            _instance[clss] = clss()

        # print('--->55_instance[clss]', _instance[clss])  # 测试
        # 返回对象的地址
        return _instance[clss]

    # print('--->wrapper', wrapper)  # 测试
    # 返回对象的地址
    return wrapper

# 单例
@decorator
class Singleton:  # Singleton 就是装饰过的对象
    def __init__(self):
        print('-----> Singleton init')

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True

'''
执行过程: (个人总结)
    。顺序执行装饰器函数中的语句[不是加载哦]
    。加载被修饰类
    。将wrapper的值给s1
    。顺序执行函数装饰器内侧函数wrapper

'''