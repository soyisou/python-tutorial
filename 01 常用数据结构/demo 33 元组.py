# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
元组：
    1. 一种容器，也可以存放多个元素
    2. 列表支持增、删、改、查元素，但是元组不支持删除、添加、修改其中元素 --> 元组放完元素便不能动了
    3. 声明：
        # 声明空列表和空元组
        tuple = ()  --> 类似于列表 list1 = []

        # 声明非空列表
        list2 = [1, 3, 4, 5]

        # 声明非空元组
        tuple2 = (1, 3, 4, 5)

        list2 = list()  --> 同 list3 = []
        tuple2 = tuple()  --> 同 tuple3 = ()

        tuple4 = (1)  # 类型为： int
        print(type(tuple4))

        tuple4 = (1, )  # 类型为：tuple
        print(type(tuple4))
        # 注意：声明元组的时候，如果只有一个元素一定要在最后加一个逗号，否则就是整型了

    4. 获取： --> 元组支持下标索引和切片
        tuple2 = (1, 3, 4, 5)
        print(tuple2[2], tuple2[-1], tuple2[::-1], tuple2[-1:-3:-1])  # 支持下标索引和切片

        注意：用切片切的是哪种数据类型，得到的切片类型还是原类型哦 ~
    5. 元组的内置函数：
        不支持：
            1. 添加
            2. 删除
            3. 修改

        支持：
            1. 查找 --> 可以使用 index() ，不可以使用 find()
                        tuple2 = (1, 3, 3, 4, 5)
                        print(tuple2.index(3))  # 1
            2. 计数 --> count() 计数
                        tuple2 = (1, 3, 3, 4, 5)
                        print(tuple2.count(3))  # 2

        排序：
            1. 可以使用sorted() 系统函数排序，但是返回的结果是一个列表
            2. 先 sorted 再类型转换
                    # 排序 + 类型转换 --> 返回结果为 () 类型
                    list1 = sorted(tuple2)
                    tuple3 = tuple(list1)
                    print(tuple3)

        类型的转换：
            str <--> int
            list <--> tuple
                列表 --> 元组   tuple(list) --> 得到的就是一个元组类型
                元组 --> 列表   list(tuple) --> 得到的是列表

        用元组类型实现：找最大值、最小值、求和、排序
            max()
            min()
            sum()
            sorted()
            # 求元组最小值、最大值、求和
            tuple2 = (1, 6, 3, 3, 4, 5)
            print(max(tuple2), min(tuple2), sum(tuple2))  # 6 1 22
'''
# 声明列表 和 元组
list1 = []
tuple1 = ()

print(type(list1))  # <class 'list'>
print(type(tuple1))  # <class 'tuple'>

# 声明非空列表
list2 = [1, 3, 4, 5]
# 声明非空元组
tuple2 = (1, 3, 4, 5)

# 声明符号上和列表不一样，但方法类似
print(type(list2))  # <class 'list'>
print(type(tuple2))  # <class 'tuple'>

# 获取元素  --> 元组支持下标索引 和 切片
tuple2 = (1, 3, 4, 5)
print(tuple2[2], tuple2[-1], tuple2[::-1], tuple2[-1:-3:-1])

# 查找
tuple2 = (1, 6, 3, 3, 4, 5)
print(tuple2.index(3))  # 1

# 计数
print(tuple2.count(3))  # 2

# 排序
print(sorted(tuple2))  # 返回列表  [1, 3, 3, 4, 5, 6]

# 注意：sorted() 可以辅助排序，但是其返回类型是一个 []

# 排序 --> 返回结果为 () 类型
list1 = sorted(tuple2)
tuple3 = tuple(list1)
print(tuple3)

# 求元组最小值、最大值、求和
tuple2 = (1, 6, 3, 3, 4, 5)
print(max(tuple2), min(tuple2), sum(tuple2))  # 6 1 22