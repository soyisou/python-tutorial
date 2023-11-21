# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
使用requests库爬取并下载百度图片
    。本节编写一个快速下载图片的程序，通过百度图片下载需要的前60张图片，并将其保存至相应的目录。
    。思路：
        。获取图片 url
        。
'''
import requests
import re
import os
import time
import random

class ChinazSpider:
    def __init__(self):
        self.url = 'https://aspx.sc.chinaz.com/query.aspx?keyword={}&page={}'
        self.img_links = []
        self.headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    # 获取html
    def get_html(self, url):
        res = requests.get(url, headers=self.headers)
        return res

    # 获取图片url
    def get_image(self, keyword, page):
        # url地址
        url_one = self.url.format(keyword, page)
        html_one = self.get_html(url_one).text

        # 用正则解析html
        regex = r'<div.*?new_block".*?<a target="_blank" href="(.*?)".*?</div>'
        # 匹配对象
        pattern = re.compile(regex, re.S)
        img_list = pattern.findall(html_one)
        # print(img_list)

        for img_url in img_list:
            if len(img_url) == 0:
                continue
            # print(img_url)
            img_url = 'http:' + img_url
            html_two = self.get_html(img_url).text
            regex = r'<div.*?imga".*?<a href="(.*?)".*?</div>'
            pattern = re.compile(regex, re.S)
            link = pattern.findall(html_two)
            if len(link):
                self.img_links.append('http:' + link[0])

        # 创建文件夹
        directory = '../image/{}'.format(keyword)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 添加计数
        count = 1
        for img_link in self.img_links:
            filename = '{}/{}_{}.jpg'.format(directory, keyword, count)
            self.save_image(img_link, filename)
            count += 1

    # 保存图片至本地
    def save_image(self, img_link, filename):
        img = requests.get(img_link, headers=self.headers).content
        with open(filename, 'wb') as ws:
            ws.write(img)
        print('下载成功！')

    # 启动函数
    def run(self):
        # keyword = input('请输入搜索内容：')
        keyword = '心'
        # page = int(input('请输入搜索的终止页：'))
        page = 2
        for i in range(1, page + 1):
            self.get_image(keyword, page)
            # time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    spider = ChinazSpider()
    spider.run()

