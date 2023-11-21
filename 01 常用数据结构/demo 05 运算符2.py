# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

"""
关系运算符：
    == != > < >= <=
    左边 运算符 右边 ——》 bool: True, False

逻辑运算符：
    and or not
    左边 运算符 右边 ——》bool值，True， False
"""

a1 = 5
a2 = 6
print(a1 < a2)

print(a1 == a2)

print(a1 != a2)

print()

b1 = 1000
b2 = 1000
print(b1 is b2)

print(b1 == b2)

a = '--'
print(a * 30)
a = 0
print(not a)

a = '--'
print(a * 30)
a = 8
print(not a)

a = '--'
print(a * 30)

a = ''
print(not a)

a = '--'
print(a * 30)

a = None
print(not a)

# and or
"""
and : 与
or : 或
"""

a = '='
print(a * 30)
t = True
f = False
print(t and f, t or f,)

print(a * 30)
number = input("请输入一个整形数字：") # number类型为字符串
print(type(number))
number = int(number)
print(8 > 5 and 5 == number)
print(8 < 5 or 5 == number)