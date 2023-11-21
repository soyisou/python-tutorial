# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
爬取 Chinaz，下载图片，并且使用 Xpath解析
'''
import requests
from lxml import etree
import time
import os
import random

class ChinazSpider:
    def __init__(self):
        # 主页图片url
        self.url = 'https://aspx.sc.chinaz.com/query.aspx?keyword={}&page={}'
        # 详细图片链接
        self.img_links = []
        # 搜索关键字
        self.keyword = ''
        # 请求头
        self.headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    # 获取url
    def get_url(self, keyword, page):
        url = self.url.format(keyword, page)
        html = requests.get(url=url, headers=self.headers).text
        self.parse_html1(html)

    # 解析图片主页
    def parse_html1(self, html):
        # 创建解析对象
        p_html = etree.HTML(html)
        # 创建xpath表达式
        xpath_bds = '//div[@class="new_block"]/div/a/@href'
        list1 = p_html.xpath(xpath_bds)
        for link in list1:
            link = 'http:' + link
            self.img_links.append(link)
            # self.parse_html2(link)
        # print(self.img_links)
        # print(len(self.img_links))
        self.parse_html2()

    # 解析图片详细页
    def parse_html2(self):
        list1 = []
        for link in self.img_links:
            html = requests.get(link, headers=self.headers).text
            # 创建解析对象
            p_html = etree.HTML(html)
            # 创建xpath表达式
            xpath_bds = '//div[@class="imga"]/a/@href|//div[@class="show_warp jl_warp clearfix"]/img/@src'
            if p_html.xpath(xpath_bds):
                list1.append('http:' + p_html.xpath(xpath_bds)[0])
        self.img_links = list1
        self.save_image(self.keyword)

    # 保存图片至本地
    def save_image(self, keyword):
        # 创建文件夹
        directory = '../image/{}'.format(keyword)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 添加计数
        count = 1
        for img_link in self.img_links:
            img = requests.get(img_link, headers=self.headers).content
            filename = '{}/{}_{}.jpg'.format(directory, keyword, count)
            with open(filename, 'wb') as ws:
                ws.write(img)
            print('{}_{}下载成功！'.format(keyword, count))
            count += 1
        print('------------图片全部下载完毕！------------')

    def run(self):
        self.keyword = input('请输入要搜索的图片名称：')
        start = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))
        for page in range(start, end + 1):
            self.get_url(self.keyword, page)

if __name__=='__main__':
    ChinazSpider().run()


