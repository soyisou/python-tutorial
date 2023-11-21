# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
面向对象编程
'''
# 导入所需模块
from  urllib import request
from  urllib import parse

class Spider:
    # 初始化函数
    def __init__(self):
        # 初始url
        self.url = 'http://www.baidu.com/s?kw={}'

    # 获取最终的url
    def get_url(self, word):
        # 初始url
        url = 'http://www.baidu.com/s?kw={}'
        # 编码
        params = parse.quote(word)
        # 拼接
        url = url.format(params)
        # 最终url
        return url

    # 请求相应并下载文件
    def request_url(self, url, filename):
        # 重构请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
        }
        # 创建请求对象
        req = request.Request(url=url, headers=headers)
        # 获取响应对象
        res = request.urlopen(req)
        # 获取响应内容
        html = res.read().decode('utf-8')
        # print(html)
        with open(filename, 'w', encoding='utf-8') as ws:
            ws.write(html)
        print('下载完毕！')

    # 运行函数
    def run(self):
        word = input('请输入搜索内容：')
        self.url = self.get_url(word)
        filename = word + '.html'
        self.request_url(self.url, filename)

Spider().run()