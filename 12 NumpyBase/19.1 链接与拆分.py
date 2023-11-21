"""
19.1 链接和拆分

1. np.concatenate 对多个数组按指定轴的方向进行连接
2. np.stack/np.vstack/np.hstack/np.dstack组合
3. np.split/np.hsplit/np.vsplit/np.dsplit拆分
"""
import numpy as np
a = np.array([[1, 2, 3], [1, 2, 3]], dtype=np.int32)
b = np.array([[11, 22, 33], [11, 22, 33]], dtype=np.int32)
c = np.array([[44, 55, 55], [44, 55, 55]], dtype=np.int32)
print(a, b, c)

"""
通过axis作为关键字参数指定组合的方向，取值如下：
若待组合的数组都是二维数组：
1. 0：垂直方向组合
2. 1：水平方向组合
若待组合的数组都是三维数组：
1. 0：垂直方向组合
2. 1：水平方向组合
3. 2：深度方向组合

注意：vstack和hstack关注长和宽，dstack关注高，其实变成三维了
"""
print('=' * 50)
dd = np.concatenate((a, b, c), axis=0)
print(dd)

# 左右排序
dd = np.concatenate((a, b, c), axis=1)
print(dd)

print('=' * 50)
# np.stack()
a = np.floor(10 * np.random.random((2, 3)))
b = np.floor(10 * np.random.random((2, 3)))
print(a, b)

c1 = np.vstack((a, b))
print(c1)
"""
[[0. 1. 7.]
 [3. 4. 0.]
 [7. 9. 7.]
 [5. 4. 2.]]
"""

c2 = np.hstack((a, b))
print(c2)
"""
[[0. 1. 7. 7. 9. 7.]
 [3. 4. 0. 5. 4. 2.]]
"""

c3 = np.dstack((a, b))
print(c3)
"""
[[[2. 8.]
  [3. 8.]
  [0. 2.]]

 [[7. 4.]
  [3. 8.]
  [6. 8.]]]
"""

"""
对那些维度比二维更高的数组，hstack沿着第二个轴组合，vstack沿着第一个轴组合，concatenate允许可选参数给出组合时沿着的轴。
"""
a = np.floor(10 * np.random.random((2, 3)))
b = np.floor(10 * np.random.random((2, 3)))
print(a, b)

# 列拼接
c3 = np.column_stack((a, b))
print(c3)

# 行拼接
c4 = np.row_stack((a, b))
print(c4)

"""
np.split()
通过给出的数组与要拆分的份数，按照某个方向进行拆分。
使用hsplit你能将数组沿着它的水平轴分割，或者指定返回相同形状数组的个数，或者指定在哪些列后发生分割。
"""
print('=' * 50)
# 构建一个方便进行拆分的二维数组
a = np.floor(10 * np.random.random((6, 3)))
print(a)
"""
[[9. 0. 3.]
 [5. 3. 1.]
 [6. 5. 3.]
 [7. 5. 6.]
 [2. 3. 0.]
 [2. 8. 3.]]
"""

# 行均匀拆分
b = np.vsplit(a, 3)
print(b)
"""
[array([[9., 0., 3.],
       [5., 3., 1.]]), 
array([[6., 5., 3.],
       [7., 5., 6.]]), 
array([[2., 3., 0.],
       [2., 8., 3.]])]
"""
b = np.vsplit(a, (1, 4))
print(b)
"""
[array([[9., 0., 3.]]), 
array([[5., 3., 1.],
       [6., 5., 3.],
       [7., 5., 6.]]), 
array([[2., 3., 0.],
       [2., 8., 3.]])]
"""
for r in b:
    print(r)
"""
[[9., 0., 3.]]
[[5., 3., 1.],
 [6., 5., 3.],
 [7., 5., 6.]]
[[2., 3., 0.],
 [2., 8., 3.]]
"""

# 构建一个方便进行列差分的二维数组
a = np.floor(10 * np.random.random((2, 12)))
print(a)
"""
[[4. 7. 6. 1. 6. 9. 2. 7. 8. 0. 8. 9.]
 [9. 4. 3. 8. 9. 6. 0. 9. 8. 3. 0. 5.]]
"""

# 列均匀拆分，必须能够整除
b = np.hsplit(a, 4)
print(b)
"""
[array([[4., 7., 6.],
       [9., 4., 3.]]), 
array([[1., 6., 9.],
       [8., 9., 6.]]), 
array([[2., 7., 8.],
       [0., 9., 8.]]),
array([[0., 8., 9.],
       [3., 0., 5.]])]
"""

# 如果参数为元组，则是指定对应的拆分位置
c = np.hsplit(a, (3, 4, 7))
print(c)
"""
[array([[4., 7., 6.],
       [9., 4., 3.]]), 
array([[1.],
       [8.]]), 
array([[6., 9., 2.],
       [9., 6., 0.]]),
array([[7., 8., 0., 8., 9.],
       [9., 8., 3., 0., 5.]])]
"""
print('=' * 50)
a = np.floor(10 * np.random.random((3, 2)))
b = np.floor(10 * np.random.random((3, 2)))
c = np.dstack((a, b))
print(c)
a1, a2 = np.dsplit(c, 2)
print(a1, a2)
"""
[[[4. 3.]
  [8. 8.]]

 [[8. 6.]
  [0. 3.]]

 [[1. 4.]
  [3. 0.]]]
[[[4.]
  [8.]]

 [[8.]
  [0.]]

 [[1.]
  [3.]]] [[[3.]
  [8.]]

 [[6.]
  [3.]]

 [[4.]
  [0.]]]
"""

"""
如果两个数组的维度不一样，则可以使用np.pad()函数来搞定维度匹配的问题
"""
print('=' * 50)
array = np.array([1, 1, 1])
# (1, 2)表示在一维数组array前面填充1位，在最后面填充2位
# constant_values=(0, 2)表示前面填充0，后面填充2
ndarray = np.pad(array, (1, 2), 'constant', constant_values=(0, 2))
print(ndarray) # [0 1 1 1 2 2]

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3, 4])
# 填充b数组使其长度与a相同，头部补0个元素，尾部补1个元素
b = np.pad(b, pad_width=(0, 1), mode="constant", constant_values=-1)
print(b) # [ 1  2
