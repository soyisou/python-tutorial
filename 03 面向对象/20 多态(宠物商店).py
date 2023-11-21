# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
多层继承：
    。格式
        class 类名(父类1, 父类2):
            pass
    。搜索顺序
        。类名.__mro__
        。类名.mro()
    。has a
        class 类：
            books = []

宠物商店：
    。issubclass(Cat, (Pet,))   ---> issubclass(类名,(父类1, 父类2))
    。isinstance(pet, Pet)   --->
'''

class PetShop:
    def __init__(self, name):
        # 宠物店名称
        self.name = name
        # 宠物店的宠物
        self.pets = set()  # 将宠物放入集合中

    # 寄存宠物
    def save_pets(self, pet):
        # 判断 pet 是否是 Pet 的实例
        if isinstance(pet, Pet):
            self.pets.add(pet)  # 将宠物加入到宠物集合中
            print('宠物: {} 添加成功！'.format(pet.pname))
        else:
            print('不是宠物，不收留！')

    # 卖宠物
    def sell_pets(self, pet):
        # 判断 pet 是否是 Pet 的实例
        if isinstance(pet, Pet):
            self.pets.discard(pet)  # 将该宠物从宠物店的名单中移除
            print('宠物减少！')

    # 查找宠物
    def search_pets(self, pname):
        for pet in self.pets:
            if pname == pet.pname:
                print('宠物在商店里')
                break
            else:
                print('宠物商店不存在此宠物！')

    # 显示所有宠物
    def show_pets(self):
        print('=' * 15 + '{}-宠物店所有的宠物信息如下：'.format(self.name) + '=' * 15)
        for pet in self.pets:
            print(pet)

class Pet:
    # 类别
    type = '宠物'

    # 初始化宠物信息
    def __init__(self, pname, color, age):
        # 宠物名字
        self.pname = pname
        # 宠物颜色
        self.color = color
        # 宠物年龄
        self.age = age

    # 返回宠物信息
    def __str__(self):
        s = '宠物类型是: {}, 宠物名: {}, 宠物颜色: {}, 宠物年龄: {}'.format(self.type, self.pname, self.color, self.age)
        return s

class Dog(Pet):
    type = '狗'
    # 看家
    def see_house(self):
        print('特长看家···')

class Cat(Pet):
    type = '猫'
    # 抓老鼠
    def catch_mouse(self):
        print('特长抓老鼠···')

class Bird:
    pass

# 创建对象
shop = PetShop('爱宠')

# 创建一个狗对象
dog = Dog('大黄', '黄色', 1)
shop.save_pets(dog)

# 创建一个猫对象
cat = Cat('花花', '米白色', 2)
shop.save_pets(cat)

cat = Cat('花花', '白色', 2)
shop.save_pets(cat)

# bird = Bird()
# shop.save_pets(bird)

shop.show_pets()

