# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
time模块：
    。获取当前时间 --- s = time.time()
    。将秒时间转换为本地时间的时间元组 --- st = time.localtime(s)
    。将时间元组转换为字符串格式化形式 --- ss = time.strftime(format, st)
    。思考：常用的时间格式的转换，需要几个步骤呢？
        1. 得到秒的表示   ----  seconds = time.time() 当前时间的秒的表示
        2. 将得到的秒时间转换为元组表示  ---- st = time.localtime(seconds)  ----> tuple
        3. 将元组表示的时间，转换为常见的时间表示格式 ---- time.strftime(format, st)  --> 时间字符串表示
            。# 获取当前时间的秒表示   --- seconds
            。s = time.time()
            。# 将秒表示转换为秒的元组表示 --- seconds tuple
            。st = time.localtime(s)
            。# 将秒的元组表示转为常见格式[秒的字符串格式化表示]  --- string format time
            。ss = time.strftime('%Y-%m-%d %H-%M-%S', st)  # 开发的时候，数据库的时间常用保存格式
            。print(ss)  # 2021-11-17 17-34-59
    。再思考：有没有更加简便的方式呢？ 有！ 用 datetime.now() 一步到位！
    。
    。

'''
import time
import os

# 休息多长时间
# time.sleep(1)

# 返回文件的最后访问时间  --- 返回的是秒
print(os.path.getatime(r'D:\python\lesson-online\14 测试\a.txt'))  # 访问时间  access time
# 返回文件的最后创建时间(windows系统)
print(os.path.getctime(r'D:\python\lesson-online\14 测试\a.txt'))  # 创建时间 create time
# 返回文件的最后修改时间
print(os.path.getmtime(r'D:\python\lesson-online\14 测试\a.txt'))  # 修改时间 modify time

# Return the current time in seconds since the Epoch
print(time.time())  # 1637140508.9401054

mtime = os.path.getmtime(r'D:\python\lesson-online\14 测试\a.txt')
# print(time.localtime(mtime))  # 元组
st = time.localtime(mtime)  # 将时间转为元组形式
# print(st)  # time.struct_time(tm_year=2021, tm_mon=11, tm_mday=17, tm_hour=17, tm_min=0, tm_sec=26, tm_wday=2, tm_yday=321, tm_isdst=0)
print(st.tm_yday)  # 返回年当中第多少天

# Convert a time tuple to a string. e.g. 'Sat Jun 06 16:26:11 1998'
print(time.asctime(st))  # Wed Nov 17 17:00:26 2021

# 思考：如何得到我们常见的时间格式呢？

# Convert a time tuple to a string according to a format specification
print(time.strftime('%Y-%m-%d %H-%M-%S', st))  # str format time
'''
思考：该格式的转换需要几个步骤呢？
1. 得到秒的表示   ----  seconds = time.time() 当前时间的秒的表示
2. 将得到的秒时间转换为元组表示  ---- st = time.localtime(seconds)  ----> tuple
3. 将元组表示的时间，转换为常见的时间表示格式 ---- time.strftime(format, st)  --> 时间字符串表示

'''
# 获取当前时间的秒表示   --- seconds
s = time.time()
# 将秒表示转换为秒的元组表示 --- seconds tuple
st = time.localtime(s)
# 将秒的元组表示转为常见格式[秒的字符串格式化表示]  --- string format time
ss = time.strftime('%Y-%m-%d %H-%M-%S', st)  # 开发的时候，数据库的时间常用保存格式
print(ss)  # 2021-11-17 17-34-59
