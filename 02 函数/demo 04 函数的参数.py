# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
函数：
    1. 参数
        。参数的作用？
        。普通参数， 默认值参数， 关键字参数， 可变参数，拆包， 装包
        genereator_code(length)
    2. 返回值
'''
import random

# 产生随机验证码
def generator_code(code, length):
    codes = ''
    for i in range(length):
        ran = random.choice(code)
        codes += ran
    # 打印验证码
    print('本次验证码是：', codes)

code = 'dfagfqw23424@dfadf45bf*43S$FFSD3d55'
generator_code(code = code, length=15)