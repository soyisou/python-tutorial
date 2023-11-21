# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
心灵毒鸡汤
'''
import requests
from bs4 import BeautifulSoup

import urllib.request
import csv

file = open('D:/学习/综合实践/小组项目/心灵毒鸡汤.csv', 'a', encoding='utf-8', newline='')
file_csv = csv.writer(file)
file_csv.writerow(['序号', '语录'])

def spider_one(i):
    url = "https://www.nihaowua.com/home.html"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    section = soup.section.text.strip(' ')
    print(i, section)
    file_csv.writerow([i, section])

def spider():
    for i in range(10):
        spider_one(i + 1)

spider()