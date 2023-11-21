# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

"""
# for···in 完成 1 -50 的偶数打印
# 完成猜数字：如果猜大了提示小一点，如果小了，提示大一点，否则恭喜猜对啦！
"""
# for···in 完成 1 -50 的偶数打印
for i in range(1, 51):
    if i % 2 == 0:
        print(i, sep=' ', end=' ')
        if i % 5 == 0:
            print()
        continue
    i += 1

# 完成猜数字：如果猜大了提示小一点，如果小了，提示大一点，否则恭喜猜对啦！
import random

print('---------猜猜乐--------')
score = 0
while True:
    number = 3
    # 1. 产生一个数字
    guess_number = random.randint(1, 20)

    # 2. 输入猜数字

    # 3. 判断随机数和所猜数字的关系
    for i in range(3):
        guess = int(input('请输入您猜的数字：'))
        if guess < guess_number:
            print('猜小了！再大点，就离成功很近了！')
            number -= 1
        elif guess > guess_number:
            print('猜大了！再小点，就离成功很近了！')
            number -= 1
        else:
            print('您太幸运了，恭喜猜对啦！')
            score += number
    else:
        print('这局有点背,没准再来一局就赢了！')

    answer = input('是否继续猜猜乐？(yes/no)')
    if answer != 'yes':
        print('此次游戏共得 %d' % score)
        print('欢迎下次再来！')
        break