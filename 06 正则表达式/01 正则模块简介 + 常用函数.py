# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
正则表达式：
    。英文：regular expression ---> 简写 regex  ---> 验证匹配
    。match()  匹配 从头进行匹配
    。fullmatch()  从头到尾，将整个字符串跟 pattern进行匹配，若匹配不成功则返回 None
    。search()  # 扫描整个字符串，匹配正则格式的内容，若能找到返回 match对象，否则返回 None

    match对象：
        。match对象.group()  # 返回匹配内容
        。match对象.span()  # 返回匹配内容的范围
        。match对象.start()  # 返回匹配的开始位置

'''
import re

# 通过re模块中的compile函数，返回一个模式对象
pattern_obj = re.compile('abc')
# 通过patter_boj对象： match search findall split ··· 得到一个匹配对象
match_obj = pattern_obj.match('abcedfaf')
print(match_obj)  # # <re.Match object; span=(0, 3), match='abc'>
# 匹配对象调用group获取匹配的内容
g = match_obj.group()  # 取到匹配的模式
print(g)  # abc

# 思考：有没有更简便的方法呢？ 有  直接使用 re.match()[封装的底层：return _compile(pattern, flags).match(string)]
match_obj = re.match('abc', 'abcdef', re.I)  # 忽略大小写
print(match_obj)  # <re.Match object; span=(0, 3), match='abc'>

# 思考：将abc往后移，能够匹配成功呢？  no    match  特点：丛头开始比较 Try to apply the pattern at the start of the string
match_obj = re.match('abc', 'dafabcdef', re.I)  # 忽略大小写
print(match_obj)  # None

# 将模式与目标字符串进行比较，从头到尾进行比较，如果全都一样返回对象，否则返回None
match_obj = re.fullmatch('abc', 'abc', re.I)
print(match_obj)  # <re.Match object; span=(0, 3), match='abc'>

# 思考：如果想后移后依然能够匹配，有没有方法呢？  能  使用fulmatch
match_obj = re.search('abc', 'dafabcdef', re.I)
print(match_obj)  # <re.Match object; span=(3, 6), match='abc'>
# print(match_obj.group())  # abc