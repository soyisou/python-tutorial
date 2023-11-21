# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

"""
运算符：
    1. 算术运算符：
       + - * / % **(平方) //(整除)
       数值型：+ 进行的是相加运算
       字符串：+ 进行的是连接运算

       数值型： * 表示乘法运算 2 * 5 = 10
       字符串： * 表示复制多少次字符串

       除法：除数不能为 0

    2. 赋值运算符
        = += -= *= /= %=

"""

a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # 余数
print(a ** b)
print(a // b)

s1 = 'hello'
s2 = 'world'
print(s1 + ' ' + s2)

s1 = 'abc'
print(s1 * 3)

result = a + b
print(result)

# id() 内置函数： id(变量名) 获取变量地址，返回一个整型值
c = 10
print(id(a),id(c))
print(id(a) == id(c)) # 证明同一个整数值都是一个值

e = 10
e += a # e = e + a
print(e)
