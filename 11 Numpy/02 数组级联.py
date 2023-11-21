# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
数组级联 -- 类似于合并
    # []或元组等均可
    。np.concatenate([a1, a2], axis = 0)  # axis=0行合并, axis=1列合并
        。当合并行的时候，注意列数要相同
        。当合并列的时候，注意行数要相同
    。np.hstack  -- 水平方向 (horizontal)
    。np.vstack  -- 垂直方向 (vertical)
'''
import numpy as np

a1 = np.random.randint(1, 100, size=(4, 4))
a2 = np.random.randint(1, 100, size=(4, 4))
print(a1)

print('=' * 50)

print(a2)

print('=' * 50)
# 注意：传递级联的数组的时候，数组需要使用元组或者列表包含
a3 = np.concatenate([a1, a2], axis=1)  # axis=0，为行合并， axis=1，为列合并
print(a3)

print('=' * 50)
a4 = np.random.randint(1, 100, size=(3, 4))
print(a4)

# 水平方向 hstack
a5 = np.hstack((a1, a2))
print(a5)

print('=' * 50)

# 垂直方向 vstack
a6 = np.vstack([a1, a2])
print(a6)

