# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
翻译机器人
上中策：使用接口  --- 最好的方案
下下策：使用浏览器 --- 最后的方案
'''
from selenium import webdriver
import requests

def send_to_robot(url, msg):
    headers = {
        'user-Agent': 'Python Robot'  # 该值不一定非得从浏览器粘
    }
    response = requests.get(url + msg, headers=headers)  # 以示尊重
    return response.json()['content']

if __name__ == '__main__':
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
    name = input('请设置您的名字：')
    while True:
        msg = input(name + ':')
        if msg == '退出聊天':
            break
        reply = send_to_robot(url, msg)
        print("机器人：" + reply)