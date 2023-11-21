# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
默认值参数：
    。在定义函数的时候，对某个参数设置一个固定的值，如下：
    def func(a, b = 10):
        pass
    其中，b = 10 就是默认值

    调用时：
    func(8) ---> a = 8, b = 10 此时使用了默认 b = 10 的值
    func(1, 5)  ---> a = 1, b = 5 替换了原来默认的值

    注意：在定义默认值的时候，必须要放在参数的后面，否则报错

关键字参数
    。在调用的时候，通过关键字的方式明确指明值是给哪一个参数的
    。func(b=7)  --> b=7就是关键字的方式
    。func(b=6, a=3)  顺序乱没有关系，关键之能够给指明给那个参数什么值
'''
def func(a, b = 10):  # 默认值，其定义要后放
    return a + b

print(func(5))  # 15
print(func(2, 5))  # 7

def func(a = 5, b = 10):  # 默认值的定义要后放
    return a + b

print(func(3))  # 15
print(func(2, 5))  # 7
print(func(b=13))  # 18
print(func(b=3, a=9))  # 12

def func1(x, y):
    return x * y

print(func1(y=10, x=12))  # 关键字