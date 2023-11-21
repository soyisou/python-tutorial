# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
使用 00 module01.py文件中的内容
如何导入模块？
    。import 模块名[py文件名叫什么，模块名就叫什么]
        。使用
            。模块名.变量
            。模块名.函数名()
            。模块名.类()
    。from ··· import
        。from 后面跟的是模块名
        。import 后面跟的是你想使用的内容[变量、函数、类]
        。from 模块名 import * [*代表模块中的所有内容]

        。使用：
            。直接使用变量
            。函数()
            。类()
'''
# 方式一
# import module01
#
# print(module01.number)
#
# module01.func()
# print(module01.Person)
#
# p = module01.Person()
# p.show()


# 方式二
# from module01 import number, func, Person  # 变量名，函数名，对象名
# from module01 import *
#
# print(number)  # 100
# func()
# p = Person()
# p.show()

# 方式三
from module01 import *

print(number)  # 100
func()
p = Person()
p.show()