# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
"""
结构：
    while
    格式：
    while 条件：
        条件成立执行的语句部分
    else:
        跟 while 是一起的，当 while 循环没有被 break 中断，执行的代码块

    for
    格式： # 每循环一次取序列中的值，将值赋值给变量 i
        for i in 序列：
            循环体的内容

        序列：str, list, tuple, set, dict
        range()
        int
"""
import random

card = ''
i = 0
while i < 16:
    r = random.randint(0, 9)
    card += str(r)
    i += 1
    if i % 4 == 0:
        card += ' '
else:
    print(card)