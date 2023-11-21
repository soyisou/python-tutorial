# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
实现学生借书的具体实现

同包中.py文件之间的引用   ---> from 包名.模块名 import 具体内容
不同包中.py文件之间的引用

注意；无论是同包还是不同包，都是基于当前项目的位置点，往下搜索的！
'''
from student.modle import Student  # 同一包之间模块的导入
from book.modle import Book  # 不同包之间模块的导入
from module01 import *  # 导入module01, 导入非包里的内容

s1 = Student()
b1 = Book()
s1.borrow_book(b1)
s1.show()

print(number)

from student import test
test()