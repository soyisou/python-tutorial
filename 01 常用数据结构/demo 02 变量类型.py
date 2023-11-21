# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

"""
变量的类型:
    (1)系统类型:
        str：符号问题：单引号，双引号，三引号(保留格式)  转义字符 + r结合使用
        int：整型 10 9
        float：python没有 double，只有 float 类型
        bool： 只有两种要么是 True, 要么是 False，而且首字母均是大写
        byte: 字节型，b'内容', 即字符串前面挂一个 b
        list
        tuple
        set
        dict
    (2)自定义类型:
"""

name = '孙杨'
name1 = "傅园慧"

# 保留格式  即在字符串里面的格式如何，出来的格式亦如何
msg = '''1. 孙杨获得游泳冠军
2. 傅园慧第一场出局
'''
# 保留格式  即在字符串里面的格式如何，打印出来的格式亦如何
# 多了一个空行，即先输出一个空行
msg = '''
1. 孙杨获得游泳冠军
2. 傅园慧第一场出局
'''

print(type(name), type(name1), type(msg))
print(name)
print(name1)
print(msg)

"""
单双引号：
    内层如果是双引号的话，外层就用单引号
    内层如果是单引号的话，外层就用双引号
"""

"""
预定义的转义字符：
\n 
\t 
\r 
\' 
\"
\\
结合：r‘内容’ raw (原始的)
"""
ls1 = 'hello \n world !'
print(ls1)

ls1 = 'hello \\ world !' # 如果是一根 \ 的话就会有一定的危险性 如，ls1 = 'hello\table'， \t会结合
print(ls1)

ls1 = r'hello \\ world !' # 打印结果：hello \\ world !
print(ls1)

# int 型变量
age = 21
print(type(age),age)

# 浮点型
money = 99.9
print(type(money), money)

# 布尔型
flag = True
print(type(flag), flag)

# 字节型
b1 = b'hello'
print(type(b1), b1)