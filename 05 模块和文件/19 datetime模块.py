# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
datetime模块
    4个类：
        。date 日期
        。time 时间
        。timedelta 时间差
        。datetime 日期时间
'''
from datetime import datetime

# 往数据库里面存的时候，我们通常用datetime.now() 而不是用time()的三步法！太繁琐了！（以下二者记住其一即可）
print(datetime.now())  # 2021-11-17 18:13:05.078133
print(datetime.today())  # 2021-11-17 18:13:05.078134

# 有兴趣的话可以了解时区时间的应用
print(datetime.utcnow())  # 2021-11-17 10:13:05.078133 有个时区的差值，取的不是我们的时区 Asia/Shanghai

# 补充
import sys  # 系统库
# 返回当前系统的版本
print(sys.version_info)  # sys.version_info(major=3, minor=7, micro=11, releaselevel='final', serial=0)
print(sys.version)  # 3.7.11 (default, Jul 27 2021, 09:42:29) [MSC v.1916 64 bit (AMD64)]

# 表示搜索路径
print(sys.path)  # ['D:\\python\\lesson-online\\05 模块和文件', 'D:\\python\\lesson-online', 'D:\\python\\lesson-online\\05 模块和文件', 'D:\\Pycharm\\PyCharm 2020.1.2\\plugins\\python\\helpers\\pycharm_display', 'D:\\Anaconda3\\envs\\Pytorch\\python37.zip', 'D:\\Anaconda3\\envs\\Pytorch\\DLLs', 'D:\\Anaconda3\\envs\\Pytorch\\lib', 'D:\\Anaconda3\\envs\\Pytorch', 'C:\\Users\\LJM\\AppData\\Roaming\\Python\\Python37\\site-packages', 'D:\\Anaconda3\\envs\\Pytorch\\lib\\site-packages', 'D:\\Pycharm\\PyCharm 2020.1.2\\plugins\\python\\helpers\\pycharm_matplotlib_backend']

# 思考：能够自定义搜索路径的优先顺序？ 可以
# sys.path.insert(0, 'D:\\python\\lesson-online\\05 模块和文件\\book')  # 为什么可以调用insert? 因为sys.path是列表嘛！
# print(sys.path)

# datetime类的使用
dt = datetime(2019, 8, 12)  # 年月日
print(dt.year)

print('=' * 50)

# 了解
from datetime import date

# 返回当前时间 年-月-日
print(date.today())  # 2021-11-17

print('=' * 50)

# 了解即可
from datetime import time

t = time(11, 52, 48)
print(time.hour)  # <attribute 'hour' of 'datetime.time' objects>

print('=' * 50)

# Represent the difference between two datetime objects
from datetime import timedelta

# 思考：时间差什么时候会用？
'''
缓存 redis  --> 机制：键值对，即 key: value
会话 session 

{’001': user, '002': user, '003': user ···} 
如果用户非常多的话，内存就会满的···
其中某些人不用了，就可以释放内存···
当在保存的时候，就会设置时间差，超过时间自动过期，就会从键值对中删除···
因此，就会用到时间差，即当前时间，往后推多少时间···
'''
import time

# t1 = time.time()

# 当前时间
dt = datetime.now()  # 2021-11-17 18:43:36.445988
# print(dt)

# 设置时间差 ---- minute
tdt = timedelta(minutes=30)  # 设置时间差为30min   0:30:00
# print(tdt)

# 过期时间
print(dt + tdt)  # 2021-11-17 19:13:36.445988

# 设置时间差 ---- days
tdt = timedelta(days=1)
print(dt + tdt)  # 2021-11-18 19:13:36.445988

# 思考：能减时间么？  可以！
tdt = timedelta(days=-1)
print(dt + tdt)  # 2021-11-16 19:13:36.445988

'''
日历相关
'''

import calendar

# 得到2021年的日历
# print(calendar.calendar(2021))
# 多加一个参数，也是得到2021年的日历，只不过是日历间距大了
# print(calendar.calendar(2021, 5))

# 思考：怎么得到月份呢？  用calendar.month()
print(calendar.month(2021, 11))  # 年月

# 返回星期几
print(calendar.weekday(2021, 11, 18))  # 年月日  3 注意：从0开始的，0代表星期一


