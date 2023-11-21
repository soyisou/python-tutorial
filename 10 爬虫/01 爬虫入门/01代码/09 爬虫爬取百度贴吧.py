# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
爬虫爬取百度贴吧
    。步骤：
        。判断页面类型
            。静态页面
            。动态页面
        。寻找 URL变化规律
        。编写爬虫程序
            。请求函数
            。解析函数
            。保存数据函数
            。入口函数
    。注意：   --- 更充分地模拟人类
        。随机获取 UA
        。随机休眠

使用面向对象方法编写爬虫程序时，思路简单、逻辑清晰、非常清楚，非常容易理解，上述代码主要包含了四个功能函数，他们分别
负责了不同的功能，总结如下：

1）请求函数
    。请求函数最终的结果是返回一个 HTML对象，以便后续的函数调用它
2）解析函数
    。解析函数用来解析 HTML页面，常用的解析模块有正则解析模块、bs4解析模块。通过分析页面，提取出所需的数据。
3）保存数据函数
    。该函数负责将抓取下来的数据保存至数据库中，比如 MySQL、MongoDB等，或者将其保存未文件格式，比如：csv、txt、excel等
4）入口函数
    。入口函数充当整个爬虫程序的桥梁，通过调用不同的功能函数，实现数据的最终抓取。入口函数的主要任务是组织数据，比如要搜
    。索的贴吧名、编码url参数、拼接url地址、定义文件保存路径。
'''
# 导入库
from urllib import request, parse  # 导入请求模块和解析模块
import time  # 导入时间模块
import random  # 导入随机模块
from ua_info import ua_list  # 导入自定义用户代理池

# 定义贴吧爬虫类
class TeiBaSpider:
    # 初始化url属性
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?{}'

    # 请求函数，得到页面
    def get_html(self, url):
        # 随机请求头
        headers = {'User-Agent': random.choice(ua_list)}
        # 创建请求对象
        req = request.Request(url=url, headers=headers)
        # 获取响应对象
        res = request.urlopen(req)
        # 获取响应内容，并解码
        html = res.read().decode('utf-8', 'ignore')
        # 返回最终的html对象
        return html

    # 解析函数
    def parse_html(self):
        pass

    # 保存文件函数
    def save_html(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as ws:
            ws.write(html)

    # 入口函数
    def run(self):
        name = input('请输入贴吧名：')
        begin = int(input('请输入开始页：'))
        end = int(input('请输入结束页：'))

        for page in range(begin, end + 1):
            pn = (page - 1) * 50
            params = {
                'kw': name,
                'pn': str(pn)
            }
            # 编码
            params = parse.urlencode(params)
            # 拼接
            url = self.url.format(params)
            # 获取html对象
            html = self.get_html(url)
            # 定义保存路径
            filename = '../02贴吧数据之深圳大学/{}-{}页.html'.format(name, page)
            # 保存文件
            self.save_html(filename, html)
            # 提示
            print('第%d页抓取成功！' % page)
            # 随机休眠
            time.sleep(random.randint(1, 2))  # 没抓取一个页面随机休眠1-2s
        print('爬取数据成功！！')

if __name__ == '__main__':
    # 爬虫开始时间
    start = time.time()
    # 创建爬虫对象
    spider = TeiBaSpider()
    # 调用启动函数
    spider.run()
    # 爬虫结束时间
    end = time.time()
    # 查看程序执行时间
    print('执行时间：%.2f' % (end - start))







