# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
列表：[] 特点： 增加、修改、查找
        常用内置函数：
                    append
                    insert
                    extend
                    remove
                    pop
                    clear
                    index
                    count
                    copy
                    sort
        排序：
            系统排序：sorted(list1) --> 返回的就是排序后的结果
                    使用：list2 = sorted(list1)
            列表自身排序：sort()
                    使用：list1.sort()
                    print(list1)  --> 排序好的列表

        翻转：reverse()
             list1 = [4, 2, 5]
             list1.reverse()  # 反转 [5, 2, 4]

元组：() 特点：查找
        常用内置函数：index count

        注意：当只有一个元素的时候，要在元素的后面加上一个逗号，否则就是 int 型数据

符号：列表和元组都是一样的， + * [] [:] in is

类型转换：
        元组 --> 列表： list(元组)
        列表 --> 元组： tuple(列表)

集合：
    ['hello', 'hello', 'world', 'hi']  # 列表
    ('hello', 'hello', 'world', 'hi')  # 元组

    特点：无序(存放顺序与打印顺序可能不一致)，不重复 (在集合中不能出现重复的元素)
    底层原理：哈希表
    哈希表特点：无序，不重复

    集合总结：可以存放不重复的元素在里面

    集合声明：
        set1 = set()  # 空集合

        # 空集合的声明
        set1 = set()  # <class 'set'>
        print(type(set1))

        # 注意：空集合不能像这样进行声明：set1 = {} --> 这样声明就是字典类型了

        # 不能直接用大花括号哦 ~
        set2 = {}  # <class 'dict'>
        print(type(set2))

        # 含有元素的集合
        set2 = {'张三', '李四'}  # <class 'set'>
        print(type(set2)

    应用场景： --> 快速去重
        # 通过集合实现快速去重
        list1 = ['hello', 'hello', 'world', 'hi']
        set1 = set(list1)
        print(list(set1))  # ['hi', 'hello', 'world']

    是否支持下标与切片：
        列表中哪些函数跟下标有关 ？
        insert(index, object)
        pop(index)
        index(object) --> index
        del list1[index]

    集合里面的函数：
        添加：add()  --> 单个元素的添加
            set1 = {1, 2, 5, 3}
            set1.add(8)  # {1, 2, 3, 5, 8}
            print(set1)  # 所有放在集合里的整型数值，默认是排好序的

             update(iterable) --> 添加一组可迭代对象，类似列表的 extend
             # 多个集合的合并
            set2.update(set1)  # 类似于列表中的 extend
            print(set2)  # {'tom', 1, 2, 3, 5, 8, 'lucy', 'jack'} --> 顺序是无序的

        删除：
            remove()  --> 删除指定的元素,如果集合中没有此元素则抛出异常 KeyError
                set1 = {1, 2, 5, 3}
                set1.remove(3)
                print(set1)

            discard()  --> 删除指定元素,如果集合中没有该元素则什么都不做
                # discard() 和 remove 类似
                set1 = {1, 2, 5, 3}
                set1.discard(1)
                print(set1)  # {2, 3, 5}
                set1.discard(9)
                print(set1)  # {2, 3, 5}

            pop()  --> 随机删除(每次都会删除第一个元素): 返回的就是被删除的元素
                set1.pop()
                print(set1)  # 随机删除集合中的任意一个元素[但实际上，每次删的是集合中的第一个元素]

            clear()  --> 清空

            del set1 --> 清空元素，并且回收对应的地址

        修改：  --> 集合自身无修改操作 ！

        查询：  --> 集合不支持查询操作 ！

        其他：
            copy()

    运算：
        + :     不支持
        * :     不支持
        [] :    不支持
        [:] :   不支持
        in :    支持
                set2 = {1, 28, 9}
                print(9 in set2)

        is :    支持
                print(set2 is set1)  # False

        &  :     交集     --> intersection()
                    result = set1 & set2  # 交集
                    print(result)  # {1, 2}

        |  :     并集     --> union()
                    result2 = set1 | set2  # 并集
                    print(result2)  # {1, 2, 3, 5, 9, 28}

        -  :     差集     --> difference()
                    result3 = set1 - set2  # 差集
                    print(result3)  # {3, 5}

                    result4 = set2 - set1  # 差集
                    print(result4)  # {9, 28}

        ^  :     对称差集   --> 两边都不一样的，即将二者各自的差集进行合并
                    set1 = {1, 2, 5, 3}
                    set2 = {1, 28, 9, 2}
                    result = set1 ^ set2
                    print(result)  # {3, 5, 9, 28}

'''
# 升序
list1 = [1, 3, 4, 5, 3, 2, 8, 5, ]
print(sorted(list1))

# 降序 方法一
list2 = sorted(list1, reverse=True)
print('方式一：', list2)

# 降序 方法二
list1.sort(reverse=True)
print('方式二：', list1)

# 降序 方法三
list1.sort()
list1.reverse()
print('方式三：', list1)

# 空集合的声明
set1 = set()
print(type(set1))  # <class 'set'>

set2 = {}
print(type(set2))  # <class 'dict'>

# 集合的定义
set2 = {'张三', '李四'}
print(type(set2))  # <class 'set'>

# 通过集合实现快速去重
list1 = ['hello', 'hello', 'world', 'hi']
set1 = set(list1)
print(list(set1))  # ['hi', 'hello', 'world']

# 集合中数字的添加
set1 = {1, 2, 5, 3}
# print(set1[0])  # TypeError: 'set' object is not subscriptable
set1.add(8)  # {1, 2, 3, 5, 8}
print(set1)  # 所有放在集合里的整型数值，默认是排好序的

# 集合中字符串的添加
set2 = set()
set2.add('jack')
set2.add('lucy')
set2.add('tom')
set2.add('tom')  # 加重复元素，不会报错
print(set2)  # 集合中的元素是无序的

# 多个集合的合并
set2.update(set1)  # 类似于列表中的 extend
print(set2)  # {'tom', 1, 2, 3, 5, 8, 'lucy', 'jack'} --> 顺序是无序的

# 集合的删除
set1 = {1, 2, 5, 3}
# remove()
set1.remove(3)
print(set1)

# pop()
set1.pop()
print(set1)  # 随机删除集合中的任意一个元素[但实际上，每次删的是集合中的第一个元素]

# clear()
set1.clear()
print(set1)

# del set1
del set1

'''
作业：
    1. 随机产生[1, 20] 不重复数字十个，并且保存在集合里面
    2. 对以上集合进行升序排列，并找出最大值和最小值
'''
import random

set1 = set()  # 定义一个空集合
count = 0  # 记录已经存在集合中的数字个数

for i in range(1000):
    rand = random.randint(1, 21)
    if len(set1) >= 10:
        break
    set1.add(rand)

print(set1)
print('集合的最大值：{} 集合的最小值：{}'.format(max(set1), min(set1)))

# 集合符号
set1 = {1, 2, 5, 3}
set2 = {1, 28, 9}

# set_merge = set1 + set2  # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(set_merge)

# print(set1 * 2)  # TypeError: unsupported operand type(s) for *: 'set' and 'int'\

# in
if 5 in set1:
    print('存在')
else:
    print('不存在')

# is
print(set2 is set1)  # False

set1 = {1, 2, 5, 3}
set2 = {1, 28, 9, 2}

# 集合运算： 交集 & 并集 | 差集 -     --> 重点记忆符号 ！
result = set1 & set2  # 交集
print(result)  # {1, 2}

result2 = set1 | set2  # 并集
print(result2)  # {1, 2, 3, 5, 9, 28}

result3 = set1 - set2  # 差集
print(result3)  # {3, 5}

result4 = set2 - set1  # 差集
print(result4)  # {9, 28}

# 集合交叉并的相关函数了解即可
result5 = set1.intersection(set2)
print('方法实现交集：', result5)  # 方法实现交集： {1, 2}

# update 方法实现交集
set1.intersection_update(set2)
print('update方法实现交集：', set1)  # update方法实现交集： {1, 2}

# 方法实现并集
set1 = {1, 2, 5, 3}
set2 = {1, 28, 9, 2}
result = set1.union(set2)  # 并集
print(result)  # {1, 2, 3, 5, 9, 28}

# 方法实现差集
set1 = {1, 2, 5, 3}
set2 = {1, 28, 9, 2}
result = set1.difference(set2)  # 差集
print(result)  # {3, 5}

# 对称差集  --> 两边都不一样的，即将二者各自的差集进行合并
set1 = {1, 2, 5, 3}
set2 = {1, 28, 9, 2}
result = set1 ^ set2  # 对称差集
print(result)  # {3, 5, 9, 28}

# 方法实现对称差集
set1 = {1, 2, 5, 3}
set2 = {1, 28, 9, 2}
result = set1.symmetric_difference(set2)  # 对称差集
print(result)  # {3, 5, 9, 28}

# discard() 和 remove 类似
set1 = {1, 2, 5, 3}
set1.discard(1)
print(set1)  # {2, 3, 5}
set1.discard(9)
print(set1)  # {2, 3, 5}
