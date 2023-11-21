"""
14.1 Numpy的各种操作

数组与数的运算（加减乘除、取整、取模）
1. 加： + 或者 np.add(a, b)
2. 减： - 或者 np.subtract(a, b)
3. 乘： * 或者 np.multiply(a, b)
4. 除： / 或者 np.divide(a, b)
"""
import numpy as np

aa = np.array([1, 2, 3, 4])
bb = np.array([5, 6, 7, 8])
print(aa, bb) # [1 2 3 4] [5 6 7 8]

# 减法
cc = bb - aa
print(cc) # [4 4 4 4]

# 平方
dd = aa ** 2
print(dd) # [ 1  4  9 16]

ee = dd < 5
print(ee)

"""
注意：像 += *= 等操作，都是在原数组的基础上进行更改，而不是返回新的数组
"""
aa *= 10
print(aa) # [10 20 30 40]

a = np.array([[1, 1], [0, 1]])
b = np.array([[2, 0], [3, 4]])
print(a, b)
"""
[[1 1]
 [0 1]] 
 
 [[2 0]
 [3 4]]
"""

# 普通乘法(对应位置直接相乘)
print(a * b)
"""
[[2 0]
 [0 4]]
"""

# 矩阵乘法(点乘，对应位置相乘再相加)
result = np.dot(a, b)
print(result)
"""
[[5 4]
 [3 4]]
"""

aa = np.arange(60, 90, 5)
print(aa)
"""
[60 65 70 75 80 85]
"""

score = aa.reshape((2, 3))
print(score)
"""
[[60 65 70]
 [75 80 85]]
"""

# 循环数组行和列，每个数值都加5
score[:, :] = score[:, :] + 5
print(score)
"""
[[65 70 75]
 [80 85 90]]
"""


