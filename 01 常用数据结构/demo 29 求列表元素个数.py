# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
list1 = {1, 2, 34, 6, 3, 7}
求列表中的个数 ？

符号问题：
    + :  # 将两个列表进行拼接，拼接成一个列表
    * :  # 同字符串，将列表中元素整体倍增多少倍
    [] :
    [:] :
    in : # 判断元素是否在列表中
'''
list1 = [1, 2, 34, 5, 6, 3, 7, 5, 2, 3, 6, 5]
count = 0
for i in list1:
    if i == 5:
        count += 1
else:
    print('5 的个数是：', count)

print(list1.count(5))  # 3

# 符号：
list2 = [1, 2, 3, 5, 6, 7, 9, 4, 49, [9, 4, 49]]

list3 = [9, 4, 49]

new_list = list2 + list3  # list2.extend(list3)
print(new_list)

list4 = list3 * 2  # 同字符串，将列表中元素整体倍增多少倍
print(list4)

print(8 in list2)  # 元素是否在列表中

print(list3 in list2)  # 判断列表是否在另一个列表中