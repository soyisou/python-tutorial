# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
本模块获取自己的名字：
    。__name__    -->  __main__ [打印自己模块叫做 __main__]
其他模块导入获取的是模块的名字
    。模块叫什么，获取的就是什么名字 [模块自身的名字]
'''
# 导入模块01
# import module01

# 思考：那如何不去执行 module01中的语句呢？ 在被导入模块使用 __name__ == __main__
# print(__name__)

# 思考：from module01 import number 是否会全部执行module01中的代码？  是的！只不过我在这只能用number而已了！
from module01 import number
print(number)

from book.modle import Book

print(Book)



