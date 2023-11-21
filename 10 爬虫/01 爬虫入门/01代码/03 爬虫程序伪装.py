# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
爬虫程序伪装
'''
from urllib import request

# 测试网址
url = 'http://httpbin.org/get'

# 重构请求头，伪装为谷歌浏览器进行访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

# 1. 创建请求对象，包装UA信息
req = request.Request(url=url, headers=headers)
# 2. 发送请求获取相应对象
res = request.urlopen(req)
# 3. 解码，提取相应内容
html = res.read().decode('utf-8')
print(html)