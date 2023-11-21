# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
CSV 实战:
    。CSV 文件又称为逗号分隔值文件，是一种通用的、相对简单的文件格式，用以存储数据，包括数字或者字符。CSV是电子表格
     和数据库中最常见的输入、输出文件格式。
    。通过爬虫将数据抓取下来，然后把数据保存在文件，或者数据库中，这个过程成为数据的持久化存储。
    。CSV模块中的 writer类可以用于读写序列化的数据
        writer(csvfile, dialect='excel', **fmtparams)
            csvfile 必须是支持迭代的对象，可以是文件对象或者是列表对象。
            dialect：编码风格，默认为excel风格，也就是使用逗号，分隔。
            fmtparam:格式化参数，用来覆盖之前dialect对象指定的编码风格。
    。操作文件对象时，需要添加newline参数逐行写入，否则会出现空行现象。
    。quotechar 是引用符，当一段话中出现分隔符的时候，用引用符将这句话括起来，以能排除歧义。
'''
import csv

# 案例1：写入一行
with open('eggs.csv', 'w', newline='') as ws:
    writer = csv.writer(ws, delimiter=' ', quotechar='|')
    writer.writerow(['www.biancheng.net'] * 5 + ['how are you'])
    writer.writerow(['helloworld', 'web site', 'www.biancheng.net'])

# 案例2：写入多行
with open('aggs.csv', 'w', newline='') as ws:
    writer = csv.writer(ws)
    # 注意传入数据的格式为列表元组的格式
    writer.writerows([('hello', 'world'), ('I', 'love', 'you')])

# 案例3: DictWriter写入csv文件
with open('names.csv', 'w', newline='') as  ws:
    # 构建字段名称，也就是key
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(ws, fieldnames=fieldnames)
    # 写入字段名，当做表头
    writer.writeheader()
    # 多行写入
    writer.writerows([{'first_name': 'Baked', 'last_name': 'Beans'}, {'first_name': 'Lovely', 'last_name': 'Spam'}])
    # 单行写入
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

# 案例4： csv.reader()
'''
csv模块中的reader类和DictReader类用于读取文件中的数据，其中reader()语法格式如下：
csv.reader(csvfile, dialect='excel', **fmtparams)
'''
# csv.reader()
with open('eggs.csv', 'r', newline='') as rs:
    reader = csv.reader(rs, delimiter=' ', quotechar='|')
    # print(reader)  # <_csv.reader object at 0x000002A875711668>
    for row in reader:
        print(', '.join(row))

print('=' * 50)

# csv.DictReader()
with open('names.csv', 'r', newline='') as  rs:
    reader = csv.DictReader(rs)
    for row in reader:
        print(row['first_name'], row['last_name'])

