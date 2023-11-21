# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
数组的增删改操作
    。添加元素
        。np.append(操作数组，添加数据，axis)
            。在末尾追加元素  -- 如果不设置axis则永远会将数组变为一维的。
            。多维数组添加元素，如果添加的是一个元素，会转为一维数组，并添加至末尾
            。多维数组添加元素，如果添加的多个一维元素，会转为一维数组，并添加至末尾
            。多维数组添加元素，如果添加的是个多维数组，则可以添加行或者添加列
                。添加行的时候，要保证列数与原数组一致
                。添加列的时候，要保证行数和原数组一致
        。np.insert(操作数组，插入位置，插入数据，axis)
            。在指定位置插入元素  -- 如果不设置axis则永远会将数组变为一维的。
            。多维数组插入元素，如果添加的是一个元素，则会转为在一维数组指定位置插入元素
            。多维数组插入元素，如果添加的是个多维数组，则可以值指定行添加行或者列
                。插入行的时候，要保证列数和原数组一致
                。插入列的时候，要保证行数和原数组一致
    。删除操作
        。np.delete(操作数组，删除位置，axis)

'''
import numpy as np

# 生成随机数组
a1 = np.random.randint(1, 100, size=(2, 3))
print(a1)

print('=' * 50)

# 添加元素 -- 添加一个元素
a2 = np.append(a1, 7)  # 转为一维数组，添加至末尾
print(a2)  # print(a2)

print('=' * 50)

# 添加元素 -- 添加多个元素
a3 = np.append(a1, [78, 33])
print(a3)

print('=' * 50)

# 添加元素 -- 添加多个元素
a4 = np.append(a1, [[22, 33, 44], [77, 88, 99]], axis=0)  # 默认 axis=0， 添加行
print(a4)

print('=' * 50)

# 添加元素 -- 添加多个元素
a5 = np.append(a1, [[22, 33, 44], [77, 88, 99]], axis=1)  # 添加列
print(a5)

print('=' * 50)

print(a1)

# 在指定位置添加列
'''
# 在指定位置添加列，如果设置的是一个数据，默认这一列都是这一个数据
np.insert(a, 1, 10, axis=1)
'''
print('=' * 50)
a6 = np.insert(a1, 3, 1)
print(a6)  # [51 81 88  1 14 90 63]

print('=' * 50)
a7 = np.insert(a1, 3, [11, 22], axis=1)  # 注意元素的个数，必须和行数相同！
print(a7)

print('=' * 50)
a8 = np.insert(a1, 2, [11, 22, 33], axis=0)  # 注意元素的个数，必须和列数相同！
print(a8)

# 删除元素 delete
print('=' * 50)
a8 = np.delete(a1, 0, axis=0)
print(a8)