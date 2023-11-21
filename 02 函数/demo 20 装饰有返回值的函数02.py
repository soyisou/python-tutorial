# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
使用装饰器进行用户的登录验证
注：python装饰器(decorator)在实现的时候，被装饰后的函数其实已经是另外一个函数了(函数名等函数属性发生了改变)
'''
islogin = False  # 是否登录成功

def login_required(func):
    def wrapper(*args, **kwargs):
        global islogin
        if islogin:  # 已经登录
            func(*args, **kwargs)  # func = buy_ticket
        else:  # 未登录
            print('用户还没有登录，请登录！')
            r = login()  # 登录
            if r:  # 登录成功，买票
                func(*args, **kwargs)
            else:  # 登录未成功，买票失败
                print('密码输入错误！')
    return wrapper

def login():
    global islogin
    username = input('输入用户名：')
    password = input('输入密码：')
    if username == 'admin' and password == '123':
        islogin = True
        return islogin
    return islogin

@login_required
def buy_ticket():
    ticket = {'中影星美水城店':('哪吒', ['11:35 1号厅', '12:35 3号厅', '14:08 1号厅'])}
    for key, value in ticket.items():
        print('影院：', key)
        print('播放的电影是：', value[0])
        print('播放时间如下：')
        for i in value[1]:
            print('-->', i)

login()  # 先进行登录
buy_ticket()  # 买票