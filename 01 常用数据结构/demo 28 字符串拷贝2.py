'''
列表总结：
    1. copy() 完成的是一个浅拷贝
        浅拷贝：执行 copy() 动作，返回一个新的地址（存放的内容同原来内容）
        内容：分类：
                1. 字符串或整型  ---> 两个地址(列表)使用的是同一个地址
                2. 列表  --> 内层的列表是一个单独的空间， 愿列表和复制后列表使用的都是同一个地址
'''
list1 = ['张三', '李四', '王五', '赵六', '田七']
list1_copy = list1.copy()
print(list1, id(list1))  # ['张三', '李四', '王五', '赵六', '田七'] 19541224
print(list1_copy, id(list1_copy))  # ['张三', '李四', '王五', '赵六', '田七'] 19540840

list1.pop()
list1.append('二狗')
list1_copy = list1.copy()
print(list1, id(list1))  # ['张三', '李四', '王五', '赵六', '二狗'] 19541224
print(list1_copy, id(list1_copy))  # ['张三', '李四', '王五', '赵六', '田七'] 19540840

list1.remove('王五')
list1.append('赵柳')
print(list1, id(list1))  # ['张三', '李四', '赵六', '二狗', '赵柳'] 19541224
print(list1_copy, id(list1_copy))  # ['张三', '李四', '王五', '赵六', '田七'] 19540840

print('=' * 30)

list3 = ['张三', '李四', ['王五', '赵六', '二狗']]
list3_copy = list3.copy()
print(list3)  # ['张三', '李四', ['王五', '赵六', '二狗']]
print(list3_copy)

list3 = ['张三', '李四', ['王五', '赵六', '二狗']]
list3[0] = 'zhangsan'
print(list3)  # ['zhangsan', '李四', ['王五', '赵六', '二狗']], 张三的连接断掉，重新连上 zhangsan 链接
print(list3_copy)  # ['张三', '李四', ['王五', '赵六', '二狗']]

# print(list3[2][2])  # 二狗
# print(len(list3[2]))  # 3

# 思考：切片操作 ? 也可以用切片做拷贝哦 ~
list5 = [2, 4, 7, 98, 0]
list6 = list5[:]  # list5 和 list6 地址不一样！
print(id(list5))  # 35851304
print(id(list6))  # print(id(list6))

list6[0] = 6
print(list5)  # [2, 4, 7, 98, 0]
print(list6)  # [6, 4, 7]

# list1 = [1, 3, 2, 5] list2 = list1 list3 = list1[:] list1, list2, list3 之间的关系 ？
'''
相同：值都是一样的， 都是 [1, 3, 2, 5]
不同：list1 和 list2 因为是赋值操作 = ，说明 list1 和 list2 是指向同一个地址的
     list1 is list 2 --> True
     list1 与 list3 使用的是切片，类似是拷贝，list3 是一个新的地址，也是存放 [1, 3, 2, 5]
     list1 与 list3 的地址是不一样的
'''

print("="*50)
list3 = [1, 2, 3, 5]
list4 = list3
print(id(list3))# 2101381537856
print(id(list4))# 2101381537856
