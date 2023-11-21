# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
豆瓣电影爬取小程序
    。核心技术
        。requests库的相关操作
        。xpath语法
        。lxml操作
        。csv操作
    。思路：
        。step1: 查看爬取页面的源码，判断是目标页面是静态页面还是动态页面，本爬取页面属于静态页面
        。step2: 分析主页面规律（链接规律，页面具体内容分布规律） --- 0,25,50···
        。step3: 解析主页面，将主页面中的子页面超链接保存到一个列表中
        。step4: 遍历该列表，解析子页面
        。step5: 分析子页面结构，利用 lxml解析子页面
        。step6: 将数据保存至本地
    。友谊提示：
        。尽量不要爬取太频繁，否则可能遭受IP封禁  ---- 我的 IP就被封了
        。可以适当增加伪装效果，避免被反爬
        。爬取内容，我只写了几个，可以再加哦 ~

'''
from lxml import etree
# from ua_info import ua_list  # 自定义用户代理
import requests
import time
import os
import random
import csv

file = open('./豆瓣电影.csv', 'a', encoding='utf-8', newline='')
file_csv = csv.writer(file)
file_csv.writerow(['电影名称', '导演', '上映时间'])

class DoubanSpider:
    # 初始化函数
    def __init__(self):
        # 初始url
        self.url = 'https://movie.douban.com/top250?start=0'
        # 每条电影的详细链接
        self.link = []
        # 请求头
        self.headers = {  # 当然也可以自定义用户代理，随机取出，增加伪装性，防止遭受反爬
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    # 获取url
    def get_html(self, page):
        url = self.url.format(page * 25)
        html = requests.get(url=url, headers=self.headers).text
        self.parse_html1(html)

    # 解析主页
    def parse_html1(self, html):
        # 定义解析对象
        ps_html = etree.HTML(html)
        # 定义xpath规则
        xpath_bds = '//div[@class="hd"]/a/@href'
        # 解析主页
        self.link = ps_html.xpath(xpath_bds)
        for url in self.link:
            # 进一步解析详细页
            self.parse_html2(url)

    # 解析详细页
    def parse_html2(self, url):
        # 获取html
        html = requests.get(url=url, headers=self.headers).text
        # 定义解析对象
        ps_html = etree.HTML(html)
        # 存放电影名称、导演、上映时间、片长
        list_all = []

        # 定义xpath规则之电影名称
        xpath_bds = '//div[@id="content"]/h1/span[@property="v:itemreviewed"]/text()'
        if ps_html.xpath(xpath_bds):
            name = ps_html.xpath(xpath_bds)[0]  # 暂存电影名称，便于后期提示
            list_all.append(ps_html.xpath(xpath_bds)[0])

        # 定义xpath规则之导演
        xpath_bds = '//div[@id="info"]/span/span[@class="attrs"]/a/text()'
        if ps_html.xpath(xpath_bds):
            list_all.append(ps_html.xpath(xpath_bds)[0])

        # 定义xpath规则之上映时间
        xpath_bds = '//div[@id="content"]/h1/span[@class="year"]/text()'
        if ps_html.xpath(xpath_bds):
            list_all.append(ps_html.xpath(xpath_bds)[0])

        # 将数据写入csv文件
        try:
            file_csv.writerow(list_all)
            print('电影：{}数据保存成功！'.format(name))
        except Exception as err:
            print(err)

    # 启动函数
    def run(self):
        for page in range(0, 5):
            self.get_html(page)
            # 模拟人的下载，伪装作用，防止遭受反爬
            # time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    DoubanSpider().run()
