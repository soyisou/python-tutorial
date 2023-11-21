"""
7.1 numpy中的常数
正无穷：Inf = inf = infty = Infinity = PINF
负无穷：NINF
正零：PZERO
负零：NZERO
非数值：nan = NaN = NAN
自然数：e
pi
伽马：euler_gamma
None的别名：newaxis
"""
import numpy as np

# 正无穷
print(np.inf) # inf

# 负无穷
print(np.NINF) # -inf

# 正零
print(np.PZERO) # 0.0

# 负零
print(np.NZERO) # -0.0

# 非数值
print(np.NaN) # nan

# 自然数
print(np.e) # 2.718281828459045

# pi
print(np.pi) # 3.141592653589793

# 伽马
print(np.euler_gamma) # 0.5772156649015329

# None的别称
print(np.newaxis) # None

