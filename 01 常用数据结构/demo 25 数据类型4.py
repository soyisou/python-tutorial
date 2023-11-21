# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
语句：
    str:
        1. 声明
        2. (下标|索引) + 切片
            索引：两种起名方式
            0 ~ len(s) - 1
            -(len(s)) ~ -1

            方向：s[start:end:step]
            正 step: 从左向右
            负 step: 从右向左
        3.字符串内置方法：
            查找：find() index() rfind() rindex()
            替换：replace()
            分割：split()
            合并：join()
            大小写转换：
            判断： isupper(), islower() ···
            去除空格：strip()
            格式化：format()

    list:
        1. 定义：
            list1 = []
            list1 = [1, 3, 5, 6]
            list4 = list([2, 4, 6, 8])  # list只能放可迭代对象，且只能是一个参数

        2. 列表支持下标， 也是切片（类似字符串）
            [2, 4, 5]
        3.列表中的内置函数：
            添加：
                append()
                insert(index, object)
                extend(iterable)

            删除：
                remove(object)
                pop()
                pop(index) ~ del list[index] 类似
                clear()
                del list1

            更新：
                list1[index] = 新值

            查找：
                list1.index(object) --> index 若找不到，则报错

    其他函数：
        补充：join()
        copy()


'''
# 均表示声明了空列表
list1 = []
list2 = list()
print(type(list2))

list3 = [1, 3, 5, 7]
list4 = list([2, 4, 6, 8])  # list能放的是可迭代对象，且只能是一个
list5 = list4[:3]  # [2, 4, 6]
list6 = list3[4:0:-1]  # [7, 5, 3]
print(list3, list4, list5, list6)

idx = list6.index(5)  # 1
print(idx)

# 学编程不要怕报错，要学会改错，第一看类型，第二看行号
# idx = list6.index(9)  # ValueError: 9 is not in list
# print(idx)



