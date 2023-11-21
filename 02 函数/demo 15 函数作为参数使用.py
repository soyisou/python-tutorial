# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
函数是否可以作为参数使用 ？  能

参数可以是：int, bool, float, list, tuple, set, dict, 函数
'''
from collections import Iterable

def func(n, msg):
    for i in range(n):
        print(i, msg)

print(5, 'hello')  # 整型是可以作为参数的，字符串也是可以作为参数的

def func1(books):
    if isinstance(books, Iterable):
        for book in books:
            print(book)

func1([1, 2, 3, 4])

func1({5, 6, 7, 8})

def A():
    print('hello world !')

def func2(f):
    print('----->', f)
    f()
    print('---->over')

func2(A)

print('=' * 50)

def func3(f):
    print('---->start:', f)

    def inner_func():
        print('---->inner_func')
        f()
    print('---->end')
    return inner_func  # 加括号表示将调用函数后的结果返回，因此不能加括号

result = func3(A)
print(result)