# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
加 * ：
    。作用：拆包
加 ** ：
    。作用：在函数调用的时候表示拆包，会将字典中的内容拆成关键字参数的形式
    。例如：dict1 = {'a': 22, 'b': 34, 'c': 56} --> func(**dict1) --> func(a=100, b=80, c=90)
'''
def func(*args, **kwargs):
    print(args)  # 用来接收可变参数
    print(kwargs)  # 用来接收关键字参数

list1 = [1, 3, 4, 5, 2]
func(list1, 100)  # ([1, 3, 4, 5, 2], 100)  {}

# 加 * 的作用：拆包
func(*list1, 100)  # (1, 3, 4, 5, 2, 100)  {}

func(*list1, 100, a=1)  # (1, 3, 4, 5, 2, 100)  {'a': 1}

dict1 = {'a': 22, 'b': 34, 'c': 56}
func(*list1, 100, dict1)  # (1, 3, 4, 5, 2, 100, {'a': 22, 'b': 34, 'c': 56})  {}

# 在调用函数时，将 * 加入某个变量前，表示拆该变量
func(*list1, 100, *dict1)  # (1, 3, 4, 5, 2, 100, 'a', 'b', 'c') {}

# 在函数调用时，才可以加两颗 *, 表示对字典拆包(对字典拆包必须加两颗 *)
func(*list1, 100, **dict1)  # (1, 3, 4, 5, 2, 100)  {'a': 22, 'b': 34, 'c': 56}

def func1(a, b, c):
    list1 = [a, b, c]
    print(list1)

dict1 = {'a': 22, 'b': 34, 'c': 56}
func1(**dict1)

list1 = ['hello', 'world', 'hello', 'tom']
def func4(msg):  # msg 和 list1 指向同一个地址
    for index, value in enumerate(msg):
        msg[index] = value.capitalize()  # 首字母大写

func4(list1)
print(list1)

