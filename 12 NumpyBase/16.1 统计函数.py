"""
16.1 统计函数

Numpy（或数组对象）具有如下常用的统计函数
1. mean/sum/prod(连乘)
2. max/min/amax/amin
3. argmax/argmin（最大值、最小值索引）
4. std/var(标准差和方差)
5. cumsum/cumprod（累乘和累加）
6. all/any
7. median/percentile# 中位数和百分比分位数
"""
import numpy as np

x = np.array([1, 2, 3, 4, -1, -2, -3, -4])
print(x)

x = np.arange(1, 11).reshape(2, 5)
print(x)

# x = np.array([1, 2, 3, 4, -1, -2, -3, -4, np.NaN])
# 求和、求平均、最大值、最小值、连乘
print(np.sum(x), np.mean(x), np.max(x), np.min(x), np.prod(x))
# 在求和的时候忽略Nan
print(np.nansum(x), np.nanmean(x), np.nanprod(x))
# 求最大值、最小值对应的索引
print(np.argmax(x), np.argmin(x))
# 求最大值、最小值对应的索引（忽略NaN）
print(np.nanargmax(x), np.nanargmin(x))

x = np.arange(30).reshape(5, 6)
print(x)
np.random.shuffle(x)
print(x)
print(x.ravel())
print(np.nanargmax(x), np.nanargmin(x))

# 标准差和方差
x = np.arange(1, 11).reshape(2, 5)
print(np.nanstd(x), np.nanvar(x))

# 累乘和累加
x = np.arange(1, 11).reshape(2, 5)
print(x)
print(np.nancumsum(x), np.nancumprod(x))

# 中位数和百分比分位数
aa = np.arange(1, 10)
print(np.median(aa), np.percentile(aa, 99))