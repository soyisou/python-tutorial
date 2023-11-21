# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

'''
__init__.py文件中也可以定义一些函数，变量，类
    。也可以将其当做一个特殊的模块，只不过此模块无需我们导入，只要导包，它会自动执行此模块

    。如何使用此模块中的内容呢？
        。from 包名 import 内容

    。结合*使用
        。from 包名 import *
            。第一部分：
                。如果__init__.py中没有定义任何内容
                    。from 包名 import *  没有任何意义
            。第二部分：
                。想导入包的时候，加载一些内容，则需要再__init__.py中定义内容
                。from 包名 import *
                。在其他的模块中，通过from 包名 import * 导入则可以使用__init__.py中定义的所有内容
                。如果想要限制__init__.py中内容的访问，则需要结合__all__=[]使用
                    。A.   __all__=[外界可以访问的内容]
                    。B.   __all__=['模块名1', '模块名2']
                        。则可以通过模块名.内容，进行访问
                        。多个模块的公用部分可以放进去
'''
# 思考：能否加上 __all__ [__all__主要是为*准备的]
__all__ = ['test1', 'modle']

# 测试
def test1():
    print('测试：test')

# 测试
def test2():
    print('测试：test')