# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
类方法:
    。特点：
        。好用
        。当我们需要用到一个类工具，还想用的时候不用创建对象，直接用类名找到该方法，这就是工具方法，就是我们可以
         直接通过类名即可访问该方法，不需要依赖对象，不需要创建对象哦 ~
        。我们写的类方法比较少，一般都是对象方法，我们在看源码的时候，可能会看到类方法，我们知道即可。
静态方法：
工具方法
'''
# 工具类  --- 何为工具？在开发的时候，只要需要连接数据库，无需创建对象，而且使用起来比较方便
# class Utils:
#     def conn_db(self):  # self表示对象本身，有了对象了，我才用self
#         pass
#
#     def select_data(self):
#         pass

# 每次用到conn_db()都得创建一个对象太麻烦了！有没有更简便的方法呢？  有嘀！
# u = Utils()
# u.conn_db()

# 工具类  --- 何为工具？在开发的时候，只要需要连接数据库，无需创建对象，而且使用起来比较方便
class Utils:  # 类加载 --> 空间 --> cls [类对象本身, 即Utils本身]
    # 类属性
    version = '1.0'

    # 类方法
    @classmethod
    def conn_db(cls):  # cls 就是类对象本身！
        # 类方法  好处：只要创建类方法，无需创建对象，可直接通过类名即可访问类方法！
        print('加载数据库的驱动程序,当前版本号是：', cls.version)  # 方法是没法直接拿属性的！cls是类本身！
        print('数据库建立连接成功！')

    def select_data(self):
        print('hello world!')

Utils.conn_db()  # 类方法，好处：只要创建类方法，无需创建对象，可直接通过类名即可访问类方法！
# Utils.select_data()
# print(Utils.version)  # 1.0

# 思考：类方法能否被类对象调用？  可以！
u = Utils()
u.conn_db()