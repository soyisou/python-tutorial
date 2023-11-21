# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
广播机制
    。规则：所有数组是以形状最长的那个看齐的，形状中不足的部分会自做自动补齐操作，维度缺失的部分是补1的。
    。这个广播机制是适用于，将一个确定的数据或者跟矩阵等列的一维数组，与矩阵进行运算。
    。
'''
import numpy as np

# 案例1：a + 1
a1 = np.random.randint(1, 100, size=(4, 5))
print(a1)

print('=' * 50)

print(a1 + 1)

print('=' * 50)

# 案例2：单位数组
ones = np.ones(shape=(4, 5))
print(ones)

print('=' * 50)
# 案例3：
a2 = np.random.randint(1, 100, size=5)  # 等列一维数组
print(a2)

print('=' * 50)

print(a1 + a2)