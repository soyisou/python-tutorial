# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
高阶函数：
    。filter(function, iterable): 返回值是一个 filter object, 需要对返回值进行转换: list(filter_object)
    。function 函数的返回值必须是 bool 类型

    。reduce()  # 不是系统函数 from functools import reduce
    。reduce(function, iterable))  --> value
    。参数function是函数，此函数的参数必须是两个， lambda x, y: x * y
    。参数iterable是一个可迭代对象，依次取出对象进行处理即可

'''
# filter()  filter(function or None, iteralble)  --> filter object
numbers = [2, 4, 7, 9, 0, 12, 45, 78, 23]
filter1 = filter(None, numbers)
print(list(filter1))

filter2 = filter(lambda x: x % 2 == 0, numbers)
print(list(filter2))

list1 = ['hello', 30, '80', 'hi100', '99', 'yes']
filter3 = filter(lambda x: str(x).isdigit(), list1)
print(list(filter3))  # [30, '80', '99']

filter4 = filter(lambda x: isinstance(x, int) or x.isdigit(), list1)
print(list(filter4))  # [30, '80', '99']

students = [('jim', 18), ('lucy', 22), ('tom', 19), ('lily', 17), ('jack', 23)]
filter5 = filter(lambda x: x[1] > 20, students)  # 过滤年龄大于 20岁的同学
print(list(filter5))  # [('lucy', 22), ('jack', 23)]

from functools import reduce

list2 = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, list2)  # 10
print(result)

# 求5的阶乘
result = reduce(lambda x, y: x * y, [i for i in range(1, 6)])
# result = reduce(lambda x, y: x * y, range(1, 6))  # 也可，因为range返回的结果也是可迭代的
print(result)  # 120