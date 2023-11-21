# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
异常的传递
'''
import random

def func(list1):  # 假如要求传递的是类别类型
    # 思考3：能够在该处捕获？
    try:
        sum = 0
        for i in list1:
            print(i)
            sum += i  # raise 表示抛出、扔出
    except Exception as err:  # 若该处便能处理，则不会再往外传递异常了
        print('func-------->', err)

def get_random():
    # 思考1：能够在该处捕获？
    try:
        list1 = []
        for i in range(5):
            ran = random.randint(1, 10)  # 左右均闭
            list1.append(ran)

        list1.append('9')
        func(list1)
    except Exception as err:  # 若该处便能处理，则不会再往外传递异常了
        print('get_random------->', err)  # -------> unsupported operand type(s) for +=: 'int' and 'str'

    # 思考2：能够在该处捕获？

# get_random()

# 思考：能够对get_random()进行异常处理呢？他能不能帮我们处理错误呢？

# 在用的时候，如果错误是多层的，则错误是可以传递的
try:
    get_random()  # 尽管该语句本身没有错，但是该方法调用过程中出错，该错最终会追踪到(raise到)该函数的调用处的哦！
except Exception as err:
    print('外层------>', err)
