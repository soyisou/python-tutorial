"""
23.1 排序：

np.sort(
参数1：a, 数组
参数2：axis=0/1, 0表示行1表示列
)
注意：
np.sort()作为函数使用，不更改被排序的原始array
array.sort()作为方法使用，会对原始array修改为排序后数组array
"""
import numpy as np

aa = np.array([1, 5, 6, 6, 6, 2, 3, 4, 5])
bb = np.sort(aa)
print(bb) # [1 2 3 4 5 5 6 6 6]

a = np.arange(1, 31)
np.random.shuffle(a)
b = a.reshape((5, 6))
print(b)
"""
[[28 19  7 15 29 18]
 [17 26  3 23 20  9]
 [ 6  2  4 25 12 10]
 [24 30 13  5 22  8]
 [ 1 27 11 21 14 16]]
 """
print(np.sort(b))
"""
[[ 7 15 18 19 28 29]
 [ 3  9 17 20 23 26]
 [ 2  4  6 10 12 25]
 [ 5  8 13 22 24 30]
 [ 1 11 14 16 21 27]]
"""
print(np.sort(b, axis=0)) # 按行排序
"""
[[ 1  2  3  5 12  8]
 [ 6 19  4 15 14  9]
 [17 26  7 21 20 10]
 [24 27 11 23 22 16]
 [28 30 13 25 29 18]]
"""
print(np.sort(b, axis=1)) # 按列排序
"""
[[ 7 15 18 19 28 29]
 [ 3  9 17 20 23 26]
 [ 2  4  6 10 12 25]
 [ 5  8 13 22 24 30]
 [ 1 11 14 16 21 27]]
"""

"""
思考：数据对象ndarray与numpy都具有sort方法，二者等价吗？
有的时候，我们不是对全部数据感兴趣，我们可能只对最小或者最大的一部分感兴趣。

部分排序：np.parition(a, k)
1. 当k为正时，我们想要得到最小的k个数
2. 当k为负时，我们想要得到最大的k个数
"""
print('=' * 50)

aa = np.array([4, 2, 8, 6, 5, 1, 9, 7])
# 取最小3个
bb = np.partition(aa, 3)
print(bb) # [1 2 4 5 6 8 9 7]
print(bb[:3]) # [1 2 4]

# 最大3个数
cc = np.partition(aa, -3)
print(cc) # [5 4 1 2 6 7 8 9]
print(cc[::-1][:3]) # [9 8 7]
