# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
返回值；
    。如果函数没有返回值则默认的返回值是None
    。如果在函数中添加返回值，要通过return关键字
        。return 作用：
            。返函数值
            。结束函数的调用
                。break 结束循环
                。return 出现在函数中，表示结束函数
                。return 可以单独使用，返回值是 None
                。Python 独有
                    。return a, b, c  # 返回的是元组形式 (a, b, c)
'''
list1 = [4, 5, 3, 6, 7, 2]
sorted(list1)  # 系统内置函数，返回一个新的列表
print(list1)  # 依然是原列表

# 找到最大值
def find_max(list1):
    if isinstance(list1, list):
        max = list1[0]
        for i in list1:
            if i > max:
                max = i
        return max

# 找到最大值所在的下标位置
def find_index(list1):
    if isinstance(list1, list):
        max1 = list1[0]
        max_index = 0
        for index, value in enumerate(list1):
            if value > max1:
                max1 = value
                max_index = index

        return max_index

# 找到最大值和最大值所在的下标位置
def find_max_index(list1):
    if isinstance(list1, list):
        max_value = list1[0]
        max_index = 0
        for index, value in enumerate(list1):
            if value > max_value:
                max_value = value
                max_index = index

        return max_value, max_index

# 找到最大值
print(find_max(list1))
# 找到最大值对应的索引
print(find_index(list1))
# 寻找最大值以及最大值对应的下标位置
print(find_max_index(list1))


