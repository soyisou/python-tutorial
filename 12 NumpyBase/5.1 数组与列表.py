"""
5.1 数组和列表
概述：
数组与列表类似，是具有相同数据类型的多个元素构成的整体。

主要区别:
1. 数组元素要求是相同类型，而列表的元素可以是不同类型
2. 数组可以与标量进行运算，数组之间也可以进行矢量运算。（对应位置的元素进行运算， 无需进行循环操作）
3. 数组在运算时具备广播能力。（可以根据需要进行元素的扩展，完成运算）
4. 数组的底层使用 C 中的数组存储方式（紧凑存储，节省内存空间）

5.2 应用对比：
1. 将两个等长的列表（数组）分别进行数学运算（例如：+、-）
2. 将一个列表（数组）中的所有元素进行相同的改变。
3. 对步骤二进行计时，衡量时间消耗（练习）
4. 创建相同大小的列表（数组），衡量内存消耗。（练习）

5.3 Numpy 的矢量化运算
1. ndarray 数组具有广播能力
2. 数组与标量运算，实现的广播。
3. 数组可以与标量执行运行。（实际上会扩散到数组中的每个元素与该标量执行运算）
"""
import numpy as np

# 班级中的每个学生的年龄，如果是列表，则需要进行循环的操作
li = [13, 14, 15, 16]
for i in range(len(li)):
    li[i] += 1
print(li)

# 矢量化运算, 广播机制
na1 = np.array([1, 2, 3, 4, 5, 6])
na2 = na1 + 2
print(na1, na2)

# 对列表执行运算，需要使用循环
li1 = [1, 2, 3]
li2 = [4, 5, 6]
li3 = []
for x, y in zip(li1, li2):
    li3.append(x + y)

print(li3)

# 数组之间也可进行矢量化运算（此时就是数组中对应的元素执行相应的运算）
a = np.array([13, 14, 15, 16])
b = np.array([10, 20, 30, 40])
print(a + b)

# 如果是 ndarray 数组，则无需循环，直接进行矢量化运算
a = np.array([13, 14, 15, 16])
a += 1
print(a)

"""
Numpy 的广播运算
numpy 广播运算的三条规则：缺失维度的数组，将维度补充为进行运算的数组的维度。缺失的数组元素使用已有元素进行补充
规则一：补充缺失的维度（进行运算的两个数组之间的维度只能相差一个维度）
规则二：缺失元素用已有的值补充
规则三：缺失维度的数组只能有一行或者一列
"""
# 数组与数组之间实现的广播
b = np.array([10, 20, 30])
c = np.array([[1, 2, 3], [4, 5, 6]])
print(b + c)

"""
广播法则能够使通用函数有意义地处理不同相同形状的输入
广播第一法则是：如果所有的输入数组维度不都相同，一个“1”将被重复地添加在维度较小的数组上，直到所有的数组拥有一样的维度。
广播第二法则是：确定长度为1的数组，沿着特殊的方向表现地好像它有沿着那个方向最大形状的大小。对数组来说，沿着那个维度的
数组元素的值理应相同。

应用广播法则之后，所有数组大小必须匹配。

广播机制的作用：使得差别不是很大的两个数组也能够进行运算。前提是使维度较低的数组扩充到和较大数组一样的维度。

思考：为什么数组会比列表要快，而且快很多呢？
相同数据大小的 array 运算，直接作用到元素级上这一 numpy 特性！
"""