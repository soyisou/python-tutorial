# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
函数的参数：
    普通参数：
    参数的个数：要求定义函数时的个数与调用函数时的个数要一致
    参数的类型：
              str in float bool tuple
              list set dict   --- 可变类型  --- 可变类型函数传递的是地址
'''

# def func(a, b, c):
#     return a + b + c
#
# # 调用函数
# func(2, 4, 5)
from collections import Iterable


# 打印 friends
def print_friends(name, friends):
    # 打印信息
    print('{}的朋友如下：'.format(name))
    if isinstance(friends, Iterable):  # 判断是否是可迭代的
        for friend in friends:
            print(friend)
    else:
        print('---->', friends)

name = '钢铁侠'
# friends = '绿巨人'  # 字符串也是可迭代的
# friends = 666  # 整型不是可迭代的
friends = ['雷神', '鹰眼', '黑寡妇', '绿巨人']  # 列表是可迭代的

# 调用函数查看 friends
print_friends(name, friends)

# print(isinstance(friends, Iterable))  # True

# 添加朋友们 friends
def add_friend(friends):
    name = input('请输入朋友的名字：')
    if isinstance(friends, list):
        friends.append(name)

name = '钢铁侠'
friends = ['雷神', '鹰眼', '黑寡妇', '绿巨人']  # 列表是可迭代的
add_friend(friends)
print_friends(name, friends)

print('==' * 50)

# 思考： --- 添加朋友们 friends
def add_friend(f):
    name = input('请输入朋友的名字：')
    if isinstance(f, list):
        f.append(name)

name = '钢铁侠'
friends = ['雷神', '鹰眼', '黑寡妇', '绿巨人']  # 列表是可迭代的
add_friend(friends)
print_friends(name, friends)