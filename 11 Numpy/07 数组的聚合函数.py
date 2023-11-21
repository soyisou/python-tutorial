# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
数组的聚合函数
    。最大值 max
    。最小值 min
    。求和 sum
    。平均值 mean
    。求标准方差 std

    # 针对bool值数组
    。all  -- 有一个为 False，结果就是 False，即：当所有元素都为 True的时候，结果为 True
    。any()  -- 有个一为 True，结果就是 True

    注意：数组本身也可以操作这些功能，Numpy也提供了这些功能。
'''

import numpy as np

a1 = np.random.randint(1, 100, size=10)
print(a1)

print('最大值：', a1.max())
print('最大值：', np.max(a1))

print('最小值：', a1.min())
print('最小值：', np.min(a1))

# 默认求所有数据的和
print('求和：', a1.sum())
print('求和：', np.sum(a1))

print('平均值：', a1.mean())
print('平均值：', np.mean(a1))

print('标准方差：', a1.std())
print('标准方差：', np.std(a1))

print('=' * 50)
bool_any = np.random.choice([False, True], size=10)
print(bool_any)
print(bool_any.all())
print(bool_any.any())
# 思考：多维的怎么办？ 能否处理多维的？  可以！

print('=' * 50)
a2 = np.random.randint(1, 100, size=(4, 5))
print(a2)

print('最大值：', a2.max())
print('最大值：', np.max(a2))

print('最小值：', a2.min())
print('最小值：', np.min(a2))

print('求和：', a2.sum())
print('求和：', np.sum(a2))

print('平均值：', a2.mean())
print('平均值：', np.mean(a2))

print('标准方差：', a2.std())
print('标准方差：', np.std(a2))

# 思考：如何求每一列的和呢？

# 求每一行的和
print('每一行的数据和：', a2.sum(axis=1))

# 求每一列的和
print('每一列的数据和：', a2.sum(axis=0))

# 求每一行的最大值
print('每一行的最大值：', a2.max(axis=1))

# 求每一列的最大值
print('每一列的最大值：', a2.max(axis=0))

# 求每一行的平均值
print('每一行的平均值：', a2.mean(axis=1))

# 其他操作也可以有类似的操作，获取每一行或者每一列的操作值！