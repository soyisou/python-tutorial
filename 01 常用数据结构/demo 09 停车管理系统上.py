# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
"""
多重if条件：
场景：
1. 停车管理系统
    练习：
    进场
        输入车牌
        print('**进场了')
    出场
        输入车牌
        print('**出场了')
    查询
        输入车牌
        判断有没有进场
2. 银行管理系统
    办卡 存钱 取钱 修改密码 账户冻结 账户解锁 找回密码 转账
"""
import random

choice = int(input("请选择需要办理的功能：（1. 办卡 2. 存钱 3. 取钱 4. 修改密码 5. 解锁 6. 转账 7.退出):"))

if choice == 1:
    # 办卡
    print('办卡功能')
    d1 = random.randint(0, 9)
    d2 = random.randint(0, 9)
    d3 = random.randint(0, 9)
    card = str(d1) + str(d2) + str(d3)
    print('您办理的卡号是：%s' % card)

elif choice == 2:
    # 存钱功能
    print('存钱功能：')
elif choice == 3:
    # 取钱功能
    print('取钱功能：')
elif choice == 4:
    print('修改密码：')
elif choice == 5:
    print('解锁功能：')
elif choice == 6:
    print('转账功能：')
elif choice == 7:
    print('推出系统：')

"""
总结：条件语句

1.  # 有可能每个条件都成立，即都执行
    if 条件：
        条件成立执行的语句
    if 条件1：
        条件成立执行的语句
    if 条件2：
        条件成立执行的语句
    ···

2. # 从上往下扫，若满足某个条件，则只能执行该条件，便不再会执行其他条件了
    if 条件1：
        条件1成立执行的语句
    elif 条件2：
        条件2成立执行的语句
    elif 条件2：
        条件3成立执行的语句
    ···

3. if 的嵌套
        if 条件A:
            ···
            if 条件B:
                ···
                if 条件C:
                    ···
                else:
            else:
        else:
            ···
"""