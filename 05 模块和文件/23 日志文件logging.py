# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
日志文件：
    。什么是日志文件？当我们的项目上线后，就不能用 print了，print适用于我们在开发阶段的时候往外打印。
    。比如，用户登录出现错误的时候，错误信息就会存放在日志文件里。

    。日志级别：
    _nameToLevel = {
        'CRITICAL': CRITICAL,  # 严重警告
        'FATAL': FATAL,  # 致命的
        'ERROR': ERROR,  # 错误
        'WARN': WARNING,  # 警告
        'WARNING': WARNING,  # 警告
        'INFO': INFO,
        'DEBUG': DEBUG,
        'NOTSET': NOTSET,  # 不管设置





    }

    。程序员写代码，最关注的就是日志文件了，因为里面能够看出来很多的信息。
'''
import logging
'''
可以认为logger是一个大总管[大哥]，它的下面可以管理很多个hander[小弟]
'''
# 1. 创建日志对象 --- getLogger()
logger = logging.getLogger()  # 可认为是日志管理员

# 2. 设置日志对象级别
logger.setLevel(logging.ERROR)  # 参数必须为整型或者字符串类型

# 3. 创建一个handler对象 [处理者]
file = 'log.txt'
handler = logging.FileHandler(file)
handler.setLevel(logging.ERROR)

# 4. 设置格式化程序，即创建一个Formatter对象
fmt = logging.Formatter('%(asctime)s-%(module)s-%(filename)s[%(lineno)d]-%(levelname)s:%(message)s')
handler.setFormatter(fmt)

# 5. 将hander对象交给logger对象管理
logger.addHandler(handler)
# logger.addHandler(handler1)  # 如果再有handler,则再加入logger对象即可

def func():
    try:
        number = int(input('请输入一个数字：'))
        for i in range(number):
            print('----> ', i)
    except:  # 如出错，则有logger对象管理
        logger.error('输入的不是一个数字！')
    finally:
        print('-------over-------')

func()
'''
当输入：dafdg
log.txt文件出现：
2021-11-18 23:06:11,962-23 日志文件logging-23 日志文件logging.py[50]-ERROR:输入的不是一个数字！
'''