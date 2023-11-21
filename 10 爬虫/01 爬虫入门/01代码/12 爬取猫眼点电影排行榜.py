# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
爬取猫眼电影排行榜
    。使用python爬虫抓取猫眼电影网TOP100排行榜影片信息，包括电影名称、上映时间、主演信息
    。思路
        。在开始编写程序前，首先要确定页面类型（静态页面或者动态页面），其次找到页面的 url规律，最后通过分析
         网页元素结构来确定正则表达式，从而提取网页信息。
        。静态页码：点击右键，查看页面源码，确定要抓取的数据是否存在于页面内。通过浏览器得知要抓取的信息全部
         存在于源码内，因此该页面属于静态页面。
        。编写正则表达式时将需要提取的信息使用(.*?)代替，而不需要的内容（包括元素标签）使用.*?代替。
        。使用面向对象的方法编写爬虫程序，主要编写四个函数
            。请求函数
            。解析函数
            。保存函数
            。主函数
'''
from urllib import request, parse
import re
import time
import random
import csv

class MaoYanSpider:
    # 初始化函数
    def __init__(self):
        self.url = 'https://www.maoyan.com/board/4?offset={}'

    # 请求函数
    def get_url(self, url):
        # 随机用户代理
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
        # 创建请求对象
        req = request.Request(url=url, headers=headers)
        # 发送请求，并获取响应对象
        res = request.urlopen(req)
        # print(res.code)
        # 获取响应内容，并解码
        html = res.read().decode('utf-8')
        print(html)
        # 直接调用解析函数
        # self.parse_html(html)

    # 解析html内容
    def parse_html(self, html):
        # 正则表达式
        regex = '<div.*?title="(.*?)".*?star">(.*?)</p><p class="releasetime">(.*?)</p></div>'
        # 创建正则表达式对象
        pattern = re.compile(regex, re.S)
        re_list = pattern.findall(html)
        print(re_list)
        # self.save_html(re_list)

    # 保存文件至本地
    def save_html(self, re_list):
        # 创建文件对象
        with open('manyan.csv', 'w', encoding='utf-8') as ws:
            # 创建csv操作对象
            writer = csv.writer(ws)
            # 整理数据
            for r in re_list:
                name = r[0].strip()
                star = r[1].strip()
                time = r[2].strip()
                L = [name, star, time]
                writer.writerow(L)
                print(name, star, time)

    # 主函数
    def run(self):
        # 抓取一页数据
        for offset in range(0, 11, 10):
            # 获取最终的url，解析并保存至本地
            url = self.url.format(offset)
            self.get_url(url)
            # 随机休眠
            # time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    # 捕捉异常错误
    try:
        spider = MaoYanSpider()
        spider.run()
    except Exception as err:
        print(err)