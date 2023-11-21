# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
数组转置
'''
import numpy as np

a1 = np.random.randint(1, 100, size=(3, 4))
print(a1)

print('=' * 50)

a2 = np.transpose(a1)
print(a2)

a3 = np.ndarray.T
print(a3)