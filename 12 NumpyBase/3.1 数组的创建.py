"""
3.1 数组的创建
"""
# 目的：学会创建各种维度的 ndarray 对象

"""
Numpy 提供了很多方式（函数），来创建数组对象，常用的方式如下：
array
arange
ones/ones_like
zeros/zeros_like
empty/empty_like
full/full_like
eye/identity
linspace
logspace
frombuffer
fromiter
fromfunction

说明：注意 arange 函数，不是 arrange
    arange 和 linspace 的区别
"""
import numpy as np

list1 = [1, 2, 3, 4, 5]
print(type(list1)) #<class 'list'>

array1 = np.array(list1)
print(array1)
print(type(array1)) # <class 'numpy.ndarray'>

# display 的功能要比 print 更强大一些，是 ipython 提供的。
# 在输出时，优先使用dispaly, 这样可以比print显示更加友好。【与out对象显示的格式是一样的】
aa = range(1000)

"""
ndarray 优点：
ndarray 组织数据更紧凑，执行效率更高
numpy 提供了很多的常用的科学计算函数，所以编写代码也变得更简单

numpy最核心的类型，就是多维数组类型numpy.ndarray
"""

# 创建一个多维数组【二维数组】
array2 = [[1, 2], [3, 4], [5, 6]]
n = np.array(array2) # 只要接收一个数组序列就可以
print(n)

# np.array() 函数： 参数给了什么格式的数据，就构建什么样式的ndarray
"""
二维数组：类似于excel表格，或者mysql表的样式。这种二维结构的数据，也是最常用的数据。
如果想要做数据挖掘，那么以后接触的数据，有可能维度会非常高
如果只做数据分析，那么二维数据一定是最长用的。
如果是二维数组，那么就看做是一个矩阵： numpy 给我们提供了一种矩阵的概念：matrix
注：主要是二维数组的乘法和矩阵的乘法会不一致！
"""

# python 中的 range() 函数生成 list
# start, stop, step

list11 = list(range(5, 10, 2))
print(list11)
print(np.array(list11))

# 使用 np.arange() 函数(类似于python中的range函数，但功能更加强大)
# 功能更强大：步长可以是浮点数，也可以是负数！
n = np.arange(0, 10, 2.3)
print(n)
print('*' * 50)
print(type(n))

"""
总结：python 中没有，我 numpy 有。python 中有的，我 numpy 更强大！
"""

"""
np.ones() / np.zeros() / np.full()
"""
# 创建值全为 1 的数组
n = np.ones((3, 4))
print(n)

# 创建值全为 0 的数组
n = np.zeros((3, 4))
print(n)

# 思考：如何创建任意维度，任意值的数组呢？
n = np.full((3, 4),  8) # 第一个参数：维度， 第二个参数：填充元素的值
print(n)

"""
np.ones_like() / np.zero_like() / np.full_like()
按照已有的 ndarray 来进行复制创建
"""
data22 = np.arange(30) # 一维数组
print(data22.reshape((5, 6))) # 二维数组
print(data22.reshape((6, 5))) # 二维数组
print(data22.reshape((2, 5, 3))) # 三维，两个五行三列的二维数组
print(data22.reshape((3, 2, 5))) # 三维，三个两行五列的二维数组

# 注：不管做什么维度之间的转换，最终维度的乘积的结果一定要相等

# 思考：创建一个与参数数组形状相同的数组，值全为1
x = np.ones_like(n) # 复制数组n的维度，保持一样的维度，但是元素都是one
print(x)

x = np.zeros_like(n)
print(x)

x = np.full_like(n, 9)
print(x)

# np.empty() 空矩阵

# 创建值全为空的数组（值并非为空，而是值尚未经过初始化），创建一个内容随机并且依赖于内存状态的数组
x22 = np.empty((2, 3))
print(x22)

# 创建单位矩阵
"""
np.eye() / np.identify()
单位矩阵特点：
1. 主对角线上的元素全为1
2. 行数和列数都是一样的
"""

# 创建单位矩阵
print(np.eye(4)) # 方法一
print(np.identity(4)) #方法二

"""
创建对角矩阵 np.diag() 对角矩阵
参数：
    参数1：主对角线数值
    参数2：对角线元素（k = 0 表示主对角线，k > 0 表示主对角线之上的元素，k < 0 表示主对角线之下的元素）
"""
array_diag = np.diag([10, 20, 30, 40]) # 列表为对角矩阵的值
print(array_diag)

array_diag[1][0] = 99
print(array_diag)

"""
等差数列：np.linspace() 等差数列
"""

# 关注的是元素之间的差值
nda1 = np.arange(1, 20, 3)
print(nda1) # [ 1  4  7 10 13 16 19]

# 关注的是元素的个数
nda2 = np.linspace(1, 22, 5)
print(nda2) # [ 1.    6.25 11.5  16.75 22.  ]
"""
创建等差数列的数组：
num 指定数组中元素的个数，endpoint 指定是否包含终点。（默认是true，包含）
"""
line_array = np.linspace(1, 10, num = 6, endpoint=True, dtype=np.int32)
print(line_array)

"""
创建等比数列：np.logspace()等比数列
创建等比数列的数组（前两个参数指定指数）
num指定数组元素的个数。endpoint 指定是否包含终点数。base用来指定底数，默认为10
"""
# 在2**1 和 2**7 生成8个数，恰好构成一个等比数列
log_array = np.logspace(1, 7, num=8, endpoint=True, base=3)
print(log_array)

"""
注意：arange 和 linspace ，二者都可以产生一系列区间值
对于 arange而言，更关注的是数值之间的步长是多少，而不太关注具体会产生多少个数值。
对于 linspace而言，更关注的是数值的个数，而不太关注数值之间的距离是多少。
"""







