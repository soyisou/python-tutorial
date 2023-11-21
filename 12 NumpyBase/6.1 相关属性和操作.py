"""
6.1 数组的相关属性和操作

数组对象具有如下常用属性：
ndim - 维度数
shape - 维度/形状
dtpye - 元数据类型
size - 元素个数
itemsize - 元素长度、字节数
nbytes 总字节数 = size x itemsize
real - 复数数组的实数数组
imag - 复数数组的虚数数组
T - 数组对象的转置视图
flat - 扁平迭代器
"""
import numpy as np
x = np.array([[1, 3, 4], [3, 4, 5]])
print(x)

# 获取数组的形状
print(x.shape) # (2, 3)

# 获取数组的维度
print(x.ndim) # 2

# 获取数组的元素类型
print(x.dtype) # int32

# 返回数组元素的个数（整体所有元素的个数）
print(x.size) # 6

# 返回数组元素占用空间的大小，以字节为单位
print(x.itemsize) # 4

# 返回总的字节数
print(x.nbytes) # 24

# 转置
print(x.T)

# 扁平化
print([elem for elem in x.flat]) # [1, 3, 4, 3, 4, 5]
