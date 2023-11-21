"""
10.1 数组的扁平化
我们可以调用ravel或者flatten方法，对数组对象进行扁平化处理
1. np.ravel / ravel
2. flatten
3. shape, reshape, resize, ravel
二者的区别在于：ravel返回原数组的视图，而flatten返回原数组的拷贝。

由于ravel扁平的数组顺序通常是“C风格”的，也就是说，最右边的索引变化得最快。所以元素a[0, 1]之后是a[0, 1]。
如果数组被改变形状(reshape)成其他形状，数组仍然是“C风格”的。Numpy通常创建一个以这个顺序保存数据的数组，
所以ravel将总是不需要复制它的参数3。但是如果数组是通过切片其他数组或者有不同寻常的选项时，它可能需要被复制。
函数reshape和ravel还可以被通过一些可选参数构建成FORTRAN风格的数组，即最左边的索引变化最快。

reshape函数改变参数形状并返回它，而resize函数改变数组自身。

总结一下：
C风格：order=C，行主顺序，最右边的索引变化最快。
F风格：order=F，列主顺序，最左边的索引变化最快。

resize(): 把指定的数组改变形状，但是元素个数可变，不足补0，无返回值，即对原始多维数组进行修改。
"""
import numpy as np

x = np.arange(12).reshape(3, 4)
print(x)

# ravel返回原数组的视图
print(x.ravel())
print(np.ravel(x))

# flatten返回原数组的拷贝
print(x.flatten())

print('=' * 50)

x = np.arange(12).reshape(3, 4)
print(x)

# 二者的主要区别：
# flatten 返回原数组的拷贝，所以x和y2没有关系
y2 = x.flatten()
y2[0] = 100
print(x, y2)

# vavel 返回原数组的视图，所以x和y1引用相同的数据
y1 = x.ravel()
y1[0] = 100
print(x, y1)

