# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
正则:
    。在 Python 爬虫过程中，实现网页元素解析的方法有很多，正则解析只是其中之一，常见的还有 BeautifulSoup 和
    。lxml，它们都支持网页 HTML 元素的解析操作。本节重点讲解如何使用 re 正则解析模块实现网页信息的提取。

正则常用方法：
    。re.compile(patter, string, flags=0)  -- 用来生成正则表达式对象 regex
    。re.findall(pattern, string, flags=0) -- 返回值是匹配到的内容列表，如果正则表达式有自足，则只能获取到子组的内容
    。regex.findall(string, pos, endpos)  -- 根据正则表达式对象匹配目标字符串内容
    。re.split(pattern, string, flags=0)
    。re.sub(pattern, replace, string, max, flags=0)
    。re.search(pattern, string, flags=0)
非贪婪模式：
    ?跟在*或者+后边用时，表示懒惰模式。也称非贪婪模式。就是匹配尽可能少的字符。就意味着匹配任意数量的重复，但是在能使整个匹配成功
    的前提下使用最少的重复。a.*?b匹配最短的，以a开始，以b结束的字符串。如果把它应用于aabab的话，它会匹配aab（第一到第三个字符）
    和ab（第四到第五个字符）。又比如模式 src=`.*?`，它将会匹配 src=` 开始，以 ` 结束的尽可能短的字符串。且开始和结束中间可以
    没有字符，因为*表示零到多个。用它来搜索 <img src=``test.jpg` width=`60px` height=`80px`/> 时，将会返回 src=``。
'''
import re

html = """
<div><p>www.biancheng.net</p></div>
<div><p>编程帮</p></div>
"""

# 创建正则表达式对象
pattern = re.compile('<div><p>.*</p></div>', re.S)  # 贪婪匹配，re.S 可以匹配换行符

# 匹配HTML元素，提取信息
re_list = pattern.findall(html)
print(re_list)

print('=' * 50)
# 创建正则表达式对象
pattern = re.compile('<div><p>.*?</p></div>', re.S)  # 非贪婪匹配，re.S 可以匹配换行符
# 匹配HTML元素，提取信息
re_list = pattern.findall(html)
print(re_list)
'''
从上述输出结果可以得出非贪婪模式比较适合提取HTML信息
'''

print('=' * 50)

# 正则表达式分组
website = "编程帮 www.biancheng.net"

# 提取所有信息
pattern = re.compile('\w+\s+\w+\.\w+\.\w+')
re_list = pattern.findall(website)
print(re_list)

# 提取匹配信息的第一项
pattern = re.compile('(\w+)\s\w+\.\w+\.\w+')
re_list = pattern.findall(website)
print(re_list)

# 有两个及以上的()则以元组形式显示
pattern = re.compile('(\w+)\s+(\w+\.\w+\.\w+)')
re_list = pattern.findall(website)
print(re_list)

print('=' * 50)
'''
正则表达式分组是提取信息的常用方式。当需要哪个特定信息的时候，就可以通过分组（也就是加括号）的方式获得。
'''

print('=' * 50)
# 网页信息提取
'''
从下面的HTML代码中使用re模块获取两部电影的名称和主演信息
'''

html = """
<div class="movie-item-info">
<p class="name">
<a title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>
<div class="movie-item-info">
<p class="name">
<a title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""

# 寻找规律，书写正则表达式，使用正则表达式提取有效信息
pattern = re.compile(r'<div.*?title="(.*?)".*?star">(.*?)</p.*?div>', re.S)  # 匹配内容，两头要卡紧
re_list = pattern.findall(html)
# print(re_list)

# 整理数据格式，并输出
if re_list:
    for re_infor in re_list:
        print('*' * 20)
        print('影片名称：', re_infor[0])
        print('影片主演：', re_infor[1].strip())