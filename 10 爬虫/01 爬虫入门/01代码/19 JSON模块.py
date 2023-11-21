# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
JSON(JavaScript Object Notation)是一种轻量级的数据交换格式。JSON易于人阅读和编写，同时也易于机器解析和生成。
能够有效地提升信息的传输效率，因此塔常被作为网络、程序之间传递信息的标准语言，比如客户端和服务器之间信息的交互就是
以 JSON格式传递的。

简单地说，JSON可以将JavaScript对象表示的一组数据转换为字符串格式，以便于在网络、程序间传输这个字符串。并且在需
要地时候，还可以将它转换为编程语言所支持的数据格式。Python语言内置了专门处理 JSON数据的模块 —— JSON模块，该模块
专门处理 JSON和 Python两种数据格式之间的相互转换。

注意：JSON字符串看上去和Python字典非常相似，但其本质却不同！JSON是字符串类型，而 Python字典是 dict类型。

常用方法：
    。json.loads() -- 将json格式的字符串转为Python对象(如：列表、字典、元组、整型以及浮点型等)，最常用地是转为字典
    。json.dumps() -- 将python对象转为JSON字符串，并将转换后的数据写入到json格式的文件中，因此必须操作文件流对象
    。json.load()
        。用于操作文件流对象，不过他与dump()刚好相反，表示从josn文件中读取JSON字符串，并将读取内容转为python对象
    。json.dump(oj,f,indent=0,ensure_ascii=False)-- 将python对象转为JSON字符串，并将转换后的数据写入到json格式的文件中，因此必须操作文件流对象
        。object： python数据对象，比如：字典，列表等
        。f：文件流对象，即文件句柄
        。indent：格式化存储数据，是JSON字符串更易于阅读。
        。ensure_ascii：是否使用ascii编码，当数据中出现中文的时候，需要将其设置为 False
'''

import json
import os

# jon.loads()的使用

# 案例1：JSON字符串之json.loads()
website_info = '{"name": "c语言中文网", "PV": "50万"}'
# 将json字符串转为字典格式
py_dict = json.loads(website_info)
print('python字典数据格式：%s; 数据类型：%s' % (py_dict, type(py_dict)))

print('=' * 50)

# 案例2：JSON字符串之json.dumps()
item = {'website': 'c语言中文网', 'rank': 1}  # python字典类型
item = json.dumps(item, ensure_ascii=False)  # json字符串类型
print('转换之后的数据类型为：', type(item))

print(item)

print('=' * 50)

# 案例3：JSON字符串之json.dump()
site = {'name': 'c语言中文网', 'url': 'c.biancheng.net'}
filename = 'website.json'
with open(filename, 'w', encoding='utf-8') as ws:
    json.dump(site, ws, ensure_ascii=False)

# 案例4：JSON字符串之json.load()
with open(filename, 'r', encoding='utf-8') as rs:
    py_dict = json.load(rs)
    print(type(py_dict))
    print(py_dict)





