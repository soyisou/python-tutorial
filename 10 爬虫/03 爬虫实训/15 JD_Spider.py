# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
爬去京东搜索目标的信息
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv
import time

from selenium.webdriver.common.by import By


class JdSpider():
    def __init__(self, wd):
        self.wd = wd
        self.url = 'https://www.jd.com/'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path=r'D:\学习\综合实践\老师课程\chromedriver\chromedriver.exe', options=chrome_options)
    def parser(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        wrap_div_list = soup.find_all('div', attrs={"class": "gl-i-wrap"})
        for div in wrap_div_list:
            # 获取价格
            p_price = div.find('div', attrs={"class": "p-price"}).text.strip()
            print(p_price)
            # 获取商品名称
            p_name = div.find('div', attrs={"class": "p-name p-name-type-2"}).text.strip()
            print(p_name)
            # 获取评价数
            p_commit = div.find('div', attrs={"class": "p-commit"}).text.strip()
            print(p_commit)
            # 获取商铺名称
            p_shop = div.find('div', attrs={"class": "p-shop"}).text.strip()
            print(p_shop)

            print('=' * 100)


    def run(self):
        self.driver.get(self.url)
        self.driver.find_element(by=By.CSS_SELECTOR, value='#key').send_keys(self.wd)
        self.driver.find_element(by=By.CSS_SELECTOR, value='#search > div > div.form > button > i').click()

        for i in range(20):
            self.driver.execute_script('window.scrollBy(0, 600)')
            time.sleep(0.1)

        # time.sleep(3)

        html = self.driver.page_source
        self.parser(html)

wd = '手机'
JdSpider(wd).run()