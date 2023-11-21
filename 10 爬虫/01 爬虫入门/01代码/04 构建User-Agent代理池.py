# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
在编写爬虫程序时，一般都会构建一个 User-Agent （用户代理）池，就是把多个浏览器的 信息放进列表中，
然后再从中随机选择。构建用户代理池，能够避免总是使用一个 UA 来访问网站，因为短时间内总使用一个 UA
高频率访问的网站，可能会引起网站的警觉，从而封杀掉 IP。
    。自定义 UA代理池
    。模块随机获取 UA
'''
from fake_useragent import UserAgent
#实例化一个对象
ua=UserAgent()
#随机获取一个ie浏览器ua
print(ua.ie)
print(ua.ie)
#随机获取一个火狐浏览器ua
print(ua.firefox)
print(ua.firefox)

