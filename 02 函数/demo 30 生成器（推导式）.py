# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
生成器：generator
    。推导式使用的符号()
    。函数 + yield

生成器，迭代器，可迭代的，三者之间的关系：

'''

list1 = [x for x in range(2000)]
print(list1)

g = (x for x in range(3))
print(type(g))  # <class 'generator'>
print(g)  # <class 'generator'><class 'generator'>
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
print(next(g,'over'))  # 默认值设为了 'over'

print('=' * 50)
r = range(5)
print(r)
print(type(r))

for i in range(5):
    pass

'''
range的使用：
    。r = range(5) 是可迭代的，但不是迭代器和生成器
    
'''
from collections import Iterable, Iterator
# iterable
# Iterator
# generator
r = range(5)
print(isinstance(r, Iterable))  # True
print(isinstance(r, Iterator))  # False

import types
print(isinstance(r, types.GeneratorType))  # False
