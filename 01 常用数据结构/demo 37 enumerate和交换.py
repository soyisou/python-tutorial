# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
1. enumerate
2. 交换
'''
set1 = {'小猫', '小狗', '旺财'}
for index, value in enumerate(set1):  # (index, value)
    print('{}:{}'.format(index, value))  # 0:小狗 1:旺财 2:小猫

# 交换 a 和 b 的值
a = 3
b = 5
print('-----> 交换前')
print('a:{}\t\tb:{}'.format(a, b))

# 交换 a 和 b 的值
c = a
a = b
b = c
print('a:{}\t\tb:{}'.format(a, b))

# 交换 a 和 b 的值
a, b = b, a
print('a:{}\t\tb:{}'.format(a, b))

# 注意：变量个数与数据类型的个数必须一致
tuple1 = (1, 5)
x, y = tuple1  # 1 5
print(x, y)

# 注意：变量个数与数据类型的个数必须一致
list1 = [1, 5]  # 1 5
x, y = list1
print(x, y)

# 注意：变量个数与数据类型的个数必须一致
set1 = {1, 4}
a, b = set1  # 1 4
print(a, b)
