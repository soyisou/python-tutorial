# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
总结：
    。单继承
        。所有的类默认继承object
        。继承其他父类的方式： class 子类(父类): pass
    。继承了父类的非私有的属性和方法
    。重写：父类的方法不能满足子类的需求，则定义一个跟父类名字相同的方法
           。每次对象调用则优先调用子类的
    。子类方法中调用父类的方法或者属性：
        。方式 1：Father.func(self, 参数)
        。方式 2：supper(Son, self).func(n)

'''

class Father:
    def __init__(self):
        self.__a = 10
        self.b = 8

    def show(self):
        r = self.__a + self.b
        print('运算的结果是：', r)

    def func(self, n):
        print('父类的func方法')

class Son(Father):
    def __init__(self):
        Father.__init__(self)
        self.__a = 100

    def show(self):
        r = self.__a + self.b
        print('运算的结果是：', r)

    # 如果多加了一个参数，则出现了警告
    def func(self, n):  # 尽量名字和格式与父类的一致，严格的重写是：子类的方法格式与父类保持一致
        # 调用父类的方法
        Father.func(self, n)

        # 其他的调用方式，使用supper访问父类的方法
        super(Son, self).func(n)  # func()里面不需要传参了

        print('子类的func方法')

s = Son()
s.show()
s.func(3)