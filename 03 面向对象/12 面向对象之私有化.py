# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
私有化:
    。只能在类自身中进行调用，对象在外部无法通过.对其进行访问
    。实现属性或者方法的私有化要通过：__属性名, __方法名()
    。在Java里面加上private, 在python里面是__
        。思考：是真的私有化了么？  不是，底层偷偷改名了
        。python中的私有化，底层对私有属性和私有方法进行了改名操作：_类名__属性名, _类名__属性名
'''

class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 20  # 私有属性

    def show_age(self):
        print('我的年龄是：', self.__age)

    def __test(self):
        print('我是测试私有的test方法')

p = Person('zhangsan')
print(p.name)  # zhangsan

# print(p._Person__age)  # 20         找到改名后的属性名，还是可以访问私有属性的

# print(p.__age)  # AttributeError: 'Person' object has no attribute '__age'
#
# p.__test()  # AttributeError: 'Person' object has no attribute '__test'


# print(p.__age)  # AttributeError: 'Person' object has no attribute '__age'
p.show_age()

# p._Person__test()  # 我是测试私有的test方法  找到改名后的方法名，还是可以访问私有方法的