# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''

'''
import requests

image_url = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/116/116.jpg'

def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    return response

if __name__ == '__main__':
    image_url = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/116/116.jpg'
    response = get_data(image_url)
    with open('../../11 爬虫练习/img.jpg', 'wb') as file:  # 图片不用设置 encoding
        file.write(response.content)  # 注意：只有字符串是直接使用 write模式
        file.flush()
