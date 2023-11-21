# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
{'ergou': {'password': '123', 'status': False, 'time': '2019-07-09'},
'songsong': {'password': '123', 'status': False, 'time': '2019-07-09'},
'xiaohua': {'password': '123', 'status': False, 'time': '2019-07-09'},
}
1. 将此数据保存到一个 user.txt文件中
2. 创建用户对象有用户名和密码、状态和登录时间，动作有：登录、退出、发表评论
3. 如果用户登录成功则状态就是 True，并记录登录时间
4. 如果用户的 status的状态是 True，则用户可以发布评论
5. 用户退出则改变 status的值为 False

具体功能：
    。登录
    。登出
    。发表评论
'''
import pickle
from datetime import datetime

class User:
    def __init__(self):
        self.username = None  # 用户名
        self.password = None  # 密码
        self.status = None  # 状态
        self.login_time = None  # 登录时间

    # 用户登录
    def login(self, username, password):
        # 作用1：用于辨别用户名和密码是否匹配
        user_flag = False  # 作用2：用户状态是否发生更改 用户后期将更新的数据写入本地磁盘
        file_flag = True
        user_list = []  # 用户列表 因为此时没有用数据库，更改是比较麻烦的
        # 异常处理  --- 一定会读到文件最后，异常一定会出现！
        try:
            with open('users.txt', 'rb') as rs:
                # 文件打开正常
                file_flag = False
                # 循环遍历文件中的user对象
                while True:  # 由于读取到磁盘文件最后会报出异常，因此while后的语句一定不会执行
                    user = pickle.load(rs)  # 从文件中顺次加载一个user对象
                    user_list.append(user)  # 将文件中的用户对象先存入user_list中，便于后续处理
                    # 如果用户名和密码相符合
                    if user.username == username and user.password == password:
                        if user.status:  # 用户已登录
                            print('此用户已登录！')
                            # 设置 self 的登录时间
                            self.login_time = user.login_time
                            break  # 退出while循环，不再遍历后面的数据
                        else:  # 用户名和密码输入正确
                            print('登录成功！')
                            user.status = True  # 修改用户登录状态
                            # 思考：此时还没有写回文件，怎么把更新的数据写回文件呢？
                            user_flag = True  # 表示用户状态发生了修改
                            # 设置 self 的登录时间
                            self.login_time = datetime.now()  # 取到当前时间，日期和时间都有

                            # 思考：能否在此处加break ?  不能，因为需要讲所有用户信息重新写入文件，会遗漏用户

                        # 设置共用的 self信息
                        self.username = username
                        self.password = password
                        self.status = True

        except Exception as err:
            # 判断文件操作是否有误
            if file_flag:
                print(err)  # 报出文件异常
                return  # 结束函数

            # 用户状态发生了更改
            if user_flag:  # 不用数据库，确实比较麻烦
                with open('users.txt', 'wb') as ws:
                    for user in user_list:
                        # print(user)  # 测试
                        pickle.dump(user, ws)
            else:  # user_flag 为 Flase
                print('登录失败，用户名或者密码有误！')

    # 用户登出
    def logout(self, username, password):
        if self.status:
            self.status = False
            # 将修改过的信息，写入磁盘

    # 发表文章
    def publish_comment(self):
        if self.status:
            print('发表文章！')

    # 用户注册
    def register(self):
        pass

    # 返回对象信息
    def __str__(self):
        return self.username + '\t' + self.password

def main():
    #
    users = {'ergou': {'password': '123', 'status': False, 'login_time': '2019-07-09'},
             'songsong': {'password': '456', 'status': False, 'login_time': '2019-08-09'},
             'xiaohua': {'password': '789', 'status': False, 'login_time': '2018-06-09'}
            }

    users_obj = []
    for key, value in users.items():
        u = User()
        u.username = key
        for k1, v1 in value.items():
            if k1 == 'password':
                u.password = v1
            elif k1 == 'status':
                u.status = v1
            elif k1 == 'login_time':
                u.login_time = v1

        users_obj.append(u)

    # 保存用户对象
    with open('users.txt', 'wb') as ws:
        for user in users_obj:
            pickle.dump(user, ws)

    # print('所有用户信息保存成功！')





if __name__ == '__main__':
    main()

    # 登录
    u = User()
    # 登录
    u.login('xiaohua', '789')
    # 发表文章
    u.publish_comment()
