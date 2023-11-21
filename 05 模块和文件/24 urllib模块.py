# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
urllib 和 urllib3，requests

url：
    。组成
        。协议：//存放资源的域名或者地址//具体资源
    。urllib.request  用来发出请求
    。urllib.parse

    。urllib.request.urlopen(str)  ---> response对象

    。resquest = urllib.request.Request(url, data, headers)
    。urllib.request.urlopen(str)  ---> response对象

    。response.read()  --- 从response中获取信息 --- 字节信息
    。response.read().decode('utf-8')  --> 对信息进行解码
'''


'''
简单版：

# 通过request模拟浏览器发送请求
from urllib import request

# 响应对象
respose = request.urlopen('https://zz.lianjia.com/zufang/ZZ2865824608672546816.html?nav=0&unique_id=3c2713fc-9b41-428c-bdca-2153e6788559zufangrs1637293421942')


# 读取内容
content = respose.read()  # read得到的是二进制的数据,要是想打印出来的话，还需要解码才行

# 打印内容
print(content.decode())
'''

# 通过request模拟浏览器发送请求
from urllib import request, parse

headers = {
    # 此时，已经不是Python程序了，否则后台会识别出我们是Python程序，现在已经伪装成一个浏览器用户了
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

data = {
'nav': 0
}

# 将字典形式的data转换为字节形式
data = parse.urlencode(data).encode('utf-8')

url = 'https://zz.lianjia.com/zufang/ZZ2865824608672546816.html'

# 发送请求
rq = request.Request(url=url, data=data, headers=headers)  # 添加伪装部分

# 获取响应
response = request.urlopen(rq)

# 读取内容
content = response.read()

# 打印内容
print(content.decode('utf-8'))

# urllib3库
'''
分的比较详细，比如: get请求和post请求
'''
import urllib3

# requests 库
import requests




