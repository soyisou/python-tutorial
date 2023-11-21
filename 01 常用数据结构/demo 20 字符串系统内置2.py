# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
"""
    字符串内置的函数：
    1. isupper()  # 判断是否是大写
    2. islower()  # 判断是否是小写
    3. isalpha()  # 是否字符串中只有字母组成， 如果是则返回T rue，否则返回 False  [alphabetic]
    4. isdigit()  # 是否是纯数字，如果是则返回 True，否则返回 False
    5. startswith()  # 是否以指定的内容开头
    6. endswith()  # 是否以指定的内容结尾

    系统函数：
    len(s) --> int

    对齐与格式：---> 了解即可
    center()  # 居中
    ljust()  # 左对齐
    rjust()  # 右对齐

    格式化：
    format()
    %

    去除空格
    strip()  # 去除字符串左右两边的空格  ***
    lstrip()  # 去除字符串左边的空格
    rstrip()  # 去除字符串右边的空格

"""

s = 'Hello'
d = '123456'
print(s.isupper(), s.islower(), s.isalpha(), d.isdigit())

# 纯数字 长度： 5-10 不能以 0 开始
# print(qq.isdigit())
# print(5 <= len(qq) <= 10)  # 在 python 中是允许连着写的
# print(qq.startswith('0'))  # 是否以 0 开头

# 判断 QQ号码是否合法
# qq = input('qq号码:')
# if qq.isdigit() and 5 <= len(qq) <= 10 and not qq.startswith('0'):
#     print('qq号码正确！')
# else:
#     print('qq号码错误！')

# 文件上传:只能上传图片（jpg，png，gif）
# file = input('上传路径：')  # C:\Users\LJM\Pictures\照片\证件照.jpg
# if file.endswith('.jpg') or file.endswith('.png') or file.endswith('gif'):
#     print('是图片格式的允许上传')
# else:
#     print('只能上传是图片(jpg，pgn，gif)')

# 对齐相关

# s = '香港暴乱, 不法分子闹事'
# l = s.ljust(50)
# r = s.rjust(50)
# r = s.rjust(50)
# print(l)
# print(s)
# print(r)

name = '蔡徐坤'
age = 22
gender = '男'

print('00后很喜欢的明星是：', name)  # 有空格
# 方法一
print('00后很喜欢的明星是:{}, 今年{}岁, 性别:{}'.format(name, age, gender))
# 方法二 --- 不写默认按顺序
print('00后很喜欢的明星是:{0}, 今年{1}岁, 性别:{2}'.format(name, age, gender))
# 方法三
print('00后很喜欢的明星是:{name}, 今年{age}岁, 性别:{gender}'.format(name=name, age=age, gender=gender))

money = 5.99489

print('我有钱，现在有:{}元'.format(money))  # 我有钱，现在有:5.99489元
print('我有钱，现在有:{:.2f}元'.format(money))  # 保留两位, 我有钱， 现在有:5.99元
print('我有钱，现在有:{:.0f}元'.format(money))  # 不带小数, 我有钱， 现在有:6元(四舍五入)

# 将数据放进数据库之前，一定要将数据两侧的空格去掉，怎么办？
s = ' abc '
# 去除右边的空格
s = s.rstrip()
print(s)

# 去除左边的空格
s = s.lstrip()
print(s)

# 去除中间的空格
s = s.strip()
print(s)