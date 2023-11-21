# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
可迭代的：Iterable ——> 迭代器：Iterator --> 生成器：generator
    。可迭代的：Iterable ——> 迭代器：Iterator   # 通过 iter()
    。迭代器：Iterator --> 生成器：generator  # 借助于 next()

可迭代对象分为：Iterable
    。迭代器：Iterator (通过next()可以得到下一个元素)  ----> 生成器 generator
    。序列：包括字符串 (str)、列表 (list)、元组 (tuple)
    。字典：dict

总结：
    。可迭代的不一定是迭代器   --> 但是可以通过 iter()将可迭代的变成迭代器
    。迭代器都是可迭代的

思考：可迭代的能够变为迭代器呢 ？ 可以！ 通过系统函数 iter()

'''
from collections import Iterable, Iterator

list1 = [1, 2]
set1 = {1, 2}
tuple1 = (1, 2)
dict1 = {'a': 1, 'b': 2}
generator1 = (x for x in range(2))  # 生成器

# list, set, dict, str 均是可迭代的
print(isinstance(list1, Iterable))  # True
print(isinstance(set1, Iterable))  # True
print(isinstance(dict1, Iterable))  # True
print(isinstance('hello', Iterable))  # True
# 生成器是可迭代的
print(isinstance(generator1, Iterable))  # True

# list, set, dict, str 均不是迭代器
print(isinstance(list1, Iterator))  # False
print(isinstance(set1, Iterator))  # False
print(isinstance(dict1, Iterator))  # False
print(isinstance('hello', Iterator))  # False
# 生成器是迭代器
print(isinstance(generator1, Iterator))  # True

'''
总结：
    。可迭代的不一定是迭代器
    。迭代器都是可迭代的
思考：可迭代的能够变为迭代器呢 ？ 可以！ 通过系统函数
'''
print('=' * 50)

list1 = iter(list1)
set1 = iter(set1)
print(isinstance(list1, Iterator))  # True
print(isinstance(set1, Iterator))  # True
