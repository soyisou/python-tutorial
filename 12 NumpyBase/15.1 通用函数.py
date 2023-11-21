"""
15.1 通用函数

numpy提供了许多通用函数，这些通用函数可以看做是以前通过Python计算的矢量化版本
1. abs/fabs
2. ceil/floor
3. exp
4. log/log2/log10
5. modf
6. sin/sinh/cos/cosh
7. sqrt
"""
import numpy as np

# 求绝对值
y = np.array([1, 2, 10, 1.3, 2.6, -10, 3, 5.5, -8.8, -8.3])
y = np.abs(y)
print(y)# [ 1.   2.  10.   1.3  2.6 10.   3.   5.5  8.8  8.3]

# 求绝对值
x = np.array([1, 2, 10, 1.3, 2.6, -10, 3, 5.5, -8.8, -8.3])
y = np.fabs(x) # 不能适用于复数
print(y) # [ 1.   2.  10.   1.3  2.6 10.   3.   5.5  8.8  8.3]

z = np.array([1, 2, 10, 1.3, 2.6, -10, 3, 5.5, -8.8, -8.3])
# 向上取整
print(np.ceil(z))
# 向下取整
print(np.floor(z))
# 四舍五入
print(np.rint(z))
# e为底数的指数函数
print(np.exp(y))

print('=' * 50)
x = np.array([1, 2, 10, np.e])
print(np.log(x))
print(np.log2(x))
print(np.log10(x))

x = np.array([1, 2, 10, 1.3, 2.6, -10, 3, 5.5, -8.8, -8.3])
# 浮点数拆分
print(np.modf(x)) # (array([ 0. ,  0. ,  0. ,  0.3,  0.6, -0. ,  0. ,  0.5, -0.8, -0.3]), array([  1.,   2.,  10.,   1.,   2., -10.,   3.,   5.,  -8.,  -8.]))

x = np.array([1, 2, 10, 4])
# 开平方
print(np.sqrt(x))