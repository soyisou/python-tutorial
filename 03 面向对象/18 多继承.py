# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
多继承：
    。多继承的查找顺序
        。经典类：深度优先                    python2.2版本
        。新式类：C3算法(先深度优先，再广度优先)             python3.7只有新式类，没有经典类

        python 2.3 和 python 2.7 同时存在

    。MRO原则
        。print(类.__mro__)  查看搜索顺序  --- 结果为元组
        。print(类.mro())  查看搜索顺序  --- 结果为列表
'''

class Father1:
    def func(self):
        print('----> father1.func')

class A(Father1):
    def func(self):
        print('----> father1.A.func')

class A1(Father1):
    def func(self):
        print('----> father1.A.func')

class A_son(A):
    def func(self):
        print('----> father1.A.A_son.func')

class Father2:
    def func(self):
        print('----> father2.func')

class B(Father2):
    def func(self):
        print('----> father2.B.func')

class B1(Father2):
    def func(self):
        print('----> father2.B1.func')

class B_son(B):
    def func(self):
        print('----> father2.B.B_son.func')

class Father3:
    def func(self):
        print('----> father3.func')

class C(Father3):
    def func(self):
        print('----> father3.c.func')

class Son(A_son, B_son, C):  # 按括号顺序，从左往右，先深度搜索，再广度搜索
    pass

s = Son()
s.func()
# print(Son.__mro__)  # 方法1 查看搜索顺序 --- 结果为元组
# print(Son.mro())  # 方法2 查看搜索顺序  --- 结果为列表
# s.func()
# s.func()
