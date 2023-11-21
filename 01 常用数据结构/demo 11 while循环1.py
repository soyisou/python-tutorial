# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
"""
循环：
    1. 银行：
        用户名和密码 --》 3次
    2. 产生银行卡号随机数
    3. ···

结构：
    while
    格式：
    while 条件：
        条件成立，执行的语句部分


    for

"""
# 验证用户名与密码是否正确，如果正确则输出登录成功，否则用户或者密码有误
# 声明变量

# while 语句
cnt = 3
while cnt:
    username = input('输入用户名：')
    password = input('输入密码：')

    # 变量和运算符构成判断条件 (admin, 123456)
    if username == 'admin' and password == '123456':
        print('登录成功！')
        cnt = 3
        break  # 跳出整个循环结构
    else:
        print('用户名或者密码有误！')
    cnt -= 1
    if cnt == 0:
        print('密码输错已超过3次，您的账户被锁定！')

"""
# while···else···语句

cnt = 0
while cnt <= 3:
    username = input('输入用户名：')
    password = input('输入密码：')

    # 变量和运算符构成判断条件 (admin, 123456)
    if username == 'admin' and password == '123456':
        print('登录成功！')
        cnt = 3
        break  # 跳出整个循环结构
    else:
        print('用户名或者密码有误！')
    cnt += 1
else:
    print('密码输错已超过3次，您的账户被锁定！')
"""

