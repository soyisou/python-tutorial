# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
"""
停车管理系统：
    1.进场
    2.出场
    3.查询
    4.统计
    5. 退出
"""
car_location = []  # 停车场
while True:
    choice = input('请选择功能：1.进场 2.出场 3.查询 4.统计 5. 退出')
    if choice == '1':
        car_in = input('请输入车牌号：')
        print(car_in + ' 进场了！')
        car_location.append(car_in)

    elif choice == '2':
        car_out = input('请输入车牌号：')
        if car_out in car_location:
            car_location.remove(car_out)
        else:
            print('%s不在停车场！' % car_out)
            continue
        print(car_out + ' 出场了！')

    elif choice == '3':
        car_inquire = input('请输入要查询的车牌号：')
        if car_inquire in car_location:
            print('车辆在场')
        else:
            print('车辆不在')

    elif choice == '4':
        print('停车场使用数量：%d' % len(car_location))

    elif choice == '5':
        print('退出系统：')
        break
    else:
        print('输入有误,请重新输入：')