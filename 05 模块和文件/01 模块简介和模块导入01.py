# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
import random
import time

模块
    。系统模块     --> 可以直接使用
    。自定义模块    --->
        。一个 py文件就是一个模块
        。为什么要有模块的概念？
            。可以认为模块就是一个 “工具箱 ”，里面提供的是各种 ’工具‘
        。哪些工具可以在模块中定义？
            。变量
            。函数
            。类
        。如何使用模块？
            。模块中的内容可以为自己所用
            。模块中的内容可以被其他所用

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

记住：搜索，是基于项目的当前位置，往下搜索的！
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