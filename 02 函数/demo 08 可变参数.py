# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
可变参数：
    。拆包
    。装包
    。格式：
        def 函数名(位置参数, *args, ** kwargs):  # * 将分散的数值装包，装起来，让函数变得更加灵活
            pass
        args --> ()  # 可变参数，底层都会将所有的位置参数 positon argument, 存放到 args 当中
        kwargs --> {}  # 关键字参数，会将所有的关键字参数都存放到字典当中

        调用：
            函数名(1, 2, 3) --> 1, 2, 3 位置参数 --> (1, 2, 3)
            函数名(a=1, b=2) --> a = 1, b = 2, 关键字参数 --> {'a':1, 'b':2}
'''
a, b = 1, 5
print(a, b)

x, y, z = 1, 3, 7
print(x, y, z)

# 拆包
list1 = [1, 3, 6]  # unpack 拆包
n1, n2, n3 = list1  # 先做一个动作拆包，其次再给白前面的变量赋值
print(n1, n2, n3)

# 先拆包，后装包
list2 = [1, 5, 3, 5, 6]
x, y, *z = list2  # step1: x, y, *z = 1, 5, 3, 5, 6  step2: x, y, *z = 1, 5, [3, 5, 6]
print(x, y, z)  # 1 5 [3, 5, 6]

x, *y, z = list2  # 优先给不带 * 的， 然后将剩余的装包给带 * 的
print(x, y, z)  # 1 [5, 3, 5] 6

# 求和
def add(a, b):
    print('和：', a + b)

# 调用add函数
add(6, 4)

# 如果要求三个，四个，五个数的和呢 ?
def add(*args):  # 名字args无所谓，可以随便起，但是必须要有 * (将分散的数值装到一块)
    # print(args)  # 函数中经过 * 处理后，是元组类型
    sum = 0
    for i in args:
        sum += i
    print('和：', sum)

add(3, 5)  # 和： 8
add()  # 和： 0
add(1)  # 和： 1

# 字符串拼接
def joint(seq,*args):  # 经过 * 处理后，args中的内容变成一个元组
    s = ''
    # 方法一：
    # count = 0
    # for i in args:
    #     s += i
    #     if not count == len(args) - 1:
    #         s += seq
    #     count += 1
    # print(s)  # hello-world-!

    # 方法二：
    # 利用切片
    for i in args:
        s += i
        s += seq

    s = s[:-1]
    print(s)

joint('-', 'hello', 'world', '!')

def func(a, b = 0, *args):
    print(a)  # 2
    print(b)  # 5
    print(args)  # (3, 6, 7, 5)

# func(a = 2, 5, 3, 6, 7, 5)  # 报错：SyntaxError: positional argument follows keyword argument
func(2, 5, 3, 6, 7, 5)  # 只要函数定义中出现可变参数，则在使用关键字参数的时候就要慎重 ！ 关键字参数最好不用！

def func(*args, a = 10):  # 该写法无意义，不推荐！
    print(args)  # (1, 3, 5, 6, 7)
    print(a)

func(1, 3, 5, 6, 7)  # 10 函数的所有实际参数，都无法给 a 赋值
func(1, 3, 5, 6, a = 7)  # 7 通过关键字的方式给 a 赋值

print('=' * 50)

def func3(*args):
    print(args)

func3()
func3(1, 3, 4)

print('=' * 100)
def func4(*args, **kwargs):  # kwargs: keyword argument 关键字参数
    print(args)
    print(kwargs)

# 调用 func4
func4()  # () {}

func4(1, 4, 6, 3)  # (1, 4, 6, 3)

func4(1, 3, 4, a = 6, b = 9) # (1, 3, 4) {'a': 6, 'b': 9}

func4(a = 10, b = 3)  # () {'a': 10, 'b': 3}