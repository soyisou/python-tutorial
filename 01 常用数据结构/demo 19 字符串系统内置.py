# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
字符串：
1. 声明 '' "" 三引号
2. 字符串的下标：从0开始到len(s) - 1
    s[-1] s[2]
    注：len = 5 -->s[6] out of range
3. 切片 --> 默认从左到右
    s[start:stop:step]
    s[start]  # 默认从头到尾
    s[:stop]  # 默认从0开始到 stop 结束
    s[start:stop]  # 默认从 start 开始到 stop - 1 结束
    s[start:stop:step]  # step 步长
    s[start:stop:负数]  # 反方向,从右到左
4. 方法：系统内置的方法
    查找：
    index, find, rfind
    index 和 find 都是返回内容的下标位置（从左向右查找）
    index : 没有找到，报错
    find  : 没有找到，返回 -1
    rfind(right find)：（从右向左查找）没有找到，返回 -1
    rindex(right index):没有找到，报错

    替换：
    replace 返回了新替换旧的复制的一个字符串
    replace(old, new, count)  # 有多少个替换多少个

    分割：
    split(分隔符，[最大切割次数]） 返回的是分割后的一个列表

    转换：
    upper()  # 转大写
    lower()  # 转小写
    title()  # 每个单词的首字母大写
    capitalize()  # 仅仅句子的第一个首字母大写
'''
s = r'D:\学习\综合实践\项目练习.txt'
index = s.rfind('\\')  # 需要转义字符
print(s[index + 1:])  # 项目练习

# 有多少个替换多少个
s = 'hello 帅哥, hi 帅哥'
s = s.replace('帅哥', '美女')  # replace 返回了新替换旧的复制的一个字符串 hello 美女, hi 美女
print(s)

# 敏感词汇
s = '苍井空很漂亮'
s = s.replace('苍井空', '***')
print(s)

# split(分隔符，[最大切割次数]） 返回的是分割后的一个列表，只要遇到分隔符就切割
s = r'D:\学习\综合实践\项目练习.txt'
list1 = s.split('\\')
print(list1)

# 大小写
# 验证码
import random

code = ''
base_str = 'fadgaga6546DAGAfdaDFRET4436'
for i in range(4):
    r = random.randint(0, len(base_str) - 1)  # 左闭右闭
    code += base_str[r]
print('验证码是：', code)

# in_code = input('输入验证码：')

# 验证码验证
# if code.lower() == in_code.lower():  # 将所有字母都转成小写(lower)或小写(upper)
#     print("验证码输入正确！")

# 大写
s = 'hello'
s = s.upper()  # 转成大写
print(s)

# title() capitalize()
s = 'yuxin is a handsome boy !'
s = s.title()
print(s)

# capitalize() 仅句子的第一个单词的首字母大写
s = 'yuxin is a handsome boy !'
s = s.capitalize()
print(s)