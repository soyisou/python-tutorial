# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
九九乘法表:
    1 * 1 = 1
    1 * 2 = 2  2 * 2 = 2
    1 * 3 = 3  2 * 3 = 6   ···
    1 * 4 = 4  2 * 4 = 8   ···
    1 * 5 = 5  2 * 5 = 10  ···
    1 * 6 = 6  2 * 6 = 12  ···
    1 * 7 = 7  2 * 7 = 14  ···
    1 * 8 = 8  2 * 8 = 16  ···
    1 * 9 = 9  2 * 9 = 18  ···
'''
# 打印九九乘法表
for i in range(1, 10):  # i 控制行 --> 第二位数字
    for j in range(1, 10):  # j 控制列  --> 第一位数字
        if j <= i:  # 列号 <= 行号
            print('{} * {} = {}\t'.format(j, i, i * j), end='')
    print()  # 打印一整行后，换行

print('=' * 30)

# 打印九九乘法表
for i in range(1, 10):  # i 控制行 --> 第二位数字
    for j in range(1, i + 1):  # j 控制列  --> 第一位数字
        print('{} * {} = {}\t'.format(j, i, i * j), end='')
    print()  # 打印一整行后，换行

print('=' * 30)

for i in range(1, 10):
    for j in range(1, i + 1):
            print('*', end='')
    print()