# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
元组可以支持的符号：
    + :
    * :
    [] :
    [:] :
    in :
    is :

元组不支持
    添加：
    删除：
    修改：

    只能借助与 list 和 tuple 之间的转化完成
'''
tuple1 = (1, 6, 3, 3, 4, 5)
tuple2 = (1, 6, 4, 5)
tuple3 = (1, 6, 4, 5)

new_tuple = tuple1 + tuple2
print(new_tuple)  # (1, 6, 3, 3, 4, 5, 1, 6, 4, 5)
print(tuple2 * 2)  # (1, 6, 4, 5, 1, 6, 4, 5)
print(5 in tuple1)  # True

# 判断两个元组是否是同一个元组
tuple2 = (1, 6, 4, 5)
tuple3 = (1, 6, 4, 5)
print(id(tuple2), id(tuple3))
print(tuple2 is tuple3)  # True

# 判断两个列表是否是同一个列表
list1 = [1, 6, 3, 3, 4, 5]
list2 = [1, 6, 3, 3, 4, 5]
print(list1 is list2)  # False
# 注意：此处，元组和列表不同！

tuple4 = (1)
# print(tuple4 + 3)  # TypeError: can only concatenate tuple (not "int") to tuple

tuple4 = (1)  # 类型为： int
print(type(tuple4))

tuple4 = (1, )  # 类型为：tuple
print(type(tuple4))
# 注意：声明元组的时候，如果只有一个元素一定要在最后加一个逗号，否则就是整型了

import random

tuple4 = (1, )  # 类型为：tuple
# print(id(tuple4))  # 31181408
list4 = list(tuple4)
for i in range(10):
    ran = random.randint(1, 10)
    list4.append(ran)

# 将列表转成元组
tuple4 = tuple(list4)
# print(id(tuple4))  # 32004136
print(tuple4)

# 即经过处理后即便打印依然是元组，但是此元组并非原来的元组啦！
# 即当你需要用到添加、修改和删除的时候，还是直接用列表吧！