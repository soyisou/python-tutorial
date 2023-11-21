# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
贪婪与非贪婪：
    。只要看到 +、*、？后面有？都是将贪婪变成非贪婪的！
'''
import re

s = '<div class="breadcrumb"><a href="http://www.baidu.com">詹姆斯</a></div>'  # div是一个块级标签，而里面的是行级标签

# 命名的方式(?P<out>) (?P<inner>)
# http://image.baidu.com/star/page

m = re.fullmatch(r'<(?P<outer>.+) class="breadcrumb"><(?P<inner>.+) href="http://www.baidu.com">.+</(?P=inner)></(?P=outer)>', s)
print(m.group(1))
print(m.group(2))

print('=' * 50)
# 贪婪与非贪婪：
'''
只要看到 +、*、？后面有？都是将贪婪变成非贪婪的！
'''
s = 'abbbbbbbc'
match_obj = re.match('ab+', s)  # 贪婪模式，+ 指b尽量有多个，有多少匹配多少
print(match_obj.group())  # abbbbbbb

match_obj = re.match('ab+?', s)  # 非贪婪模式，+? 找到一个符合的便不再往后找了
print(match_obj.group())  # ab

s = '<div>hello</div><div>world</div>'
# 思考：如何只找到第一对div
match_obj = re.match('<(?P<n>.+)>.+</(?P=n)>', s)
print(match_obj.group())  # <div>hello</div><div>world</div>

match_obj = re.match('<(?P<n>.+)>.+?</(?P=n)>', s)
print(match_obj.group())  # <div>hello</div>