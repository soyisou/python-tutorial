# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
match
fullmatch
seach
    。若在字符串中找到匹配的，则不会继续查找了，如果想要继续找下去，怎么办呢？  用 findall
findall

特殊字符：
    '.' 任意字符除了换行
    []表示的是一个范围
        。如果比较短 [xyz] 表示或者是x或者是y或者是z
        。如果比较长 [a-zA-Z] 表示 a-z或者 A-Z之间的任意一个字符
        。如果有数字 [0-9] 表示 0-9 之间的任意一个数字

        # 思考：如何表示多个字母或者数字呢？
    * 表示 >= 0 个字符
    + 表示 >= 1 个字符
    ？ 表示 0 或 1 个字符

    注意：只要用以上内容，即在写正则表达式的时候，要在前面增加 r, 保证里面的内容是正则内容！
'''

# a_b anb atb aqb ···
s = 'worldaobhelllo' # a8b a&b ··· 均可

import re

m_obj = re.search('a.b', s)  # '.'可以表示任意字符，除了换行符
if m_obj:
    print(m_obj.group())  # aob

else:
    print('没有找到！')

print('=' * 50)
# []表示的是一个范围，[xyz]或者是x或者是y或者是z
m_obj = re.search('a[a-z]b', s)  # [a-z] 表示 a-z中的任意字符
# m_obj = re.search('a[opq]b', s)  # [opq] 表示opq中的任意字符
# m_obj = re.search('a[opq]b', s, re.I)  # [opq] 表示opq中的任意字符 [忽略大小写]
if m_obj:
    print(m_obj.group())  # aob

else:
    print('没有找到！')


print('=' * 50)
s = 'worldaxbhelllo' # a8b a&b ··· 均可
# m_obj = re.search('a[xx]?b', s)  # [a-z]? 表示 a-z中的任意字符, 且要么不匹配，要么匹配一次 -- 没有找到！
# m_obj = re.search('a[x]+b', s)  # [a-z]+ 表示 a-z中的任意字符, 且至少有一个  -- axb
m_obj = re.search('a[xx]+b', s)  # [a-z]+ 表示 a-z中的任意字符, 且至少有一个  -- axb
if m_obj:
    print(m_obj.group())  # aob

else:
    print('没有找到！')


print('=' * 50)
s = 'worldaxxubhelllo' # a8b a&b ··· 均可
# m_obj = re.search('a[xx]+b', s)  # [a-z] 表示 a-z中的任意字符, 且至少有一个  -- 没有找到！
m_obj = re.search('a[xu]+b', s)  # [a-z] 表示 a-z中的任意字符, 且至少有一个  -- axxub
# m_obj = re.search('a[xxu]*b', s)  # [a-z] 表示 a-z中的任意字符, 且至少有一个  -- axxub
if m_obj:
    print(m_obj.group())  # aob

else:
    print('没有找到！')

# 思考：如果两头是数字，中间是字母（可以是多个，但至少要有一个）  --- 1daf9