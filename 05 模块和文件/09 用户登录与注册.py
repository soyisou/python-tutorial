# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
持久化用户数据，实现登录和注册

open(file, mode, encoding)   ---> 流
write  输出
read   输入

with open(···) as rstream:
    pass

with open(···) as wstream:
    pass
'''

class User:
    def __init__(self):
        self.username = None
        self.password = None

    def __str__(self):
        return self.username

    def login(self):
        self.username = input('用户名:')
        self.password = input('密码:')
        if self.username and self.password:
            with open('users.txt', 'r', encoding='utf-8') as rstream:
                users = rstream.readlines()  # 结果为列表 ['张三 123\n', 'admin 123456\n']
                print(users)
                for user in users:  # '张三‘ '123'\n
                    users = user.replace('\n', '')
                    ulist = users.split(' ')  # 得到用户名和密码
                    if self.username == ulist[0]  and self.password == ulist[1]:
                        print('登录成功！')
                        return False
                else:
                    print('登录失败！用户名或者密码输入错误！')
                    return True
        return True

    def register(self):
        self.username = input('用户名:')
        self.password = input('密码:')
        if self.username and self.password:
            with open('users.txt', 'a', encoding='utf-8') as wstream:
                wstream.write('{} {}\n'.format(self.username, self.password))
                print('注册成功！')
        else:
            print('用户名或者密码不能为空！')

def main():  # 作为一个入口
    flag = True
    u = User()
    u.register()
    while flag:
        print('-' * 25 + '用户登录' + '-' * 25)
        flag = u.login()

if __name__ == '__main__':
    main()

