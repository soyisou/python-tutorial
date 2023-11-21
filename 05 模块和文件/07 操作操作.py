# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
文件相关：
    。银行管理系统
原来数据：
    。list dict ---> 存放于内存  ---> 会被回收
文件：
    。作用：持久化保存数据   --- 存放于硬盘  ---> 不会被回收
思考：
    。python 怎么和文件打交道？
        。python --> 文件：user.txt  user.xls ···
文件操作：
    。系统函数 open(file, mode)  --- Open file and return a stream
        。write(输出)
        。read(输入)
            。注意：只要是读操作，文件不存在就会报错！
            。mode = 'r'
            。rstream.read()
            。rstream.readline()
            。rstream.readlines()
            。

'''
# 1. 打开需要访问的文件，并得到一个流对象
rstream = open('a.txt', 'r', encoding='utf-8', newline='')  # 只要是读操作，若所读文件不存在，则报错。

# 2. 通过流对象进行相关操作
lines = rstream.readlines()
print(lines)  # ['河南理工大学 计算机1801 张三\r\n', '河南理工大学 计算机1801 李四\r\n', '河南理工大学 计算机1801 王五']

print('==============')
all = rstream.read()  # 默认读完，即读到文件最后
print(all)

# 3. 释放流对象资源
rstream.close()  # 关闭流通道，释放资源

print('==============')
# 之前的方式需要三个步骤，每次都得关闭流，否则就会占用资源，比较麻烦，有没有更好的方式？  用 with

# 对于流操作，我们更多地是使用该格式，比较方便
with open(r'D:\python\lesson-online\05 模块和文件\a.txt', 'r', encoding='utf-8') as rstream:  # 节省了关闭操作
    all = rstream.read()
    print(all)
    # 不用关闭了，系统会默认调用close()操作

