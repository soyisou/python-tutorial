# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
python: 可变 不可变
    不可变类型：只要改变变量的值，则地址发生改变，则认为该类型是不可变的
           如， int str float tuple  # 以上类型都不支持添加
    可变类型：内容发生改变，但是地址没有发生改变，则认为该类型是可变的
           如，list, set, dict

    对于字典来说，key 放的都是不可变的。如，key 不可以为 list 类型（因为list的内容是可以改变的，会导致字典不唯一）
'''
n = 10  # 小整数对象池 n 指向 10
print(id(n))  # 2087581760

n = 11  # n 断开对 10 的指向，n 重新指向 11
print(id(n))  # 2087581776

s = 'hello'
print(id(s))  # 31589888

s = 'hello1'
print(id(s))  # 31591520

f = 9.99
print(id(f))  # 21968416

f = 8.8
print(id(f))  # 27735104

tuple1 = (1, 34)
print(id(tuple1))  # 12702184

tuple1 = (2, 36)
print(id(tuple1))  # 13455752

# 以上类型都不支持添加

# 列表是可变类型
list1 = [2, 3, 4]
print(id(list1))  # 26946760

list1.append(7)
list1.remove(2)
print(id(list1))  # 26946760

list1 = [9, 6, 4]
print(id(list1))  # 26946376

# 集合是可变类型
set1 = {2, 4, 5}
print(id(set1))  # 34208760

set1.add(3)
print(id(set1))  # 34208760

# 字典是可变类型
dict1 = {'a': 1, 'b': 2}
print(id(dict1))  # 26773096

dict1.pop('a')
print(id(dict1))  # 26773096