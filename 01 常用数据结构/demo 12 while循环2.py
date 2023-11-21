# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

"""
while 条件：
    条件成立，执行的语句部分

步骤：
1. 先判断条件
2. 执行循环体
3. 判断条件
4. 再执行循环体
···

避免死循环：
方法 1. 改变条件
方法 2. 在循环体中设置结束条件

while 条件：
    条件成立执行的语句部分
    循环体
else:
    表示条件完成了规定的次数，没有遇到 break

结构：
    while
    格式：
    while 条件：
        条件成立执行的语句部分
    else:
        跟 while 是一起的，当 while 循环没有被 break 中断，执行的代码块
"""

"""
cnt = 5
while cnt:
    print('hello world !')
    cnt -= 1

print('----------over----------')

cnt = 0
while True:
    if cnt == 5:
        break
    print('hello world !')
    cnt += 1

print('----------over----------')

"""

"""
cnt = 0
while cnt < 5:
    cnt += 1

    # 不会报错，cnt == 3,只是一种可能,不是必须的
    if cnt == 3:
        break
else:
    print('----------over----------')
"""
# 求 1 - 100 之间的奇数和
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        i += 1
        continue
    sum += i
    i += 1
else:
    print("累加和：", sum)

