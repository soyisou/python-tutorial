# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
情感分析 -- 官网
'''
import requests
import json
import csv
import os

file = open('D:/学习/综合实践/小组项目/结果.csv', 'w', encoding='utf-8', newline='')
file_csv = csv.writer(file)
file_csv.writerow(['positive_prob', 'confidence', 'negative_prob', 'sentiment'])

ak = 'AudTbTd2ndODSwQz1R5Wtt04'
sk = 'KfeGSqw6P16ls1SVnkrB2UgfsD6XNt7x'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(ak,sk)
response = requests.get(host)
token = response.json()['access_token']
url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token={}'.format(token)

data = {
    'text':'这个手机不好用'
}

data = json.dumps(data)  # dumps是将dict转化成str格式，loads是将str转化成dict格式
res = requests.post(url, data=data).text

data1 = json.loads(res)  # 将字符串转换为字典类型

result = data1['items'][0]
print(result['positive_prob'])

file_csv.writerow([result['positive_prob'], result['confidence'], result['negative_prob'], result['sentiment']])
print(data1)
