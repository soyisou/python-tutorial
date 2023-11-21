# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
运算相关的 系统柜内置函数:
    1. sum(list)  --> 和
    2. min(list)
    3. max(list)
'''
list1 = [1, 3, 4, 6, 4, 7, 8, 9]
list2 = [1, 3, 4, 7, 8, 9]

s = 0
for i in list1:
    s += i
print(s)

# 求列表中元素和
print(sum(list1))

# 求列表中元素最大值
print(max(list1))

# 求列表中元素最小值
print(min(list1))

list1 = [1, 3, 4, 6, 4, 7, 8, 9]
list2 = [1, 3, 4, 6, 4, 6, 8, 9]

flag = True
if len(list1) == len(list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            flag = False
            break

    if not flag:
        print('不一样')
    else:
        print('完全一样')
else:
    print('不一样')
