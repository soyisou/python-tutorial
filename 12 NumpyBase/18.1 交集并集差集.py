"""
18.1 交集并集和差集

交集：numpy.intersect1d(参数1：数组a，参数2：数组b)——查找两个数组中的相同元素
差集：numpy.setdiff1d(参数1：数组a，参数2：数组b)——查找在数组a中在数组b中的元素
并集：numpy.union1d(参数1：数组a，参数2：数组b)——查找两个数组的并集元素
"""
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])

print(np.intersect1d(a, b)) # [3 4 5]
print(np.setdiff1d(a, b)) # [1 2]
print(np.union1d(a, b)) # [1 2 3 4 5 6 7]