# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
用递归的方式求斐波那契数列
'''

# 使用递归的方式求斐波那契数列
list1 = []

# 1, 1, 2, 3, 5, 8 ···
def func(n):  # 非递归方式
    for i in range(n):
        if i == 0 or i == 1:  # 出口
            list1.append(1)
        else:
            list1.append(list1[i - 1] + list1[i - 2])

func(8)
print(list1)

def func1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return func1(n - 1) + func1(n - 2)

list2 = []
for i in range(1, 9):
    list2.append(func1(i))

print(list2)