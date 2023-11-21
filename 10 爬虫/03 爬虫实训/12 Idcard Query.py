# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
身份证号查询
'''
import requests
import time

def idcard_query(url, id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }
    data = {
        'idcard': id
    }

    res = requests.get(url, data = data, headers = headers)

    return res.json()['result']

if __name__ == '__main__':
    url = 'https://api.jisuapi.com/idcard/query?appkey=acdd3be9e92edd7a&idcard={}'
    while True:
        id = input('请输入要查询的身份证或身份证前6位：')
        res = idcard_query(url.format(id), id)
        print(res)