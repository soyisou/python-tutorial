# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
numpy的基本操作
    。变形
        。reshape(行，列) -- 行和列赋值的时候，要考虑一下数组中元素的总个数，看看给定的行和列是否符合数据均分
         的情况，不符合的话，就会报错了。
        。行和列也可以给定-1，行给-1，只考虑列，根据数据的总数和列数，自动计算出行数。列给-1，同理。

'''
import numpy as np

# 随机生成一个4行5列的数组
arr = np.random.randint(1, 100, size=(4, 5))  # 范围，大小
print(arr)

print('=' * 50)

# 数组变形 -- 注意：要均分
arr = np.reshape(arr, newshape=(5, 4))
print(arr)

print('=' * 50)

# 数组变形 -- 注意：要均分
arr = np.reshape(arr, newshape=(5, -1))  # 自动计算列
print(arr)

print('=' * 50)

# 数组变形 -- 注意：要均分
arr = np.reshape(arr, newshape=(-1, 10))  # 自动计算列
print(arr)
#
# import keyword
#
# print(keyword.kwlist)

