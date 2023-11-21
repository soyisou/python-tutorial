# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
封装，继承，多态
    。属性和方法  ---> 封装到类中
    。属性封装：将属性私有化，定义共有的 set和 get方法
    。私有化作用：
        。隐藏属性，只能在类中使用
        。对私有属性的赋值和取值起到一定的限制作用
        。通过set方法限制赋值，通过get方法限制取值
'''

class Person:
    # 限制作用  ---> 限制了外界动态属性的添加！
    __slots__ = ['__name', '__age', '__flag']  # 加进来的才是能赋值的！如果没有加到里面，外界是不能赋值的！

    def __init__(self, name, age):
        self.__name = name  # 私有化属性
        self.__age = age  # 私有化属性
        self.__flag = True

    def get_name(self):
        # 有需求可以定制内容，添加验证条件，比如：判断用户是否登录等
        if self.__flag == True:
            return self.__name
        else:
            print('没有权限查看该用户名！')

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if len(name) >= 6:
            self.__name = name
            print('名字设置成功！')
        else:
            print('名字必须要大于等于6位！')

    def set_age(self, age):
        if 0 < age < 125:
            self.__age = age
            print('年龄设置成功！')
        else:
            print('年龄设置失败！必须在0 ~ 125之间！')

p = Person('zhangsan', 20)

# print(p.get_name())

# p.name = 'jack'  # 可以正常赋值！加上__slots__后，如果里面没有name，则是不能执行该语句的哦
# print(p.name)  # jack

p.set_name('jack')
p.set_name('zhangsan')
print(p.get_name())
p.set_age(12)
print(p.get_age())