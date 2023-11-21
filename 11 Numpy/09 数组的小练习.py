# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
练习：
    。生成一个存放身高在150-200之间的长度为 10的数组
    。级联两个存放：男、女性别的长度为 10 的数组
        身高 性别 形成这个一个对应位置的数组
        170 男
        175 男
        165 女
'''
import numpy as np

# 生成一个存放身高在150-200之间的长度为 10的数组
height = np.random.randint(150, 200, size=10)
print(height)

print('=' * 50)

gender = np.random.choice(('男', '女'), size=10)
print(gender)

print('=' * 50)

# 纵向级联 -- 结果是横向的
info = np.vstack((height, gender), )
print(info)

print('=' * 50)

# 行和列翻转 -- 结果为纵向
info = info.T
print(info)

print('=' * 50)

# 判断是否是男性
ba = info[:, 1] == '男'
print(ba)

print('=' * 50)
male = info[ba]
print(male)

print('=' * 50)

# 思考：如何获取所有男生的平均身高？  1. 先获取身高  2. str --> int
male = male[:, 0]  # 获取第一列数据
print(male)  # 字符串类型

male = male.astype('i4')  # 转换数组的数据类型， 如果字符串数组表示的全是数字，也可以用astype转为数值类型
print(male.mean())

