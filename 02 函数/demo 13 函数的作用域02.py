# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
作用域：
    。全局作用域
    。局部作用域

    系统函数：
        。global  # 关键字，在函数中对全局变量进行声明而使用的。
        。globals() # 用在函数的外层，获取全局的变量 （系统默认产生的变量 + 自定义的变量）

        。nonlocal # 关键字, 没有 local关键字
        。locals() # 在函数中使用，获取的是当前函数的局部变量们。将函数中的局部变量放在字典中

    。搜搜变量的规则：
        。如果有内部函数，先找内部函数自身的变量
        。如果内部函数自身没有变量，则找外部函数的变量
        。如果外部函数也不存在此变量，则找全局变量
        。如果全局也不存在该变量，则找 builtins（内部模块）
        。如果内部 builtins 也没有，则报错
'''

number = 10
books = []
name = '张三'

def func1():
    books.append('西游记')  # 将数据放在全局变量 books， global可加可不加
    global number
    number += 5  # 不可变类型，必须加 global
    a = 100
    b = 20
    # locals 在函数中使用，获取的是当前函数的局部变量们。将函数中的局部变量放在字典中
    print(locals())  # 是相对的, {'a': 100, 'b': 20}

# func1()
# print(globals())
# print(locals())  # 是相对的

# LEGB 之 enclosing

a = 200  # 全局变量
d = 300 # 全局变量

# 以后分析代码，要学会划块
def func2():
    a = 10  # int  外部函数的局部变量
    b = 'good'  # str
    c = [1, 3, 4]  # list

    # 思考：能否在此定义一个函数 (内部函数)
    def inner_func2():  # 可以使用外部函数的变量
        a = 100  # 内部函数的局部变量
        print('我是一个内部函数:', a)  # 先从内部函数找
        print('我是一个内部函数:', b)  # 找不到，再从外部函数找
        print('我是一个内部函数:', d)  # 还找不到， 再找全局变量
        print('我是一个内部函数:', max)  # 最后还不到，再从 builtin 中找

    # 调用内部函数
    inner_func2()  # 不能在函数外部调用哦 ~
    print(locals())  # 内部函数也是作为一个变量出现的
    return c

r = func2()
print(r)

a = 100
b = 0
def func(b):
    a = 10
    b = 1000
    def inner_func(c):
        # b = c  # 报错，只要不改，随便用。直接改，会报错
        # global b
        nonlocal b # 内部函数使用外部函数的变量 b
        c = a + b + c
        b = c
        print('a:', a)
        print('b:', b)
        print('c:', c)
    inner_func(5)

func(8)

set1 = {1, 3, 5, 6}
set2 = {1, 3, 6, 8}
def func(set1, set3):
    global set2
    set2 = set1 & set3
t
func(set1, set2)
print(set1)  # {1, 3, 5, 6}
print(set2)  # {8, 1, 3, 6}