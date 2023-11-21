# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
函数间的调用问题：

'''
import random

books = ['红楼梦', '三国演义', '西游记', '水浒传']

def show_book():
    print('-' * 20 + '图书馆书籍如下' + '-' * 20)
    for index, book in enumerate(books):
        print('{}: {}'.format(index + 1, book))

def add_book(book_name):
    if book_name:
        books.append(book_name)
        # 查看所加书籍
        show_book()
    else:
        print('书籍不能为空！')

show_book()
add_book('因梦而生')

def func1():
    ran = random.randint(0, 100)  # 左闭右开
    return ran

def func2():
    ran = func1()
    print('随机整数：', ran)
    print('---------调用函数func2-------')
    for i in range(ran):
        print(i)
    print('-------函数func2调用完毕------')

func2()