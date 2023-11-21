# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
元类被称为 Python 中的'深奥的巫术'。尽管你需要用到它的地方极少（除非你基于zope编程），可事实上它的基础理论其实
令人惊讶地易懂。
一切皆对象
一切都有类型
'class' 和 ‘type' 之间本质上并无不同
类也是对象
他们的类型是 type
以前，术语 type用于内置类型，而术语 class用于用户定义的类，但自 Python2.2以来 'class'和 'type'本质上并无不同。
对于旧风格 (old-style)类的类型是 type.ClassTpye
类的类是···
它的元类···
就像对象是类的实例一样，类是它的元类的实例
调用元类可以创建类
确切来说，python中的其他对象也是如此。
因此，当你创建一个类时···
解释器会调用元类来生成它···
定义一个继承自 object 的普通类意味着调用 type 来创建它。
'''
a = 10
print(type(a))  # <class 'int'> in 为系统类型

class Person:
    pass

p = Person()
print(type(p))  # Person 为自定义类型

# 测试类型
print(type(int))  # <class 'type'>
print(type(Person))  # <class 'type'>

# class Student:
#     '''
#     这个是一个学生类
#     '''
#     type1 = '学生'
#     def __init__(self, name):
#         self.name = name
#
# s = Student('zhangsan')
# print(Student.__dict__)

# 所有的类都是有type类创建出来的,type类可以帮我们构建我们想要的类型，底层都是调用元类创建出类的
Student = type('Student', (object, ), {'type1': '学生类'})  # 等同于33行-37行
print(type(Student))
s = Student()
print(s)

print(type(object))

# 思考：我们能不能通过元类来完成一些事情？

# 每次创建对象的时候，便会过ListMetaclass，不会过元类type了
class ListMetaclass(type):  # 不是直接用type，而是用type的子类
    # *args 中存放的是名字、父类和属性
    # def __new__(cls, *args, **kwargs):
    #     print(*args)
    #     print(**kwargs)

    # 也可以拆开查看
    def __new__(cls, name, bases, attrs):
        print(name)
        print(bases)
        print(attrs)
        attrs['b'] = 'world'
        # 底层还是通过type构建的，只不过我们在用之前动态增加了一些属性而已，当然也可以拦截一些属性
        if attrs.get('test'):  # 如果取到返回内容，反之返回空值
            attrs.pop('test')  # 移除属性test
        return type.__new__(cls, name, bases, attrs)  # 必须return一个值

# 加上括号中内容，就不会直接用元类了
class MyList(object, metaclass=ListMetaclass):  # 没加括号内容默认还是找type
    a = 'hello'

    # 也可以拦截一些属性
    def test(self):
        print('----> test')

mylist = MyList()
print(mylist)  # TypeError: 'NoneType' object is not callable
mylist.test()
print(mylist.a, mylist.b)
