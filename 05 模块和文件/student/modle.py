# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
包：
    。包： 文件夹 + __init__.py   ---> 包
    。包里面存放的是多个模块
    。包的作用：
        。组织模块
        。避免模块名的命名冲突问题
            。不同包里面的模块同名是没有问题的
    。包中内容的导入：
        。import 包名.模块名
        。from 包名.模块名 import 具体内容[变量，函数，类]

    补充：无论包也好，模块也好，都是基于当前项目的位置，往下搜索！

modle
    。modle是结合数据库来操作的，在此处就暂时不结合数据库啦
    。虽然都叫做module，但在不同的包里面的，避免了同名的混淆，通过包来区分他们

'''
# import book.modle   # 使用后名字太长了
from book.modle import Book  # 注意：from后面定义的一定是模块，import后面定义的是具体的

class Student:
    # 注意：跟数据库关联的没有往__init__里面放，都是直接放外面的
    def __init__(self):
        self.name = '张三'
        self.no = '0001'
        self.age = 18
        self.gender = '男'
        self.books = []

    # 显示学生学号和姓名
    def show(self):
        print(self.no, self.name)
        for book in self.books:
            print(book)

    # 借书
    def borrow_book(self, book):
        # if isinstance(book, book.modle.Book):  # 直接写Book会报错的！包之间的引用也需要导入嘀！
        #     self.books.append(book)

        if isinstance(book, Book):  # 直接写Book会报错的！包之间的引用也需要导入嘀！
            self.books.append(book)
