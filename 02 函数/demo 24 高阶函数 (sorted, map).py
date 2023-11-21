# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
高阶函数：
    。定义：把函数当成参数，进行传递的函数
    。如，sorted(iterable, key, reverse)  # 其中 key就是一个函数参数
        。sorted(list1, key=函数名, reverse=True)
            。按照 key 给这个函数指定规则
            。# 按分数排序
            。dict1 = {'zhangsan': 90, 'lisi': 100, 'wanglu': 89, 'zhaoliu': 99}
            。dict4 = dict(sorted(dict1.items(), key=lambda x: x[1]))
            。print(dict4)  # {'wanglu': 89, 'zhangsan': 90, 'zhaoliu': 99, 'lisi': 100}
        。map(func, iterable)  --- 系统函数之一
            。names = ['tom', 'jack', 'lily', 'jim']
            。map2 = map(lambda x: x.capitalize(), names)
            。print(list(map2))  # ['Tom', 'Jack', 'Lily', 'Jim']
'''

dict1 = {'zhangsan': 90, 'lisi': 100, 'wanglu': 89, 'zhaoliu': 99}
print(sorted(dict1))  # ['lisi', 'wanglu', 'zhangsan', 'zhaoliu']
print(sorted(dict1, key=lambda x: dict1[x]))  # ['wanglu', 'zhangsan', 'zhaoliu', 'lisi']

print(sorted(dict1.items(), key=lambda x: x[1]))  # [('wanglu', 89), ('zhangsan', 90), ('zhaoliu', 99), ('lisi', 100)]

# 按分数排序
dict4 = dict(sorted(dict1.items(), key=lambda x: x[1]))
print(dict4)  # {'wanglu': 89, 'zhangsan': 90, 'zhaoliu': 99, 'lisi': 100}

print('=' * 50)

# map：映射 --> 按照一种方式，返回一个新的结果
map1 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # map object
print(map1)  # <map object at 0x0000016BCDF0CC08>
print(list(map1))  # [1, 4, 9, 16, 25]

print('=' * 50)
names = ['tom', 'jack', 'lily', 'jim']
map2 = map(lambda x: x.capitalize(), names)
print(list(map2))  # ['Tom', 'Jack', 'Lily', 'Jim']



