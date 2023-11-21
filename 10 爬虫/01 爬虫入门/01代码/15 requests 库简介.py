# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

'''
requests库：
    是在urllib的基础上开发而来，它使用Python语言编写，并且采用了一种开元协议的HTTP库。与urllib相比requests
    更加方便、快捷、因此在编写爬虫程序的时候，requests库使用更多。

常用方法：
    。requests.get(url, headers=headers, params, timeout)  # 向网站发送请求，并且获取网页相应对象
        。url: 要抓取的url地址
        。headers: 用于包装请求头信息
        。params: 请求时携带的查询字符串参数
        。timeout: 超时时间，超过时间会抛出异常
    。requests.post(url, data={请求体的字典})

'''
import requests

'''
requests.get()方法
    。该方法用于get请求，表示向网站发起请求，获取页面响应对象
'''

# 案例1：测试百度
url = 'http://www.baidu.com'
response = requests.get(url)
print(response)  # <Response [200]>

# 案例2：测试 httpbin
# 获取带查询字符串参数的响应对象
data = {
    'name': '编程帮',
    'url': 'www.biancheng.net'
}

# 获取响应对象
response = requests.get('http://httpbin.org/get', params=data)
# 查看Http响应码
print(response.status_code)  # 200
# 查看响应字符编码
print(response.encoding)  # utf-8
# 指定响应字符编码
response.encoding = 'utf-8'
# 查看请求的url地址
print(response.url)  # http://httpbin.org/get?name=%E7%BC%96%E7%A8%8B%E5%B8%AE&url=www.biancheng.net
# 查看请求头信息
print(response.headers)  # {'Date': 'Thu, 25 Nov 2021 02:24:38 GMT', 'Content-Type': 'application/json', 'Content-Length': '425', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
# 查看cookies信息
print(response.cookies)  # <RequestsCookieJar[]>
# 以字符串形式输出
print(response.text)
# 以字节流形式输出，如果要保存下载图片，则需要使用该属性
print(response.content)  # b'{\n  "args": {\n    "name": "\\u7f16\\u7a0b\\u5e2e", \n    "url": "www.biancheng.net"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate, br", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.26.0", \n    "X-Amzn-Trace-Id": "Root=1-619ef451-7d8426e1512ec4e50fb556cb"\n  }, \n  "origin": "115.56.77.139", \n  "url": "http://httpbin.org/get?name=\\u7f16\\u7a0b\\u5e2e&url=www.biancheng.net"\n}\n'






# print(response.text)  # 调用响应对象的text属性，获取文本信息

# 直接拼接参数也行，与上面方法等价
# response1 = requests.get('http://httpbin.org/get?name=编程帮&url=www.biancheng.net')
# print(response1.text)  # 调用响应对象的text属性，获取文本信息

print('=' * 50)

'''
requests.post()方法
    。该方法用于post请求，先由用户向目标url提交数据，然后服务器返回一个HttpResponse响应独享
    。post请求体携带的参数，可以通过开发者调试工具查看，查看步骤：
        。step1：NetWork选项
        。step2：Headers选项
        。step3：Form Data
'''

# 百度翻译
url = 'https://fanyi.baidu.com'

data = {
    'from': 'zh',
    'to': 'en',
    'query': '你好'
}

response = requests.post(url, data=data)
print(response)



