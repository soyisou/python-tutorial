# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
闭包：
    定义：
        。闭包是由函数及其相关的引用环境组合而成的实体（即：闭包 = 函数块 + 引用环境）
    符合以下条件：
        。嵌套函数
        。内部函数引用了外部函数的变量
        。返回值是内部函数名
    用途：
        。装饰器的时候用
    注意：
        。如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数
          就认为是闭包(closure)
'''
def outer(n):
    a = 10

    def inner():
        b = a + n
        print('内部函数：', b)

    return inner

r = outer(5)
print(r)

r()