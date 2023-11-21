"""
3.3 其他创建 ndarray 的方式： 随机函数
np.random.rand 生成指定形状的 0-1 之间的随机数
np.random.random 用法基本和 rand 一样
np.random.randn 标准正态分布
np.random.normal 指定均值和方法的正态分布
np.random.randint 生成指定数值范围内的随机整数
np.random.seed 按照种子来生成随机数，种子一样，则生成的结果必一致
np.random.shuffer 打乱数组元素顺序
np.random.uniform 均匀分布
np.random.choice 按照指定概率从指定集合中生成随机数
"""
import numpy as np

# 生成指定形状的，每个位置元素都是 0-1 之间的随机浮点数的一个ndarray数组
aa = np.random.random(3)
print(aa)

# 生成指定形状的，2行3列的一个二维数组
bb = np.random.random((2, 3))
print(bb)

# 生成指定形状的0-1之间的随机数
aa = np.random.rand(3)
print(aa)


print('*' * 50)
# 生成指定形状的服从正态分布的从0-1之间的随机数
aa = np.random.randn(4) # 用法和 rand() 函数一样，只是 randn() 函数时服从正态分布
print(aa)

"""
loc 均值
scale 方差
size 元素个数
"""
# 生成指定形状的指定方差和均值的正态分布
aa = np.random.normal(loc=4, scale=0.01, size=10) # 指定方差和均值的正态分布
print(aa)

"""
随机整数 np.random.randint()
"""
# 在1-10范围里，随机生成5个int32类型的数值，生成的结果可能出现重复数值
aa = np.random.randint(low=1, high=10, size=5, dtype=np.int32)
print(aa)

"""
np.random.choice() 从指定数据集中，随机抽取一个数据
"""
aa = np.random.choice([1, 2, 3, 4], p=[0.1, 0.2, 0.3, 0.4])
print(aa)

# 检测是否按照概率生成
list1 = [0, 0, 0, 0]
for i in range(100000):
    aa = np.random.choice([1, 2, 3, 4], p=[0.1, 0.2, 0.3, 0.4])
    list1[aa - 1] = list1[aa - 1] + 1

result_list = [value / sum(list1) for value in list1]
print(result_list) # [0.09923, 0.19892, 0.3011, 0.40075]

"""
np.random.seed() 指定种子随机
seed()用于指定随机数生成时所用算法开始的整数值，如果使用相同的seed()值，则每次生成的随机数相同。
如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。
"""
np.random.seed(0)
aa = np.random.rand(4, 3)
print(aa)
np.random.seed(0)
bb = np.random.rand(4, 3)
print(bb) # 与上者相同

"""
np.random.shuffle() 打乱数据
"""
aa = np.arange(10)
print(aa)

np.random.shuffle(aa)
print(aa)

"""
均匀分布：np.random.uniform()
"""
# 生成1-10之间的5个随机数，可以包含1，但是不包含10
aa = np.random.uniform(1, 10, 5)
print(aa)
