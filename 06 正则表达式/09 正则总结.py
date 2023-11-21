# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
urllib:
    url
    request 请求
    response 相应

logging 日志

正则：
    import re
    re.match()
    re.fullmatch()
    re.findall()
    re.sub()
    re.split()

    match对象：
    m.group()
    m.group(n)
    m.span()

符号：
    .
    []
    [^]
    *
    +
    ?
    {m,n}
    *?
    +?
    ??
    {m,n}?
    |  常和()结合使用
    ()  常和|结合使用
    ^  开始
    $  结束

预定义
    \d
    \w
    \s
    \b
    ···大写

分组
    \number  引用number组内容
    (?P<name>patter)  使用名：(?P=name)

贪婪与非贪婪
    +
    *
    ？
    以上均是贪婪模式，会尽可能无限进行匹配，尽可能多地进行匹配
    +?
    *?
    ??
    以上均是非贪婪模式，只匹配 0次或者 1次

结合网页标签的使用内容的提取
    ()  分组往往会和非贪婪进行结合使用
'''
import re

s = 'hello5hight6fadf823fdas9world'
# 思考：遇到数字，则切割，字符串能否直接完成任务？ 不可以，字符串切片功能太弱！
# s1 = s.split('5')
# print(s1)

# 思考：能否用正则切割
result = re.split(r'\d+', s)
print(result)  # ['hello', 'hight', 'fadf', 'fdas', 'world']

