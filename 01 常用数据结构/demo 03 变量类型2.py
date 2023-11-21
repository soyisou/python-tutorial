# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

"""
1.  类型：
    str：符号问题：单引号，双引号，三引号(保留格式)  转义字符 + r结合使用
    int：整型 10 9
    float：python没有 double，只有 float 类型
    bool： 只有两种要么是 True, 要么是 False，而且首字母均是大写
    byte: 字节型，b'内容', 即字符串前面挂一个 b

    python 独有的类型 container:容器
    list:  类型 []
    tuple：元祖 ()
    set：  集合 {} 底层由字典构成,即由字典转化而成
    dict：字典 {}

2.  格式化 快捷键：
        default 快捷键：Ctrl + alt + L
        eclipse 快捷键：ctrl + shift + F

3. 运算符：
    算术运算符
    赋值运算符
    关系运算符
    逻辑运算符
    位运算符
    三目运算符

"""
number = 10
print(type(number), number)

# python PEP8 编码规范

# 列表
scores = [100, 98, 97]
print(type(scores), scores)

# 元组 允许有重复元素
scores = (1, 4, 4)
print(type(scores), scores)

# 集合 不允许有重复元素
scores = {1, 3, 5, 7, 3}
print(type(scores), scores)

# 字典 键值对
scores = {'张三': 100, '李四': 99}
print(type(scores), scores)
