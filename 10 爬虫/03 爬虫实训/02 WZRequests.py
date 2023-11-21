# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
快捷键：
    。双击 shift
'''
import requests

url = 'https://pvp.qq.com/web201605/herolist.shtml'


def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    # 学习方法：双击 shift 细查
    # print(response)  # <Response [200]>
    # print(type(response))  # <class 'requests.models.Response'>

    # 指定编码
    response.encoding = 'gbk'

    return response.text

def extract_hero(text):
    hero_list = []
    return hero_list

def save_hero_list(hero_list):
    pass

def save_hero(hero):
    pass

if __name__ == '__main__':
    content = get_data(url)
    with open('../../11 爬虫练习/wzry.html', 'w', encoding='utf-8') as file:
        file.write(content)
        file.flush()