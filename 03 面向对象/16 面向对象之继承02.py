# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
继承：
    。步骤：
        。step1: 定义一个父类
        。step2:定义子类，继承父类
            。继承父类非私有的属性和方法
            。如果子类定义了一个跟父类相同的属性，先找子类的属性，然后才去找父类
            。如果父类与子类有相同的方法，则认为子类重写了此方法(重写[覆盖]：override)
'''
class Animal:
    type1 = '动物'

    def __init__(self):  # 如果有子类调用，那么此时的self永远指的是子类对象本身！
        self.name = '花花'
        print('----> Animal')

    def run(self):
        print('{}正在奔跑···'.format(self.name))

    def eat(self):
        print('{}喜欢吃···'.format(self.name))

    def __str__(self):  # 调用print(对象)或者str(对象)时触发
        return '当前类型: ' + self.type1  # 使用self,优先先找自己，如果找不到，再去父类找

class Dog(Animal):
    type1 = 'dog'

    def __init__(self, name, color):
        # 调用父类的__init__方法，推荐将父类的init放在最前面！
        Animal.__init__(self)  # 会找父类的__init__方法

        # 后面的name和color会把前面的覆盖掉
        self.name = name
        self.color = color

        # 如果将父类的init放在后面，则会覆盖子类的name和color！
        # Animal.__init__(self)  # 会找父类的__init__方法    ---> 打印 "花花"

    def see_home(self):
        print('看家高手···')

    def eat(self):
        print('{}喜欢啃骨头···'.format(self.name))

dog = Dog('大黄', '黄色')
dog.eat()
dog.run()
dog.see_home()
print(dog)



