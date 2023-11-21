# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
pickle实现序列化和反序列化
    。pickle.dumps(dict1)  ---> 字节串
    。pickle.loads(byte_objects)    ---> 对应的Python类型
'''
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

import pickle

# pickle用法和json类似
result = pickle.dumps(dict1)  # 将字典格式转换为pickle格式
print(result)  # 二进制格式

r = pickle.loads(result)
print(r)  # 又转回为字典格式

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

# 创建学生对象
student = Student('张三', 20)
student1 = Student('李四', 19)
boj = pickle.dumps(student)  # python_object--> byte_object
print(boj)  # 字节对象
# print(type(boj))  # <class 'bytes'>

stu = pickle.loads(boj)
print(stu)  # 张三

print('=' * 50)

with open('stus.txt', 'wb') as wstream:
    pickle.dump(student, wstream)  # dump(obj: Any, file: IO[bytes], protocol: Optional[int] = ...)
    pickle.dump(student1, wstream)  # dump(obj: Any, file: IO[bytes], protocol: Optional[int] = ...)

with open('stus.txt', 'rb') as rstream:
    # # 存了两个：张三、李四
    # content = pickle.load(rstream)  # 第一次读
    # print(content)  # 张三
    # content = pickle.load(rstream)  # 第二次读
    # print(content)  # 李四
    # content = pickle.load(rstream)  # 第三次读
    # print(content)  # EOFError: Ran out of input
    try:
        while True:
            content = pickle.load(rstream)
            print(content)
    # except Exception as err:
    #     print(err)  # Ran out of input
    except:
        print('打印完毕！')  # 异常处理