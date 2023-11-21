# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
for
    格式： # 每循环一次取序列中的值，将值赋值给变量 i
        for i in 序列：
            循环体的内容

        序列：str, list, tuple, set, dict
        range()
        int

'''
# r = range(1, 11)  # 1, 2, 3, 4 ···10
r = range(1, 11, 2)  # 1, 3, 5, ···9
# print(type(r))  # <class 'range'>
for i in r:
    print(i)

names = ['jack', 'tom', 'jerry', 'lily']
for i in names:
    print(i)

s = 'hello'
for i in s:
    print(i)
else:
    print("----------over--------")

