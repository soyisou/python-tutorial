# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
数组的运算操作
    。+   np.add(a1, a2)
    。-   np.sub(a1, a2)
    。*   np.mutifly(a1, a2)
    。/   np.divide(a1, a2)
    。%   np.mod(a1, a2)
    。**  np.power(a1, a2)
    。1/  -- 小数
        。np.reciprocal(a1) -- 倒数 -- 整数
    。np.percentile(a1, 30)  # 求百分位 --- 特殊情况下(第二个参数为50)可以求中位数

    以上操作，针对于多个矩阵相同位置的元素进行的操作！

    。>=
    。<=
    。>
    。<
    。!=
    。==

    。矩阵的相乘
        。np.dot(a1, a2)
    。矩阵的转置
        。np.transpose(a)
        。a.T
    。排序 sort
        。numpy中的sort排序  -- 不影响本身
        。数组的sort排序 -- 影响了本身
'''

import numpy as np

# 产生随机数组
a1 = np.random.randint(1, 100, size=(5, 4))
# 拷贝数组 -- 深拷贝
a2 = a1.copy()
print(a1)
print('=' * 50)
print(a2)

print('=' * 50)

# 进行加法运算
print(a1 + a2)
print(np.add(a1, a2))

print('=' * 50)

# 进行减运算
print(a1 - a2)
print(np.subtract(a1, a2))

print('=' * 50)

# 进行乘法运算
print(a1 * a2)
print(np.multiply(a1, a2))

print('=' * 50)

# 进行除法操作
print(a1 / a2)
print(np.divide(a1, a2))

print('=' * 50)

# 进行模运算
print(a1 % a2)
print(np.mod(a1, a2))

print('=' * 50)

height = np.random.randint(50, 260, size=10)
print(height)

# >=   --  将数据将数组中的每一个元素进行比较，对应位置结果为 True 或者 False
ba = height >= 175
print(ba)

# 思考：如何提取175以上的身高信息?  根据bool结果提取数据即可

# 根据bool数组在原数组中取值
print(height[ba])

print('=' * 50)

a1 = np.array([[1, 2, 3], [4, 5, 6]])
print(a1)

print('=' * 50)

a2 = np.array([[1, 4, 7], [2, 5, 8]])
print(a2)

print('=' * 50)

print(a1 ** a2)
print(np.power(a1, a2))

print('=' * 50)
print(1/a1)
print(np.reciprocal(a1))  # 结果为整型

print('=' * 50)
# 取中间值的 --- 中位数 --- 特殊情况 --- 我们一般用其求中位数
a1 = np.array([[2, 4, 6], [0, 5, 7]])   # 排序：0 2 4 5 6 7
# 可以使用它取中位数，数据的中间值，第二个数据需要赋值为50
print(np.percentile(a1, 50))  # 那个数据占以上数据和的50%    -- 4.5

print('=' * 50)
a2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.percentile(a2, 30))  # 3.4
'''
在数组中获取占比百分之q位置的数据。
计算公式：
    (n - 1) * p = i + j   --- i 为整数部分，j 为小数部分，n 为一维数组的个数
    result = (1 - j) * a[i] + j * a[i + 1]
    如：a[1, 2, 3, 4, 5, 6, 7, 8, 9]
    step1： 计算一维数组的数值个数，n = 9
    step2： 需要计算的百分数，[0, 100] 上的整数，代表位置，例如：30是30%
    i: 是计算后的数值部分的整数部分
    j: 是计算后的小数部分，j = 0.4
    最后的结果：
    result = (1 - j) * a[i] + j * a[i + 1]
           = (1 - 0.4) * a[2] +  0.4 * a[3]
           = 0.6 * 3 + 0.4 * 4
           = 3.4  
'''

print('=' * 50 + 'a1' + '=' * 50)
a1 = np.random.randint(1, 10, size=(3, 5))
print(a1)

print('=' * 50 + 'a2' + '=' * 50)
a2 = np.random.randint(1, 10, size=(5, 3))
print(a2)

print('=' * 50 + 'a3' + '=' * 50)
a3 = np.dot(a1, a2)
print(a3)

print('=' * 50 + 'a1' + '=' * 50)
print(a1)

print('=' * 50 + '转置之transpose' + '=' * 50)
a3 = np.transpose(a1)
print(a3)

print('=' * 50 + '转置之.T' + '=' * 50)
a3 = a1.T
print(a3)

print('=' * 50 + 'a1' + '=' * 50)
print(a1)

# 排序np.sort()
print('=' * 50 + '排序之numpy.sort' + '=' * 50)
a3 = np.sort(a1)
print(a3)

# 排序之数组.sort()
print('=' * 50 + '排序之数组.sort' + '=' * 50)
a1.sort()  # 无返回值

print('=' * 50 + 'a1' + '=' * 50)
print(a1)

print('=' * 50 + 'random.permutation' + '=' * 50)
# 思考：能够部分排序？  可以！ partition -- 部分排序
a = np.random.permutation(1000)  # 生成从0开始到指定数据[)，指定数据长度的一维数组，这些数据是无序的！
print(a)

'''
kth
    。如果是正数获取的是最小的前几个数  --- 在数组的最前面
    。如果是负数获取的是最大的前几个数  --- 在数组的最后面
'''
print('=' * 50 + 'np.partition' + '=' * 50)
a1 = np.partition(a, kth=5)  # 最小的前五个数
# a1 = np.partition(a, kth=-5)  # 最大的前五个数
print(a1)