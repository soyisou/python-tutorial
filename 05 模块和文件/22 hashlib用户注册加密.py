# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
用户注册和登录
    。以后所有的原则就是，对密码进行加密保存
    。验证的时候，将用户密码与数据库中加密的密码进行匹配
'''
import csv
import hashlib

def register():
    # 明文
    username = input('用户名：')
    password = input('密码：')

    user = []
    # 密码加密
    user.append(username)
    user.append(hashlib.sha256(password.encode('utf-8')).hexdigest())

    with open('users.csv', 'a', newline='', encoding='utf-8') as ws:  # 创建文件对象
        csv_writer = csv.writer(ws)  # 创建csv对象
        csv_writer.writerow(user)  # 写入
    print('注册成功！')

def login():
    # 明文
    username = input('用户名：')
    password = input('密码：')

    # 加密
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    with open('users.csv', 'r', encoding='utf-8') as rs:
        csv_reader = csv.reader(rs)
        for user in csv_reader:
            if username == user[0] and password == user[1]:
                print('登录成功！')
                break
        else:
            print('用户名或者密码有误！')

def show():
    with open('users.csv', 'r', encoding='utf-8') as rs:
        csv_reader = csv.reader(rs)
        for user in csv_reader:
            print(user)

# register()
login()
# show()

# base64  --- hashlib里面是没有base64的