# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
os模块：
    。获取绝对路径 -- os.path.abspath('student')
    。判断给的路径是否是一个绝对路径 -- os.path.isabs('student')
    。判断是否是文件 -- os.path.isfile('student')
    。判断是否是文件夹 -- os.path.isfile('student')
    。判断是否存在文件夹或者文件 -- os.path.exists('student')
    。文件的拼接 -- os.path.join(r'D:\python\lesson-online\14 测试', 'a.txt')
    。文件的分割 [将文件名和文件前边的内容切割] -- os.path.split(r'D:\python\lesson-online\14 测试\a.txt')
    。思考：如何利用split()获取文件名呢？
        path = r'D:\python\lesson-online\14 测试\a.txt'
        print(os.path.split(path))  # ('D:\\python\\lesson-online\\14 测试', 'a.txt')
        print(os.path.split(path)[1])  # a.txt  --- 获取文件名！
    。获取文件大小[单位字节] -- os.path.getsize(r'D:\python\lesson-online\14 测试\a.txt')
    。返回文件的最后访问时间[返回的是秒] -- os.path.getatime(r'D:\python\lesson-online\14 测试\a.txt')  # 访问时间  access time
    。返回文件的最后创建时间(windows系统) -- os.path.getctime(r'D:\python\lesson-online\14 测试\a.txt')  # 创建时间 create time
    。返回文件的最后修改时间 -- os.path.getmtime(r'D:\python\lesson-online\14 测试\a.txt')  # 修改时间 modify time

'''
import os

# 获取绝对路径
print(os.path.abspath('student'))  # D:\python\lesson-online\05 模块和文件\student

# 判断给的路径是否是一个绝对路径
print(os.path.isabs('student'))  # False

# 判断是否是文件
print(os.path.isfile('student'))  # False

# 判断是否是文件夹
print(os.path.isdir('student'))  # True

# 判断是否存在文件夹或者文件
print(os.path.exists('student'))  # True

# 文件的拼接
print(os.path.join(r'D:\python\lesson-online\14 测试', 'a.txt'))  # D:\python\lesson-online\14 测试\a.txt

# 文件的分割 --- 将文件名和文件前边的内容切割
print(os.path.split(r'D:\python\lesson-online\14 测试\a.txt'))  # ('D:\\python\\lesson-online\\14 测试', 'a.txt')
# 思考：如何利用split()获取文件名呢？
path = r'D:\python\lesson-online\14 测试\a.txt'
print(os.path.split(path))  # ('D:\\python\\lesson-online\\14 测试', 'a.txt')
print(os.path.split(path)[1])  # a.txt  --- 获取文件名！

# 获取文件大小
print(os.path.getsize(r'D:\python\lesson-online\14 测试\a.txt'))  # 29   -- 单位字节

# 返回文件的最后访问时间  --- 返回的是秒
print(os.path.getatime(r'D:\python\lesson-online\14 测试\a.txt'))  # 访问时间  access time
# 返回文件的最后创建时间(windows系统)
print(os.path.getctime(r'D:\python\lesson-online\14 测试\a.txt'))  # 创建时间 create time
# 返回文件的最后修改时间
print(os.path.getmtime(r'D:\python\lesson-online\14 测试\a.txt'))  # 修改时间 modify time

# 思考：已知的是秒，怎么获取具体时间呢？请看下一节！


