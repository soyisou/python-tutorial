"""
17.1 增删改

增加，插入，删除
1. 矩阵添加：numpy.append(参数1：数组，参数2：elements，参数3：axis=0/1)
2. 矩阵插入：numpy.insert(参数1：数组，参数2：index，参数3：elements，axis=0/1)
3. 矩阵删除：numpy.delete(参数1：a，参数2：elements，参数3：axis=0/1)
"""
import numpy as np

x=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x)

print(np.append(x, [0, 2])) # 末尾添加元素
print(np.append(x, [[0, 2, 11]], axis=0)) # 最后一行添加元素
print(np.append(x, [[0], [2], [11]], axis=1)) # 最后一列添加一列

print(np.insert(x, 1, [11, 12, 10]))
print(np.insert(x, 1, [[11, 12, 10]], axis=0))
print(np.insert(x, 1, [[11, 12, 10]], axis=1))
