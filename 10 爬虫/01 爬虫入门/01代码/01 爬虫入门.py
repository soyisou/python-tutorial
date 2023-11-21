# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
爬虫入门
    。字符串转换为字节码
        string.encode("utf-8")
    。字节码转换为字符串
        bytes.decode("utf-8")

'''
# 导包,发起请求,使用urllib库中的request模块
from urllib import request

# urlopen向url发送请求，返回相应对象
response = request.urlopen('http://www.baidu.com')
print(response)  # <http.client.HTTPResponse object at 0x000001FE56FE9D48>

# 获取相应对象的url地址
# url = response.geturl()  # http://www.baidu.com
# print(url)

# 返回请求时的http响应码
# code = response.getcode()
# print(code)  # 200

# 获取相应内容，并解码
html = response.read().decode('utf-8')  # 字节串类型(bytes) --> 字符串类型(string)
print(html)  # 打印相应内容


