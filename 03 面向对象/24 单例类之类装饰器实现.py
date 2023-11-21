# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
装饰器实现单例
'''

# 类装饰器 --- [也可以用函数装饰器装饰类]
class cls_decorator:  # 在此处用类装饰器装饰类[之前咱是用类装饰器装饰函数]
    def __init__(self, clss):  # clss = 'Singleton'
        # 类名
        self.clss = clss  # clss = 'Singleton'
        # 单例，保证共用一个对象
        self.__instance = {}  # self.__instance中存放的是对象[self.clss]和对应对象[self.clss]的地址

    # 执行对象() 时触发
    def __call__(self, *args, **kwargs):
        # 判断类是否在字典里面
        if self.clss not in self.__instance:
            self.__instance[self.clss] = self.clss()  # self.clss()[Singleton()] 创建了一个对象

        # 返回值是个地址[函数装饰器返回的函数名，本质也是一个地址]
        return self.__instance[self.clss]  # {'Singleton': <Singleton object at 0x000002F566672788>}

# @+名字，会自动执行一些动作的话，我们有时候会将其成为’语法糖‘
@cls_decorator  # step1: cls = cls_decorator()   step2: Singleton = cls
class Singleton:  # Singleton 就是装饰过的对象
    def __init__(self):
        print('-----> Singleton init')

s1 = Singleton()  # cls  --- cls()默认调用__call__
# print(s1)  # <__main__.Singleton object at 0x000002F566672788>
s2 = Singleton()
# print(s2)  # <__main__.Singleton object at 0x000002F566672788>
print(s1 is s2)

'''
具体步骤：(个人总结)
    。因为别装饰和装饰器均是类，所以先加载所有的类
    。具体来说：先加载类装饰器，然后加载被装饰的类
    。执行类装饰器中的__init__方法
    。执行调用类的语句，执行__call__方法
'''