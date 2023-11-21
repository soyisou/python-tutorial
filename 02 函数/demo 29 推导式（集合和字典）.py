# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
列表推导式：
    。符号：[表达式 for i in iterable if 条件]
    。符号：[表达式1 if 条件1 else 表达式 2 for i in iterable if 条件]
集合推导式：
    。符号：{表达式 for i in iterable if 条件}
    。符号：{表达式1 if 条件1 else 表达式 2 for i in iterable if 条件}
字典推导式：
    。符号：{key: value for 循环}

思考：有没有元组推导式 ？
答案：没有！元组推导式，推到出来的是生成器！
'''

# 列表推导式
list1 = [x for x in range(10) if x % 2 != 0]  # 得到其中的奇数
print(list1)  # [1, 3, 5, 7, 9]

# 集合推到式
list2 = [1, 2, 3, 4, 5, 6, 3, 4, 7, 8, 5, 9]
set1 = {x for x in list2 if x % 2 != 0}  # 既去重，又得到其中的奇数
print(set1)

# 偶数不变，奇数加 1
set2 = {x if x % 2 == 0 else x + 1 for x in list2}
print(set2)

# 互换键和值的位置
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {value: key for key, value in dict1.items()}
print(dict2)

foods = ['火锅', '茶', '牛肉', '麻辣香锅', '红烧肉']
dict3 = {index + 1: value for index, value in enumerate(foods)}
print(dict3)
print(type(dict3))  # <class 'dict'>