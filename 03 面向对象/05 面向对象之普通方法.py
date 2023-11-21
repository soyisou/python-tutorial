# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
面向对象：
    。类
        class 类名：
            属性
            方法

    。对象
        对象 = 类名()
    。属性
        。类属性
        。对象属性

方法：
    。普通方法
        。定义格式
            def 方法名(self, 参数 1, 参数 2···):
                pass
        。调用
            。都要依赖对象调用方法
                。对象名.方法(参数)

            注：在调用过程中，会默认传递 self对象，self表示的是对象本身
        。访问属性
            。self.属性名
                。self.属性名 = 值  --> 改变属性的值
        。访问普通方法
            。self.方法名(参数)
    。类方法
    。静态方法
    。魔术方法
'''
class Card:
    def __init__(self, cardno, phoneno):
        self.money = 0
        self.cardno = cardno
        self.phoneno = phoneno

    # 存钱
    def save_money(self, money):
        self.money += money
        print('卡号:{} 存钱成功，当前的余额是:{}'.format(self.cardno, self.money))

    # 取钱
    def withdraw_money(self, money):
        if money < self.money:
            self.money -= money
            print('卡号:{} 取钱成功!'.format(self.cardno))
            # 调用'兄弟'方法
            self.show()
        else:
            print('账户金额不足！')

    def show(self):
        print('=' * 20 + '用户的详细信息' + '=' * 20)
        print('卡号是: {}, 余额: {}, 手机号码: {}'.format(self.cardno, self.money, self.phoneno))


# 创建对象
card1 = Card('001', 18339117550)
card1.save_money(10000)
card1.save_money(50000)
card1.withdraw_money(50000)

# card2 = Card('002', 13899004567)
# print(card2.money)