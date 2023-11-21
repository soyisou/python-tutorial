# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''

'''
import requests

def get_job_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    return response.text


if __name__ == '__main__':
    url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python%2B%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    text = get_job_data(url)
    print(text)


