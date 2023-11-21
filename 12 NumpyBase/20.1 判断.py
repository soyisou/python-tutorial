"""
20.1 判断：

np.any()/np.all()
np.all()是对 np.array中所有元素进行与操作，然后结果返回 True 或者 False
np.any()是对 np.array中的所有元素进行或操作，然后结果返回 True 或者 False
"""
import numpy as np

print(np.any(np.array([True, True, False]))) # True
print(np.all(np.array([True, True, False]))) # False

aa = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
bb = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print((aa == bb).all()) # True
print((aa == bb).any()) # True

aa = np.arange(30).reshape((5, 6))
aa[3, 4] = 0
np.random.shuffle(aa)
print(aa)

print(np.any(aa, axis=0))
print(np.any(aa, axis=1))

print(np.all(aa, axis=0))
print(np.all(aa, axis=1))