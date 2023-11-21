# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
*
    。from 模块名 import 具体
    。from 包名.模块名 import 具体

    。导入模块中所有内容，往往使用 *
        。from 包名.模块名 import * [*号代表所有]

    。在被导入模块中，可以通过__all__ = [可以通过*访问的内容] 对*起到一定的限制作用，但对其他的不起限制作用
        。用 *不是所有的内容都导入，而是只要 []中的内容才能导入，才能使用

'''

from module01 import *  # 将所有module01所有内容都导入

# 思考：能够对*起到一定的限制作用？ [加个限制所用，只导入一部分内容] 在被调用模块，使用 __all__ = []

print(number)
# print(Person)  # 加__all__后，NameError: name 'Person' is not defined

# 包的使用
from student import *

from student import modle  # 从包中导入模块，也是可以使用的，但很少使用此方式[比较麻烦！模块.···]
from student import views  # 导入views

# 不能使用！
# from student import *  # 将包中的模块均导入  理论上已经导入modle，但是实际上modle.···是不能用的！


s = modle.Student()
print(s)  # <student.modle.Student object at 0x00000173F3963C08>

# 思考：包中的__init__中的作用
