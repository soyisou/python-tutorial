# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
raise = 自定义异常
ValueError
自定义异常
    。系统异常不能满足个人需求
    。自定义异常是异常的一种
    。格式：xxxError
    。自定义异常其实很简单
        。step1: 自定义异常
            class xxxError(Exception):  # 只要继承Exception，若不定义，底层统统推抛给 Exception
                def __init__(self, *args, **kwargs)  # 不写也是可以的
                    pass

        。step2: 使用异常：
            raise xxxError(提示信息)

        。step3: 处理异常
            try:
                有可能出现异常的代码
            except 类型:  # 打印异常 except Exception as err
                ·异常处理

异常两大部分
    。处理异常
        。try ··· except
        。try ··· except ··· else
        。try ··· except ··· else finally
    。自定义异常
        。自定义异常 + raise [raise用于抛出异常对象]

注意：如果不处理，就会出现红色的一片···
'''
# 自定义用户名异常
class UserNameError(Exception):  # 所有的异常都需要继承Exception
    pass
    # def __init__(self, *args, **kwargs):  # real signature unknown
    #     pass

    # 若加上该函数，则结果为： TypeError: exceptions must derive from BaseException
    # @staticmethod
    # def __new__(*args, **kwargs):  # real signature unknown
    #     """ Create and return a new object.  See help(type) for accurate signature. """
    #     pass

# 自定义密码异常
class PassWordError(Exception):  # 里面什么都不写，也是没有关系的，都有父类处理了
    pass
    # def __init__(self, *args, **kwargs):  # real signature unknown
    #     pass

# 注册
def register():
    uername = input('请输入用户名：')
    # 名字长度>=6,不能数字开头   '2'
    if len(uername) < 6 or uername[0].isdigit():
        # 用户名定义出错 --- 之前是系统帮我们往外扔，但是自定义异常是我们自定义的，因此需要我们自己往外扔
        raise UserNameError('用户名格式错误！')
    else:
        print('用户名合法')
        password = input('请输入用户名：')
        if 10 >- len(password) >= 6:
            print('注册成功！')
        else:
            raise PassWordError('密码格式错误！')

# 调用函数，进行异常处理
try:
    register()
except Exception as err:
    print(err)  # 用户名格式错误
