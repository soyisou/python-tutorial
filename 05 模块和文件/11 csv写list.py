# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
思考：能够将数据保存在 .scv格式的文件中？
文件不是一个图片，文本文件
表格：
    。excel
        。数据导出 --> csv
注意：word格式 ！= .txt格式, 处理 word格式需要第三方库

读写csv的两种格式：
    。读 csv
        。以列表形式
        。以自典形式
    。写 csv
        。以列表形式
        。以自典形式
'''
# 导入csv模块
import csv

# 以列表形式
def write_csv(file_path):  # def writer(fileobj, dialect='excel', *args, **kwargs):
    # 虽然我们不用open直接操作，但是我们也离不开open
    with open(file_path, 'w', newline='') as wstream:  # 找到文件，创建文件对象
        csv_writer = csv.writer(wstream)  # 因为csv需要一个文件对象
        # 写东西
        csv_writer.writerow(['001', '小花', 19])
        csv_writer.writerow(['002', '小芳', 21])
        csv_writer.writerow(['003', '翠花', 20])

# write_csv(file_path)

# 以字典形式
def dictwrite_csv(file_path):
    # 虽然我们不用open直接操作，但是我们也离不开open
    with open(file_path, 'w', newline='') as wstream:  # 找到文件，创建文件对象
        fieldnames = ['sno', 'sname', 'age']
        csv_writer = csv.DictWriter(wstream, fieldnames)
        # 写东西
        csv_writer.writeheader()
        csv_writer.writerow({'sno': '001', 'sname': '小花', 'age': 19})
        csv_writer.writerow({'sno': '002', 'sname': '小芳', 'age': 21})
        csv_writer.writerow({'sno': '003', 'sname': '翠花', 'age': 20})

file_path = r'D:\python\lesson-online\05 模块和文件\users.csv'

dictwrite_csv(file_path)

# 后期还可以使用pandas 处理csv文件

# 读csv文件
def read_csv(file_path):  # def writer(fileobj, dialect='excel', *args, **kwargs):
    # 虽然我们不用open直接操作，但是我们也离不开open
    with open(file_path, 'r', newline='') as rstream:  # 找到文件，创建文件对象
        csv_reader = csv.reader(rstream)  # 因为csv需要一个文件对象
        for row in csv_reader:
            print(row)  # 列表形式

read_csv(file_path)

# 以自典形式读csv
def dictread_csv(file_path):
    # 虽然我们不用open直接操作，但是我们也离不开open
    with open(file_path, 'r', newline='') as rstream:  # 找到文件，创建文件对象
        csv_reader = csv.DictReader(rstream)
        for row in csv_reader:
            # print(row)  # OrderedDict([('sno', '001'), ('sname', '小花'), ('age', '19')])
            print(dict(row))  # 以自典形式展示  {'sno': '001', 'sname': '小花', 'age': '19'}

dictread_csv(file_path)




