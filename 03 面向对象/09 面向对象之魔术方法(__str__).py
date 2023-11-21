# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
__str__魔术方法 [使用频率非常高]
    。触发时机：使用print(对象)或者str(对象)的时候触发
    。参数：一个self接收对象
    。返回值：必须是字符串类型
    。作用：print(对象的)进行操作，得到字符串，通常用于快捷操作
    。注意：无

__repr__魔术方法
    。触发时机：在使用repr(对象)的时候触发
    。参数：一个self接收对象
    。返回值：必须是字符串
    。作用：将对象转化repr化为字符串时使用，也可以用于快捷操作

二者：
    。__str__ 和 __repr__ 均可将对象转换为字符串表示形式
    。print(obj) --> 默认触发 __str__
    。repr(obj)  --> 触发 __repr__

# 以下两个方法用的很少
__call__
    。调用类型的魔术方法
    。触发时机：将对象当作函数调用时触发，方式：对象()
    。参数：至少一个self接收对象，其余根据调用时参数决定
    。返回值：根据情况而定
    。作用：可以将复杂的步骤进行合并操作，减少调用的步骤，方便使用
    。注意：无

__len__
    。触发时机：使用len(对象)的时候触发
    。参数：一个参数self
    。返回值：必须是一个整型
    。作用：可以设置为检测对象成员个数，但是也可以进行其他任意操作
    。注意：返回值必须是整数，否则语法报错，另外该要求是格式要求

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 重写的目的：方便在打印对象的时候，打印一些对程序员有用的信息
    def __str__(self):
        return self.name + '\t' + str(self.age)  # 注意：有整型变量拼接的时候，需要先转换为字符串类型

    def __repr__(self):
        return 'hello world!'

    def __call__(self, *args, **kwargs):
        print('我被调用了')

    # 返回对象的长度
    def __len__(self):  # 根据需求来写
        return 5

p = Person('zhangsan', 20)
print(p) # zhangsan	20

p1 = Person('lisi', 16)
print(p1) # lisi	16

# 将对象转换为字符串类型
print(repr(p1))  # hello world!

print('=' * 50)
def func():
    print('func')

# 函数的调用
func() # func

print('=' * 50)

# 当对象要当作函数用的时候，可以使用__call__
p = Person('zhangsan', 20)
p()  # 如果不写__call__, 执行结果：TypeError: 'Person' object is not callable

# 返回对象 p 的长度
print(len(p))  # 5
"""
我被调用了
5
"""