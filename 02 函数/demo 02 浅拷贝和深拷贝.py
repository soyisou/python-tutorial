# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
可变和不可变对象：
    在 Python 中，strings， tuples， numbers 是不可更改的对象
    list, dict 则是可以更改的对象

    不可变类型：变量赋值 a = 5 后，再赋值 a = 10, 这里实际是新生成一个 int值对象 10，再让 a 指向它，而 5 被丢弃，
              而不是改变 a 的值，相当于又生成了一个新的 a
    可变类型：变量赋值 la = [1, 2, 3, 4]后， 再赋值 la[3] = 10, 则是将 la的第三个值修改，而 la本身没有动，只是
            其内部的一部分值被修改了。
    不可变类型：类似于 C ++ 中的值传递，如整数、字符串和元组。如：fun(a)， 传递的只是 a 的值，没有影响 a 对象本身。
              如果 fun(a) 内部修改了 a 的值，则是新生成了一个 a 的对象。
    可变类型： 类似于 C ++ 中的引用传递，如列表、字典，如：fun(la)，则是将 la 真正地传过去，修改后外面的 la 也会
             受到影响。

    注：python中一切都是对象，严格意义上我们不能够说是值传递还是引用传递，我们应该说传不可变对象和传可变对象。


拷贝：其实就是将容器内数据，备份一份到新的地址
    浅拷贝：对于可变类型引用（共用）的是同一个(里面的内容改变，但是其地址是不会改变的)
          对于不可变类型，引用的是其地址。(一开始是共用的，但是如果有发生改变的，则其地址就会发生改变)

深拷贝：
    copy.deepcopy()
    列表中可变类型的元素，会有一个新的地址，而不是像浅拷贝一样，共用一个地址

'''
# 浅拷贝
# t1 = (1, 3, 4, 5)
# t2 = t1.copy()  # AttributeError: 'tuple' object has no attribute 'copy'

# 案例1
print('==========案例1==========')
list1 = [1, 2, 3, 5]
list2 = list1.copy()  # 将 list1 的内容复制到 list2
print(id(list1), id(list2))  # 31993000 31992616

# 案例2
print('==========案例2==========')
list1.pop(2)
print(id(list1), id(list2))  # 31993000 31992616

import random
import time
import copy

# 案例3
print('==========案例3==========')
list1 = ['jack', 20, '男', ['贾玲', '娜扎']]
list2 = list1.copy()  # 浅拷贝
print(id(list1), id(list2))

# 案例4
print('==========案例4==========')
list3 = copy.copy(list1)
print(list1, list2, list3)  # 内容一样，但地址不同
print(id(list1), id(list2), id(list3))  # 23867144 23866600 23866216

# 案例5
print('==========案例5==========')
# 添加信息
list2[3].append('凤姐')
print(list2)  # ['jack', 20, '男', ['贾玲', '娜扎', '凤姐']]
print(list1, list2, list3)  # 三个都是 ['jack', 20, '男', ['贾玲', '娜扎', '凤姐']]
print(id(list1), id(list2), id(list3))  # 30289672 30289128 30288744

# list1[3].remove('热巴')
# print(list1, list2, list3)  # 三个都是 ['jack', 20, '男', ['贾玲', '娜扎', '凤姐']
# print(id(list1), id(list2), id(list3))  # 30289672 30289128 30288744

# 案例6
print('==========案例6==========')
list1[1] = 30
print(list1, list2, list3)
# list1： ['jack', 30, '男', ['贾玲', '娜扎', '凤姐']]
# list2 和 list 3：['jack', 20, '男', ['贾玲', '娜扎', '凤姐']]
print(id(list1), id(list2), id(list3))

# 案例7
print('==========案例7==========')
a = 5
print(id(a))  # 140729319793184

# 案例8
print('==========案例8==========')
a = 10
print(id(a))  # 140729319793344

# 案例9
print('==========案例9==========')
la = [1, 3, 5, ['a', 'b']]
print(id(la))  # 2367746072968

# 案例10
print('==========案例10==========')
la[2] = 9
print(id(la))  # 2367746072968

# 深拷贝

import copy

# 案例11
print('==========案例11==========')
list1 = ['张三', 20, '男', ['娜扎', '热巴', '贾玲']]
# list2 = copy.copy(list1)  # 浅拷贝 共用里面的字符串地址，整数地址和列表地址，不共用外面的列表地址
list2 = copy.deepcopy(list1)  # 深拷贝  共用里面的字符串地址，整数地址， 不共用里面的列表地址，不共用外面的列表地址
print(list1, id(list1))  # 2953980731784
print(list2, id(list2))  # 2953982053832

print('==' * 50 + 'list1' + '==' * 50)
for e in list1:
    print(e, id(e))

print('==' * 50 + 'list2' + '==' * 50)
for e in list2:
    print(e, id(e))

'''
list1 = [1, 4, 3, ['a', 'b']]
list2 = list1.copy()
list2.remove(3)
print(list1, list2)

list2[3].append('hello')
print(list1, list2)
'''
# 案例12
print('==========案例12==========')
list1 = [1, 4, 3, ['a', 'b']]
list2 = list1.copy()  # 浅拷贝 --  整数和内部列表 ['a', 'b'] list1和 list2均共用
print('==' * 50 + 'list1' + '==' * 50)
for e in list1:
    print(e, id(e))

print('==' * 50 + 'list2' + '==' * 50)
for e in list2:
    print(e, id(e))
print('====list1====list2')
list2.remove(3)
print(list1, list2)  # [1, 4, 3, ['a', 'b']] [1, 4, ['a', 'b']]

# 案例13
print('==========案例13==========')
list1[3].remove('a')
list1[3].append('hello')
print(list1, list2)  # [1, 4, 3, ['a', 'b', 'hello']] [1, 4, 3, ['a', 'b', 'hello']]