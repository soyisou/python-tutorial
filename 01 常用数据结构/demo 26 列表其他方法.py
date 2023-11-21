# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
列表其他方法：
    补充： ''.join(iterable) --> 把可迭代的合并成一个字符串
    copy()

'''
import random

list1 = [2, 4, 3, 6, 9]

# 随机产生 QQ 号码： 5-10位，0 不能开头
qq = []
count = 0
while True:
    ran = random.randint(0, 9)
    if count == 0 and ran == 0:
        continue
    qq.append(ran)
    count += 1
    # 退出
    if count == 10:
        break

print(qq)

# 合并 join()    ''.join(list|tuple|set)
# new_str = ''.join(str(qq))  # TypeError: sequence item 0: expected str instance, int found
# print(new_str)

list0 = ['a', 'b', 'c']  # abc, 列表中放的不能为整型
print(''.join(list0))

list0 = ['a', 'b', 'c']  # a+b+c
print('+'.join(list0))

# 随机产生 QQ 号码： 5-10位，0 不能开头
qq = []
count = 0
while True:
    ran = random.randint(0, 9)
    if count == 0 and ran == 0:
        continue
    qq.append(str(ran))
    count += 1  # 或者 qq += str(ran)
    # 退出
    if count == 10:
        break

new_str = ''.join(qq)  # 6368101638
print(new_str)