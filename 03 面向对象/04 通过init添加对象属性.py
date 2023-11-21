# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
方式二：
    依赖__init__()完成
    __init__(self)  --> 系统的魔术方法（无需程序员自身调用，在某种条件下自动触发的方法）
        。init触发条件：创建对象的时候触发
        。可以在init里面，做到对象属性的统一
        。其中：self表示的是对象本身！[self代表类的实例，而非类 !]
            。可以通过 self.name = 值，进行赋值操作
'''
# 有缺陷，即无法做到所有属性的统一！
# class Student:
#     sname = 'zhangsan'
#     age = 18
#
# s1 = Student()
# s1.sname = 'tom'
# s2 = Student()
# s2.sname = 'lucy'
# s2.gender = '女'  # 给对象新添加了一个属性 gender
#
# print(s1.sname)  # tom
# print(s2.sname)  # lucy
# print(s2.gender)  # 女

class Student:  # 定义类属性的时候，self.sname，self.age 等是不会出现在Student中的
    def __init__(self):  # self就是我们创建的对象
        print('-------> init', self)
        self.sname = 'zhangsan'
        self.age = 18
        self.gender = '女'

# print(Student.age) # 报错
print('=' * 50)

s1 = Student()
'''
思考：该() 是干嘛的呢？
作用：
    1.表示固定格式  
    2. 底层当中，默认去找__init__()
        创建对象的步骤：
        step1：Student空间
        step2：按照Student类模型构建一个对象空间
        step3：找到一个魔术方法：__init__, 并执行该魔术方法__init__(self)
        step4：self.name = 'lucy'
        step5：给s1对象赋值s1 = 0550地址
        
'''
print(s1)
print(s1.sname)
print(s1.age)
print(s1.gender)

s2 = Student()
# print(s2)
print(s2.sname)
print(s2.age)
print(s2.gender)

print('=' * 50)

# 思考：如何修改对象的值呢？
class Student1:  # 定义类属性的时候，self.sname，self.age 等是不会出现在Student中的
    def __init__(self,name, age = 18, gender = '男'):
        print('-------> init', self)
        self.sname = name
        self.age = age
        self.gender = gender

student1 = Student1('lucy', 19, '女')
# print(id(student1))  # 2081565154632
print(student1.sname)
print(student1.age)
print(student1.gender)

student2 = Student1('tom', 12)
print(student2.sname)
print(student2.age)
print(student2.gender)