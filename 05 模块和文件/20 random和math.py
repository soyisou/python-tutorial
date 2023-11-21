# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
random 随机数
    。randint(a, b)  # [a, b]
    。randrange(a, b)  # [a, b)
    。random()  # 得到一个小数[0, 1)
    。choice()  # 从非空序列中随机选取一个元素
    。shuffle(List)  # 打乱列表顺序

math 数学

'''
import random

random.randint(1, 10)  # 左右均闭
random.randrange(1, 10)  # 左闭右开
# 思考：randint和randrange的区别： 均是获取随机整数，randint[], 而randrange[)

print(random.random())  # x in the interval [0, 1)  即：左闭右开

# 从非空序列中选择一个随机元素
print(random.choice('aaflnadfwfgno243n23r'))

# 将列表洗牌
list1 = [1, 2, 4, 5, 7, 8]
random.shuffle(list1)  # 返回值为空
print(list1)

import math, cmath

# 天花板 --- 上取整
print(math.ceil(9.12))  # 10

# 地板 --- 下取整
print(math.floor(9.12))  # 9

# 直接用roun()进行四舍五入
print(round(9.52))  # math里面没有四舍五入，可以直接使用round()函数进行四舍五入

# 求和 -- 返回浮点数
list2 = [1, 2, 3, 4, 5]
print(math.fsum(list2))  # 15.0

# 求余 -- 返回浮点数
print(math.fmod(10, 3))  # 1.0

# 求绝对值
# 方法一：直接使用系统函数 abs()
print(abs(-9.6))  # 9.6
# 方法二：使用math.fabs()
print(math.fabs(-9.2))  # 9.2

# 开平方 -- 返回浮点数
print(math.sqrt(9))  # 3

# 求方 x的n次方  math.pow(x, n)
print(math.pow(2, 5))  # 32


