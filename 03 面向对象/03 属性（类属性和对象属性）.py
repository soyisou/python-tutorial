# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
类与对象：
    。属性
        。类属性：在类空间中的属性，既可以被类访问，也可以被对象访问[对象没有的情况下才访问，对象有的话就不访问了]
        。对象属性：在对象空间中的属性，只能被当前的对象访问

    。创建方式
        。类属性：
            class 类名：
                属性 = 值  # 类属性
        。对象属性：
            。方式一：
                。步骤：
                    。先创建对象： 对象 = 类名()
                    。对象.属性名 = 值  --》 在空间中创建(添加)了对象属性
            。方式二：
                。依赖 __init__() 完成
'''
class Book:
    # 类属性
    bname = '盗墓笔记'
    price = 39

print(Book)
print(id(Book))

print(Book.bname)

# 创建对象
b1 = Book()  # 刚创建对象时，b1里面是没有内容的
print(b1.bname)  # 搜索原则：先搜索对象自身的空间，如果没有，则去类中(模型)中去找
# print(b1.author)  # 都没有，报错

b2 = Book()  # 刚创建对象时，b2里面是没有内容的
print(b2.bname)

Book.bname = '鬼吹灯'
print(b1.bname)  # 鬼吹灯
print(b2.bname)  # 鬼吹灯

# 通过对象修改bname的值
# 对象的动态赋值：如果对象中不存在属性 bname，则会在对象空间中动态添加属性 bname
b1.bname = '寻龙诀'  # 对象属性的自动添加(先在对象自身找，发现没有bname属性，于是自动添加bname = '寻龙诀')
b2.name = '怒晴湘西'
print(Book.bname)  # 鬼吹灯   --- 类属性
print(b1.bname)  # 寻龙诀   --- 对象属性
print(b2.bname)  # 怒晴湘西  --- 对象属性