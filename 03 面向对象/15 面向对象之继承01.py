# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
继承：
    。目的：使程序的代码更加简练，提高了程序的可读性
    。实现继承
        class 子类名(父类):
            pass
    。子类继承了父类的非私有的属性和方法
    。对于公有的属性和方法，是可以直接在子类中访问的，但是对于私有的无法访问到

'''
# 将共性代码提取出来，将该类作为父类或者超类或者基类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 10000  # 改名为：_Person__money

    def eat(self):
        print('{}去食堂吃饭了！'.format(self.name))

    def sleep(self):
        print('{}想睡觉了！'.format(self.name))

# 子类
class Student(Person):  # (父类的名字)
    pass

class Teacher(Person):
    def show(self):
        print(self.name)
        print(self.age)
        # print(self.__money)
        # print(self._Person__money)  # 10000
    pass

class Admin(Person):
    pass

s = Student('李同学', 18)
print(s)
s.eat()
s.sleep()

print('=' * 50)

t = Teacher('张老师', 35)
print(t)
t.eat()
t.sleep()
t.show()