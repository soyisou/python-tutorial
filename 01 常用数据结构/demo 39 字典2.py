# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

'''
集合：
    特点：无序，不重复
    list1 = [1, 2, 4]
    set1 = set(list) --> {1, 2, 4}


    函数：
        remove()
        discard()
        pop()
        clear()
        del set1

    更新： 查找 :index

    其他方法：
        运算：intersection()  union()  difference()  symetric_difference()

       符号： & | - ^

字典：
    常用：
        key : value
    声明：
        dict1 = dict()
        dict1 = {}
        dict1 = {'a': 50}

    获取：
        dict1[key]  --> 报错
        dict1.get(key)  -- > None
        dict1.get(key.default)  --> default

    内置函数：
        添加和更新：
            dict1[key] = value
        删除：
            pop(key)
            popitem()
            clear()
            del dict1
        获取：
            keys()
            values()
            items()

        for key, value in dict1.items():
            print(key, value)

        for e in dict1:
            print(e)

    转换：
        list --> 字典     格式，如： [('a', 100), ('b', 99)]
        字典  --> list    格式，如：{'a': 100, 'b': 99}
'''