# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
列表推导式：
    。有点类似于 map
    。格式：[表达式 for i in list|tuple|dict[if 条件]]
    。格式：[表达式 1 if 条件 else 表达式 2 for i in list|tuple|dict[if 条件]]
'''

list1 = [1, 3, 4, 5, 7, 9, 8]
list2 = [i for i in list1 if i % 2 == 0]  # 筛选偶数
print(list2)
'''
# 底层实现
for i in list1:
    if i % 2 == 0:
        list2.append(i)
'''

# 如果是偶数加 1， 奇数加 2 呢？
list3 = [i + 1 if i % 2 == 0 else i + 2 for i in list1]
print(list3)  # [3, 5, 5, 7, 9, 11, 9]
'''
# 底层实现
for i in list1:
    if i % 2 == 0:
        list2.append(i + 1)
    else:
        list2.append(i + 2)
'''
list0 = [1, 2, 3]
list1 = [1, 3, 4, 5, 7, 9, 8]
list2 = [1, 4, 5]
list4 = [(x, y) for x in list0 for y in list1]
print(list4)
'''
# 底层实现
for x in list0:
    for y in list1:
        t = (x, y)
        list4.append(t)
'''

# 三层行不行 ？ OK ！
list5 = [(x, y, z) for x in list0 for y in list1 for z in list2]
print(list5)
'''
for x in list0:
    for y in list1:
        for z in list2:
            t = (x, y, z)
            list5.append(t)
'''
