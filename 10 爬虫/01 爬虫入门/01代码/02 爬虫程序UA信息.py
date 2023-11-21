# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
爬虫程序UA信息
'''
from urllib import request

response = request.urlopen('http://httpbin.org/get')
html = response.read().decode('utf-8')
print(html)