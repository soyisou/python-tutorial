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
                    clear()
                    del 列表[下标]

                修改：

                查找：

            4. 列表可以支持的符号
        元组
        集合
        字典

'''
# 停车场
car_park = []

# 添加
car_park.append('京A9909')
car_park.append('京A9919')
car_park.append('京A9929')
car_park.append('京A9939')

# 查询
print(car_park)  # ['京A9909', '京A9919', '京A9929', '京A9939']

for car in car_park:
    print(car)

# insert(位置，元素) --> 在某个位置，插入某个元素
car_park.insert(0, '京A9949')
print(car_park)

# 老板又买了一块地， 挨着的
car_park1 = ['京C9959']

# 可迭代的：一个一个可以按顺序往下取
car_park1.extend(car_park)  # ['京C9959', '京A9949', '京A9909', '京A9919', '京A9929', '京A9939']
print(car_park1)

# from  collections import Iterable
#
# print(isinstance(car_park, Iterable))  # 判断是否是可迭代的
# print(isinstance('abc', Iterable))  # 字符串是可迭代的
# print(isinstance(123, Iterable))  # 整数不是可迭代的
# print(isinstance(('tom', 100), Iterable))  # 元组是可迭代的

print('='*30)

# 删除元素
car_park1.append('京C9959')  # 直接从列表中删除第一个找到的元素
print(car_park1)  # ['京C9959', '京A9949', '京A9909', '京A9919', '京A9929', '京A9939', '京C9959']
car_park1.remove('京C9959')
print(car_park1)  # ['京A9949', '京A9909', '京A9919', '京A9929', '京A9939', '京C9959']

car_park1.pop()  # 不传参，默认删除最后一个元素
car_park1.pop(2)  # 表示删除下标位置为 2 的元素
print(car_park1)  # ['京A9949', '京A9909', '京A9919', '京A9929', '京A9939']

