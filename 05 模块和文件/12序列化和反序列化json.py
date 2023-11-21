# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
每种编程语言都有各自的数据类型，其中面向对象的编程语言，还允许开发者自定义数据类型(如：自定义类),Python也是一样
很多时候，我们会有这样的需求：
    。把内存中的各种数据类型的数据通过网络传送给其他机器或者客户端
    。把内存中的各种数据类型的数据保存到本地磁盘持久化

什么是序列化和反序列化？
    。将对象转换为可以通过网络传输或可以存储到本地磁盘的数据格式（如：XML，JSON或者特定格式的字节串）的过程称
     为序列化
    。反之，则成为反序列化

Python实现序列化的方式有几种？
    。Json  javascript 脚本 {key:value, key:value}
    。如果要将一个系统内的数据，通过网络传输给其他系统或者客户端，我们通常都需要先把这些数据转化为字符串或者字节串
     而且需要规定一种统一的数据格式才能让接收端正确解析并理解这些数据的含义。
     XML是早期被广泛使用的数据交换格式，在早期的系统集成论文中经常可以看到它的身影；
     <student>
        <name>xiaofang</name>
        <age>18</age>
     </student>
     <student>
        <name>xiaohua</name>
        <age>18</age>
     </student>
     如今大家使用更多的数据交换格式是JSON(JavaScript Object Notation),他是一种轻量级的数据交换格式。
     JSON相对于XML而言，更加简单，易于阅读和编写，同时也易于机器解析和生成。

     序列化：dumps  dump
     反序列化： loads  load

pickle
    如果是想把数据持久化到本地磁盘，这部分数据通常只是供系统内部使用，因此数据转换协议以及转换后的数据格式
    也就不要求是标准、统一的。只要本系统内部能够正确识别即可。但是，系统内部的转换协议通常会随着编程语言版本
    的升级而发生变化（改进算法、提高效率），因此通常会涉及转换协议与编程语言版本兼容问题。
'''
import json

# with open('test.txt', 'w', encoding='utf-8') as wstream:
#     # 字典类型不可以直接存储到本地，需要转化为字符串   --- 可以转换为JSON字符串
#     dict1 = {'sno': '001', 'sname': '小花', 'age': 18, 'status': False}
#     wstream.write(dict1)  # TypeError: write() argument must be str, not dict

dict1 = {'qianfeng': [{'sno': '001', 'sname': '小花', 'age': 18, 'status': False},
                 {'sno': '002', 'sname': '小黄', 'age': 19, 'status': True},
                 {'sno': '003', 'sname': '小黑', 'age': 19, 'status': False},
                 {'sno': '004', 'sname': '小白', 'age': 20, 'status': False}
                 ],
         'beike': [{'sno': '005', 'sname': '小花2', 'age': 18, 'status': False},
                 {'sno': '006', 'sname': '小黄2', 'age': 21, 'status': True},
                 {'sno': '007', 'sname': '小黑2', 'age': 22, 'status': False},
                 {'sno': '008', 'sname': '小白2', 'age': 20, 'status': True}
                 ]
         }
# dict --> json字符串    即序列化
result = json.dumps(dict1)
print(result)
print(type(result))  # <class 'str'>

# json --> dict   即反序列化
r = json.loads(result)
print(r)
print(type(r))  # <class 'dict'>

# 得到qianfeng的学生们的信息
students = r.get('qianfeng')
print(students)
for student in students:  # student也是字典类型
    if '小花' == student.get('sname'):  # 按照姓名查找
        print('找到了')
        break
else:
    print('没有此学生')
'''
序列化：dumps
反序列化: loads

思考：
    。序列化：dump
    。反序列化: load
'''
print('=' * 50)

with open('students.txt', 'w') as wstream:
    json.dump(dict1, wstream)  # 字符串类型写到本地
print('保存成功！')

with open('students.txt', 'r') as rstream:
    content = json.load(rstream)  # 传一个fp即可，即传个流对象即可
    print(content)
    students = content.get('beike')  # 得到beike的学生
    print(students)

