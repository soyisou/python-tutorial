# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
is a  --> 继承  子类继承父类
has a  --> has a 一个类里面去使用另一个类

'''

class Book:
    def __init__(self, name, price, author, number):
        self.name = name
        self.price = price
        self.author = author
        self.number = number

    # 增加书籍的数量
    def add_number(self):
        self.number += 1

    # 减少书籍的数量
    def reduce_number(self):
        self.number -= 1

    # 返回书籍对象的信息
    def __str__(self):
        s = '书名：{}, 价格：{}, 作者：{}, 数量：{}'.format(self.name, self.price, self.author, self.number)
        return s

class Student:
    def __init__(self, name, clazz):
        # 存放学生姓名
        self.name = name
        # 存放学生班级
        self.clazz = clazz
        # 存放学生所借书籍
        self.books = []  # [book1, book2, book3 ···] 每本书都是一个对象

    def borrow_books(self, book):  # has a 问题 -- 一个类使用另一个类
        self.books.append(book)

    def send_books(self, book):
        pass

    def show_books(self):
        for book in self.books:
            print(book)

    def __str__(self):
        s = '班级：{} \n姓名：{}'.format(self.clazz, self.name)
        return s


book1 = Book('颈椎康复指南', 20, '李四', 5)
book2 = Book('防脱发指南', 25, '王五', 2)

s = Student('张三', '计算机1801')
s.borrow_books(book1)
s.borrow_books(book2)

# print(s)
s.show_books()




