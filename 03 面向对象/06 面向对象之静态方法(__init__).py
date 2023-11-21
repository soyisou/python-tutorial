# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
类方法，静态方法：
工具方法

类方法：
    定义格式：
        @classmethod
        def 类方法名(cls, 参数):
            pass
    使用：
        。类名.方法()
        。也可以通过： 对象.方法名() --- 了解

静态方法：
    定义格式：
        @staticmethod
        def 方法名(self):
            pass
    使用：
        。类名.方法名()

二者共同点：
    。无论是类方法还是静态方法，都能被对象访问
    。二者都可以通过：类名.方法名() 调用方法


二者很类似，唯一的区别：
    。classmethod有 cls参数，而 staticmethod没有参数
    。classmethod可以通过 cls访问类的属性，而 staticmethod方法只能通过类名访问
'''
class Utils:
    # 类属性
    version = '1.0'

    # 类方法
    @classmethod  # 装饰器
    def conn_db(cls):  # cls其实就是类对象本身
        print('classmethon--->',cls)
        print('加载数据库驱动程序，当前的版本号是：', cls.version)
        print('数据库建立连接成功！')

        # cls.select_data()

    # 静态方法， 不依赖对象self，也不依赖类cls
    @staticmethod  # 装饰器
    def select_data():
        print('查询数据库的数据，当前版本号是：', Utils.version)
        Utils.conn_db()  # 不用传cls，只要是类方法，默认会传

print('=' * 50 )
# 类方法的调用
Utils.conn_db()
print('Utils:', Utils)

print('=' * 50 )
# 类方法能够被对象调用？   能调用
u = Utils()
u.conn_db()  # 对象调用 conn_db(cls)  --> cls 仍然是类对象本身<class '__main__.Utils'>
print('u==', u)

print('=' * 50 )
# 思考：类方法中能否访问对象属性？

# 静态方法的调用
Utils.select_data()

print('=' * 50 )
# 静态方法能被对象访问么？ 能
u = Utils()
u.select_data()

# 思考：类方法中能否调用静态方法？ 可以
print('=' * 50)
Utils.conn_db()

# 思考：静态方法中能够调用类方法？ 可以

# 思考 1：类方法中能否访问对象属性？  不能

# 思考 2：类方法，静态方法中能否调用普通方法？  不能
'''
用类方法就单独用类方法的特点就ok了，就不用再访问对象的了，不然的话就没必要定义类方法了，它不依赖于对象
'''