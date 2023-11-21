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
                    append()  # 列表的末位追加
                    extend()  #
                    insert()

                删除：
                    remove
                    pop()
                    clear()
                    del 列表[下标]

                修改：

                查找：

            4. 列表可以支持的符号
        元组
        集合
        字典

'''
# 复数类型
a = 5.6 + 0.8j
print(type(a))

print(a.real, a.imag)  # 实部和虚部

# 创建一个容器类型： list
cars = []  # 列表可以认为就是一个'停车场'
cars = ['京A0988', '京B0866']  # 有内容的列表，内容的列表不限

score = [99, 88, '0分', True] # 有内容的列表，内容的列表不限

print(cars)
print(score)

# 从列表中获取内容: 支持下标索引
print(cars[0])

print(len(cars))

# 队列： FIFI first in first out

print('='*30)

# 列表也是支持切片的
print(score[:2])  # score [99, 88, '0分', True]    [99, 88]
print(score[1:])  # [88, '0分', True]
print(score[-2])  # 0分

print('='*30)

# 只要是切片就是包前不包后
print(score[::-1])
print(score[-1:-4:-2])  # [True, 88]
print(score[:])  # 从头到尾