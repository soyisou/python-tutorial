"""
9.1 改变形状
我们可以通过数组对象的 reshape（或者 np 的 reshape 方法）方法来改变数组的形状
说明：
1. 改变数组形状时，如果维度大于1，可以将另一个维度设为-1
2. numpy 中存在很多方法，既可以用 np 来访问，也可以通过数组对象来访问
"""
import numpy as np
x = np.arange(10)
print(x)

# 使用np.reshape方法(只能通过元组的形式传入)
y = np.reshape(x, (2 ,5))
print(y)

# 通过数组对象方法
y = x.reshape(2, 5)
print(y)

# 级联操作和-1处理
aa = np.arange(30).reshape(5, 6)
print(aa)

bb = np.arange(30).reshape(5, -1)
print(bb)