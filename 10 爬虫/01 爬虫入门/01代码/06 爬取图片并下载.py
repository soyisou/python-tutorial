# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
爬取图片并下载
    。步骤：
        。拼接 url
        。发送请求
            。创建请求对象-Request
            。获取相应对象-urlopen
            。获取相应内容-read
        。将照片下载到本地
'''

# 导入所需模块
from  urllib import request
from  urllib import parse

# 拼接URL地址
url = 'http://www.baidu.com/s?wd={}'
# 搜索内容
word = input('请输入搜索内容：')
params = parse.quote(word)
full_url = url.format(params)

# 向URL发送请求
'''
 。创建请求对象-Request
 。获取响应对象-urlopen
 。获取响应内容-read
'''

# 重构请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

# 创建请求对象
req = request.Request(url=full_url, headers=headers)

# 获取响应对象
res = request.urlopen(req)

# 获取响应内容
html = res.read().decode('utf-8')
# print(html)

# 保存到本地
filename = word + '.html'
with open(filename, 'w', encoding='utf-8') as ws:
    ws.write(html)

