# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

"""
目的：爬取中餐加盟
爬取网址： https://jiameng.baidu.com/list?category=20907

要求：
    1、爬取当前页面 商铺名称
    2、爬取第二页商铺名称
提示：
    以动态数据爬取方式获取
"""

import requests
import csv

file = open('../../11 爬虫练习/shop.csv', 'a', encoding='utf-8', newline='')
file_csv = csv.writer(file)
file_csv.writerow(['商铺名称'])

class Spider():
    def __init__(self):
        self.url = "https://jiameng.baidu.com/portal/search?ajax=1&accessid=2742514549D0&device=pc&strategy=list&from=jmx&pageSize=20&page=1&category=20907&is_cert=1"
        self.headers ={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        }
        
    def spider(self):
        ls = []
        res = requests.get(self.url, self.headers)
        data1 = res.json()
        data = data1['data']
        list1 = data['list']
        for i in range(len(list1) - 1):
            name = list1[i]['name']
            file_csv.writerow([name])

sp = Spider()
sp.spider()


