# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
简易版停车管理系统：
    参数：
    停车场最多停车数：max_car
    当前停车数：cur_car
    当前停车列表：car_list = []

    入停车场：
    1. 如果没有达到最多停车数，则允许停车
    2. 计入入场的时间，使用 time.time() 的到的是自 1970 年 1 月 1 日， 00:00:00到现在的秒数
    3. 显示剩余停车位数

    出停车场：
    1. 判断该汽车是否进入，如果进入，则删除 car_list 里面相关的信息
    2. 如果该汽车从未进入，则通知管理员：
    3. 计入出场时间，使用 time.time() 的到的是自 1970 年 1 月 1 日， 00:00:00到现在的秒数计时收费
       停车费 5 元 / 小时
    4. 显示剩余停车位数

    查询系统：
    判断车是否在停车场中，如果在进场的时间是：XX:XX:XX (时：分：秒)

    退出系统：
    退出停车管理系统
'''
import time
import random

print('=' * 50)
print('--------------欢迎来到深圳大学停车场------------------')
print('=' * 50)

car_list = []  # 停车场
pos_list = ['1号车位', '2号车位', '3号车位', '4号车位', '5号车位']  # 剩余车位标号信息
MAX_CAR = 5  # 最大停车量
cur_car = 0  # 当前停车量

while True:
    choice = input('请选择功能：1. 进入停车场 2. 出停车场 3. 查询车辆 4.查询所有车辆 5. 退出系统')
    if choice == '1':
        # 进入停车场
        if cur_car < MAX_CAR:
            car_number = input('请输入车牌号码：')
            # 计入入场时间
            start = time.time()  # 时间戳
            # 随机选择车位
            ran_pos = random.choice(pos_list)
            # 车辆相关信息
            car_massage = [car_number, start, ran_pos]
            # 将该车及停车位置添加到停车场
            car_list.append(car_massage)
            cur_car += 1
            # 该车位已经被占用
            pos_list.remove(ran_pos)
            print(car_number + '停车成功！')
        else:
            print('车位已被占满，请选择其他停车场或者等候！')

        pass

    elif choice == '2':
        # 出停车场
        print('--------------离开深圳大学停车场------------------')
        out_carno = input('请输入车牌号码：')
        # 查询
        for car_massage in car_list:
            if out_carno in car_massage:
                # 出去
                car_list.remove(car_massage)

                # 开始计算费用
                end = time.time()
                hour = (end - car_massage[1]) / 3600 # 差值分钟
                money = hour * 5
                print('车牌号：{} 停车时间：{} 费用：{:.2f}元'.format(out_carno, hour, money))
                print('缴费中, 请稍等 ···')
                time.sleep(2)
                print('缴费成功，欢迎下次再来！')

                # 将占用的停车位归还
                pos_list.append(car_massage[2])

                # 当前停车位数量 - 1
                cur_car -= 1
                break

    elif choice == '3':
        # 查询车辆信息
        print('--------------车辆信息查询------------------')
        search_no = input('请输入要查询的车牌号：')
        for car_massage in car_list:
            # car_massage 是一个列表 ['京A888', 465464654, '3号车位']
            if search_no in car_massage:
                print('该车在停车场中！')
                break
            else:
                print('停车场中没有此车：', car_number)
                break

    elif choice == '4':
        # 查询所有车辆
        print('------------所有车辆信息查询----------------')
        for car_massage in car_list:
            print(car_massage[0], car_massage[1], car_massage[2])

    elif choice == '5':
        # 退出停车管理系统
        ans = input('您是否确定退出停车管理系统 ？(yes/no)')
        if ans.lower() == "yes":
            print('即将退出停车管理系统 ···')
            time.sleep(1)
            print('系统已关闭！')
            break
    else:
        print('输入错误，请重新选择：')
