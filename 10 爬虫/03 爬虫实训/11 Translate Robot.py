# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
Python 驱动浏览器 --- selenium
翻译机器人
'''
from selenium import webdriver
import requests
import time

def translate(word):
    # 设置浏览器无界面模式
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    # 设置浏览器驱动路径和浏览器无界面模式
    driver = webdriver.Chrome(executable_path='D:/学习/综合实践/老师课程/chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)
    # 获取目标的 url
    url = 'https://fanyi.youdao.com/'
    res = driver.get(url)

    time.sleep(1)
    # 通过id确定翻译框内容
    input_original = driver.find_element_by_id("inputOriginal")
    input_original.send_keys(word)  # 在翻译框中送入翻译内容
    # 睡眠 1 s
    time.sleep(1)
    # 通过id准确定位翻译框
    trans_target = driver.find_element_by_id('transTarget')
    #返回翻译框内容
    return trans_target.text
    # 关闭浏览器
    driver.close()

if __name__ == '__main__':
    while True:
        word = input('要翻译的内容为：')
        en = translate(word)
        print('{}的翻译为：{}' .format(word, en))
        print('==' * 50)