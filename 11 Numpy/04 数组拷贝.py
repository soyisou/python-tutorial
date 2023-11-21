# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
数组拷贝
    。类似于深拷贝 --- 拷贝出来一份，修改拷贝的那一份，对原来的那份没有影响
'''
import numpy as np

# 生成随机数组
a1 = np.random.randint(1, 100, size=(2, 3))
print(a1)

print('=' * 50)

a2 = a1.copy()  # 深拷贝
print(a2)

# 打印a2第一行，第二列
print(a2[1, 2])

# 修改a2第一行，第二列的值
a2[1, 2] = 88
print(a2)

print('=' * 50)

# 修改a2对a1并没有产生影响
print(a1)
