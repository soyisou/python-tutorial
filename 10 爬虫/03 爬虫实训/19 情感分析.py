# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
通过百度 API 进行情感分析
'''
import json
import requests
import csv
import os
import time

file = open('D:/学习/综合实践/小组项目/结果.csv', 'w', encoding='utf-8', newline='')
file_csv = csv.writer(file)
file_csv.writerow(['positive_prob', 'confidence', 'negative_prob', 'sentiment'])


# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的 SK
start_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=AudTbTd2ndODSwQz1R5Wtt04&client_secret=KfeGSqw6P16ls1SVnkrB2UgfsD6XNt7x'
start_response = requests.get(start_url)
token = start_response.json()['access_token']
print(token)

# token = "24.a3f3663dfc133cd605966054a4a1fc01.2592000.1638092051.282335-25078811"
url = 'https://aip.baidubce.com/oauth/2.0/token={}'.format(token)
# url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token={}'.format(token)
response = requests.get(url)
print(response.json())
data = {
    'text':'这个手机不好用'
}
data = json.dumps(data)  # dumps是将dict转化成str格式，loads是将str转化成dict格式
res = requests.post(start_url, data=data).text

data1 = json.loads(res)  # 将字符串转换为字典类型

result = data1['items'][0]
print(result['positive_prob'])

file_csv.writerow([result['positive_prob'], result['confidence'], result['negative_prob'], result['sentiment']])
print(data1)









# path = r'C:\Users\LJM\AppData\Roaming\Lantern'
# dirs = os.listdir(path)
#
# for file in dirs:
#     print(file)

# print(os.listdir('./tmp'))
#
#
# # 创建的目录
# path = "./tmp/home/monthly/daily"
#
# os.makedirs( path, 0o777 );
#
# print ("路径被创建")