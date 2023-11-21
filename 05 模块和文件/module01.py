# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
模块01
'''
# __all__ 仅限于用*使用的内容，对其他的不限制哦
__all__ = ['number', '_MAX', '_MIN']

# 定义变量
number = 100
_MAX = 200
_MIN = 10

# 定义函数
def func():
    for i in range(4):
        print('---->', i)

# 定义类
class Person:
    def __init__(self):
        print('初始化方法：init')

    def show(self):
        print('Person的show方法')

# 调用函数
# print(__name__)
# print(number)
# func()

# 调用函数
if __name__ == '__main__':  # 在其他模块中__name__ 为该模块名，不等于__main__，因此不会执行
# 如果自己执行__name__ == 'main'
# 但如果其他模块调用我，则__name__ == 我的模块名
    print(number)
    func()

# 测试
# print('===========')