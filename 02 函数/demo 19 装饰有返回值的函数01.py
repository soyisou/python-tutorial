# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
装饰有返回值的函数, 装饰器的内层函数也要有返回值，从而保证装饰后的函数与原函数保持一致性
注：python装饰器(decorator)在实现的时候，被装饰后的函数其实已经是另外一个函数了(函数名等函数属性发生了改变)
'''
flag = False

# 定义一个装饰器函数
def decorator(func):
    def wrapper(*args, **kwargs):  # 可以把 wrapper <==> islogin
        print('---->进行用户的登录验证')
        r = func(*args, **kwargs)  # 被装饰的函数如果有返回值，则
        if r:
            return 'success'
        else:
            return 'failure'
    return wrapper

def login():
    global flag
    username = input('输入用户名：')
    password = input('输入密码：')
    if username == 'admin' and password == '123':
        flag = True

@decorator
def islogin():
    if flag:
        return True
    else:
        return False

# 调用 login 函数
login()

# 调用 islogin函数
r = islogin()
print(r)