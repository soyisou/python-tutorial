# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
类与对象之间的关系：
    。在现实中：对象1，对象2， 对象3 --》共同的特征、动作 --》提取 --》封装
    。在开发中：类 --》对象（实例化）

先定义一个类，再通过类创建对象: 对象 = 类名()
    。类：模型
    。对象：通过模型构建的具体事务
'''

# 顺序：先加载，后调用
class Student:  # 类
    pass

print(Student)
print('Student:', id(Student))

class Book:
    bname = '盗墓笔记'
    price = 39

print(Book)
print(id(Book))

print(Book.bname)
print(Book.price)

# 对象的创建
# 格式：对象名 = 类名()
s1 = Student()  # s1就是对象
print('s1:', id(s1))

s2 = Student()  # s2就是对象
print('s2:', id(s2))

b1 = Book()  # b1就是对象



