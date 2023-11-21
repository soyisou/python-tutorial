# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
函数式编程
'''
# 导入所需模块
from  urllib import request
from  urllib import parse

# 获取最终的url
def get_url(word):
    # 初始url
    url = 'http://www.baidu.com/s?kw={}'
    # 编码
    params = parse.quote(word)
    # 拼接
    url = url.format(params)
    # 最终url
    return url

def request_url(url, filename):
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

if __name__ == '__main__':
    word = input('请输入搜索内容：')
    url = get_url(word)
    filename = word + '.html'
    request_url(url, filename)