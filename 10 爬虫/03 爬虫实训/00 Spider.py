# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
418: 客户端发送的请求被网站的反爬程序返回的
'''
import requests
import time

url = 'https://movie.douban.com/subject/30464542/comments?start=%d&limit=20&status=P&sort=new_score'
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

# 请求的时候增加请求头
response = requests.get(url, headers=headers)  # Ctrl + P 显示参数列表
print(response, response.text)  # 未加请求头，客户端错误 418  --- 被服务器识别出来了，我们需要伪装
# for i in range(10):
#     response = requests.get(url % i * 20, headers=headers)
#     with open('%d.html' % i, 'w', encoding='utf-8') as file:
#         file.write(response.text)
#         file.flush()  # 只要涉及写的东西，用一次 flush 一次

