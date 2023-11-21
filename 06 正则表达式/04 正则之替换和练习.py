# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
\w 表示字母、数字、下划线
{n,}  >=n
{n} 必须是n位
{3,4} 3-4位
\d
\w
\b

re模块中的：
    。sub(pattern, rep1, str)替换

注意：只要用以上内容，即在写正则表达式的时候，要在前面增加 r, 保证里面的内容是正则内容！

验证用户名：可以是字母、数字、下划线，不能是数字或者下划线开头，用户名长度必须是6位以上
手机号验证：1开头，可以是13/15/18XXX··· 11位
座机：区号-电话号码  区号必须是3或者4位，电话号码是8位数字
已知一句话：'I am a good boy, a handsome boy', 提取这句话中的所有单词
'''
# 思考1：如何验证用户名？可以是字母、数字、下划线，不能是数字或者下划线开头，而且用户名长度必须6位以上！
import re

# username = input('输入用户名：')
# match_obj = re.search('^[a-z]\w{5,}$', username, re.I)
# if match_obj:
#     print('用户名合法！')
# else:
#     print('用户名不合法！')

# 思考2：如何验证手机号码？1开头，可以是13/15/18XXX··· 11位
# phone = input('输入手机号码：')
# match_obj = re.search('^1[3,5,8]\d{9}$', phone)
# if match_obj:
#     print('手机号合法！')
# else:
#     print('手机号不合法！')

# 思考3：如何验证座机号呢？区号-电话号码  区号必须是3或者4位，电话号码是8位数字
# tel = input('输入座机号码：')
# match_obj = re.fullmatch('\d{3,4}-\d{8}', tel)
# if match_obj:
#     print('座机号码合法！')
# else:
#     print('座机号码不合法！')

# 思考4：如何提取单词呢？已知一句话：'I am a good boy, a handsome boy', 提取这句话中的所有单词
s = 'I am a good boy, a handsome boy'
words = re.findall(r'[a-z]+\b', s, re.I)  # + 一个以上, 思考：为什么要加r?
print(words)


# \s space
s = ' am    a    good     boy '
s1 = s.replace(' ', '#')
print(s1)  # #am####a####good#####boy#

# 思考5：加入多个空格，也只用一个'#'替换，如何用正则处理呢？
s = re.sub(r'\s+','#', s)  # sun: 替换
print(s)
