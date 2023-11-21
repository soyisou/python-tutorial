# Email  : 878665865@qq.com
# coding : utf - 8
'''
文件操作：
    。open(file_path, mode, encoding='utf-8')
    。file_path = '路径'
    。mode = 'r'/'w'/'rb'/'wb'/'a'
csv: 表格
    。import csv
    。csv.reader()  --> list
    。csv.writer(list)
序列化和反序列化：
    。dict, list, int, bool, Student···  --> 文件保存，网络传输[如：ajax操作 --- 底层 json数据]
    。json
        。import json
        。json.dumps() ---> 一般在网络中用
        。json.dump()  ---> 一般在文件中用
        。json.loads() ---> 反序列化
        。json.load()  ---> 文件，反序列化
    。pickle
        。import pickle
        。pickle.dumps()
        。pickle.dump()
        。pickle.loads()
        。pickle.load()

相对路径和绝对路径：
    。推荐用相对路径

'''
# 相对路径  file_path = 'a.txt'   ---> 相对路径：基于当前文件
# with open('a.txt', 'w', encoding='utf-8') as ws:
#     ws.write('hello')

# 相对路径
# with open('./a.txt', 'r', encoding='utf-8') as rs:
#     print(rs.read())

# 思考如何访问上一级里面的文件或者上一级文件呢？ 可以用 ..
with open('../14 测试/a.txt', 'r', encoding='utf-8') as rs:
    print(rs.read())

# 绝对路径 -- 从根目录下开始的完整路径
# with open(r'D:\python\lesson-online\05 模块和文件\a.txt', 'r', encoding='utf-8') as rs:
#     print(rs.read())