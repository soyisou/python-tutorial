# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
普通函数： # 最大的类别，用的最多
    。参数
    。返回值
    。作用域
    。闭包
    。装饰器

递归函数： # 最后讲解，比较简单

高阶函数： # 匿名函数常和高阶函数结合起来使用

匿名函数： # 匿名函数常和高阶函数结合起来使用
    。函数体非常简单
    。函数使用次数较少
    。作用：
        。简化函数定义
        。使用更加方便
    。定义格式：
        。lambda 参数：返回值    如，lambda x: x + 1
'''
def calc(n):
    return n + 1

f = lambda n: n + 1

# print(f)  # <function <lambda> at 0x000002D87A4C5438>
print(f(5))  # 6

f1 = lambda x, y: x + y
print(f1(4, 8))  # 12

# 用途：匿名函数结合高阶函数使用
list1 = [2, 6, 3, 5, 1, 9]
print(sorted(list1))

list1.sort()
print(list1)

def func(x):
    return x[1]

list3 = [('jim', 18), ('lucy', 22), ('tom', 19), ('lily', 17), ('jack', 23)]
list4 = sorted(list3, key=lambda x: x[1], reverse=True)  # x表示列表中的元素, x[1] 表示年龄
# list4 = sorted(list3, key=func, reverse=True)  # 降序排列，func 为函数名
print(list4)

list3.sort(key=lambda x: x[1])  # 升序排列
print(list3)

print('=' * 50)

def func(f):  # lambda 地址给 f
    r = f(5)  # 5 * 2 = 10
    r += 10 # 10 + 10 = 20
    return r

result = func(lambda x: x * 2)
print(result)  # 20