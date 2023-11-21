# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
functools模块
    。reduce() # 可进行加减乘除等，关键看函数怎么写
    。partial() 偏函数
        。偏函数(partial function) 是通过将一个函数的部分参数预先绑定为某些值，从而得到一个
          新的具有较少可变参数的函数。

'''

from functools import partial

def add(x, y):
    return x + y

# lambda x, y: x + y

res = add(1, 3)
print(res)

# 每次都有3，还需要填写，有简便方法么？
add(3, 5)
add(3, 6)
add(3, 9)

add1 = partial(add, 3)
r = add1(9)
print(r)

r = int('123', base=8)
print(r)  # 64 + 16 + 3 = 83

r = int('00101101', base=2)
print(r)  # 45

int1 = partial(int, base=8)
print(int1('123'))  # 83

map0 = map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print(list(map0))  # print(list(map0))

