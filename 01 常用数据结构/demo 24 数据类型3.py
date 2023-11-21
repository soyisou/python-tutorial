# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
    数据类型：
    int str float bool complex(复数)
    ‘容器’
        列表：list
            1. 创建：
                list1 = []
                list2 = [2, 3, 5]

                特点：
                    1. 没有长度限制
                    2. 可以存放任意类型
            2. 内容的访问：
                1. 取一个元素： list1[下标]
                2. 取多个元素： 借助于切片： 类似于字符串用法
                    list[start:]  # 从 start 到结尾
                    list[:end]  # 从 0 到 end - 1
                    list[start:end - 1]  # 从 start 到 end - 1
                    list[start:end:step]  # 从 start 到 end - 1， 每次步长 step

                    逆序：step 必须是负数
                    list[::-step]  # 逆序输出整个列表
                    list[start:end:-step]  # 从 start 到 end - 1， 每次的步长 step （从右向左）
            3. 内置函数
                增加：
                    append(object)  # 列表的末位追加
                    insert(index, object)  # 将对象 object 插入到 index 位置 (插队)
                    extend(iterable)  # 将一个可迭代对象添加到列表中 --> 可迭代的：一个一个可以按顺序往下取


                删除：
                    remove()  # 直接从列表中删除第一个找到的元素，如果没有找到要删除的元素则报错：
                                Raises ValueError if the value is not present.
                    pop([index])  # 可以传参，也可以不传参。一旦传参，传的是下标
                             1. pop() 不传参，默认删除列表的最后一个元素
                             2. pop(index) 删除index对应位置的元素
                             # 如果传的下标位置没有或超出范围 --> IndexError: pop index out of range
                    clear()  # 仅仅清空内容
                    del 列表[下标]  # 内容、地址都回收

                查找：
                    list1.index()  # 参数是要查找对象，返回的是对象的位置，如果没有则报错

                修改：
                    list1[位置] = 新值 --> 新值则替换该位置的旧值

            4. 列表可以支持的符号
        元组
        集合
        字典

'''
numbers = [2, 3, 5, 3, 6, 7]
numbers.remove(3)  # [2, 5, 3, 6, 7]
print(numbers)

numbers.pop()  # [2, 5, 3, 6]
print(numbers)

numbers.pop(3)  # [2, 5, 3]
print(numbers)

# 不是列表特用的删除方式，而是系统的通用删除
del numbers[1]  # [2, 3]
print(numbers)

# print(id(numbers))  # numbers 的地址

# 从内当中将整个列表都删除
# del numbers  # 有点狠了，内容没了，地址也没了，很彻底 --> 既清空内容，又删除地址
# print(numbers)

# numbers.clear()  # 且空内容，但地址保留
# print(numbers)

# [2, 3]
pos = numbers.index(3)  # 参数是要查找的对象，返回的是对象的位置，如果没有报错
print(pos)

# [2, 9]
numbers[pos] = 9
print(numbers)

