# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
@property  装饰器，是用来装饰类中方法的
    。步骤：
        step1: 在 get方法上面添加 @property装饰器, 函数的名字最好更加简要[让使用者调用起来、访问起来更加简便]
        step2: 装饰 set方法，@属性名.setter
                    @属性名.setter
                    def 属性名(self, 参数):
                        pass
        step3: 使用
                  。对象 = 类名(参数)
                  。print(对象，属性名)  ---> get 方法
                  。对象.属性名 = 值
    。总结：
        。日后，如果需要对私有化的属性进行一些操作的时候，就可以这样加了，既可以像以往一样使用私有属性，又能
          够通过一些条件对设置或访问属性进行条件限制。

'''

class Person:
    # 限制作用  ---> 限制了外界动态属性的添加！
    __slots__ = ['__name', '__age', '__flag', '__password']  # 加进来的才是能赋值的！如果没有加到里面，外界是不能赋值的！

    def __init__(self, name, age):
        self.__name = name  # 私有化属性
        self.__age = age  # 私有化属性
        self.__flag = False
        self.__password = '1234'

    @property
    def name(self): # 改装 name
        # 有需求可以定制内容，添加验证条件，比如：判断用户是否登录等
        if self.__flag == True:
            return self.__name
        else:
            print('没有权限查看该用户名！')

    @name.setter  # 引用name函数，绑定set   --- 加了装饰器后，底层做了一些操作
    def name(self, name):  # 改装 set
        if len(name) >= 6:
            self.__name = name
            print('名字设置成功！')
        else:
            print('名字必须要大于等于6位！')

    def age(self):
        return self.__age

    def set_age(self, age):
        if 0 < age < 125:
            self.__age = age
        else:
            print('年龄设置失败！必须在0 ~ 125之间！')

    def login(self, username, password):
        if self.__name == username and self.__password == password:
            print('登录成功！')
            self.__flag = True
        else:
            print('用户名或者密码有误！')

p = Person('jack', 21)
p.login('jack', '1234')

p.name = 'steven'  # 进入 name函数
print(p.name)  # steven

p.name = 'zhangsan'