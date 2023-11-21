# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
函数的作用域：LEGB
local: 局部的
enclosing: 嵌套的
global: 全局
    。可变类型  ---可以省略 global声明
    。不可变类型  --- 不可以省略 global 声明
builtins: 系统内置

作用域的使用：
    。全局的 --- books = ['红楼梦', '西游记', '三国演义', '水浒传']  # 可变类型，可以省略 global
    。在函数中使用的时候：
        。因为 books 是可变类型，所以可以省略 global 声明
        。因为 number 是不可变类型，所以在函数中如果想要修改，则必须添加 global声明
'''
number = 10

def func():
    # number = 0  # 局部变量
    # 如果想要修改全局的变量 number，必须要明确声明
    global number  # 以下声明的 number是全局的 number
    print(number)  # 10
    number = 9  # 局部变量  --> 相当于对全局变量的值进行覆盖
    number += 5

func()
print(number)  # 14

# 全局变量
books = ['红楼梦', '西游记', '三国演义', '水浒传']  # 可变类型，可以省略 global

def func1():
    # books = []
    books.append('斩龙')  # 因为 books 是可变类型，所以可以省略 global 声明
    print(books)
    global number  # 因为 number是不可变类型，所以在函数中如果想要修改，则必须添加 global 声明
    number += 8

func1()
print(books)