# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
多层装饰器：
    。谁距离被装饰函数最近，先执行谁
    。原函数作为第一层装饰器的 func
    。第一层装饰器的返回值 wrapper 传给第二层的装饰器，作为第二层装饰器的 func
    。第二层装饰器的返回值 wrapper 传给第三层的装饰器，作为第三层装饰器的 func
    。最后：原函数得到的地址是第二层函数的返回值 wrapper

装饰器总结：
    。作用域：
    。传参
        。函数也可以作为参数使用   --- 函数也是一个变量 ！
    。闭包
    。装饰器
        。@函数名  --- 对函数进行装饰 --- 要明白底层做了哪些动作?即要明白底层的执行原理！
        。装饰器函数的定义
            def 装饰器函数名(func):
                def wrapper(*args, **kwargs):  # 一定要做到可变，增加通用性！
                    ···
                    ···
                    # func <==> 原函数
                    func(*args, **kwargs)
                    return 返回值  # 如果原函数有返回值，则该处(内层)也要有返回值！

                return wrapper  # 装饰后的 test

            @装饰器函数名
            def test():
                pass

            test # test就是装饰器的内层函数 wrapper

        。带参数的装饰器   ---> 就是三层
        。多层装饰器  ---> 先执行最近的装饰器, 然后是第二层装饰器, ···

普通函数： # 最大的类别，用的最多
    。参数
    。返回值
    。作用域
    。闭包
    。装饰器

匿名函数： # 匿名函数和高阶函数会结合起来

递归函数： # 最后讲解，比较简单

高阶函数： # 匿名函数和高阶函数会结合起来

注：python装饰器(decorator)在实现的时候，被装饰后的函数其实已经是另外一个函数了(函数名等函数属性发生了改变)
'''
# 将 house 作为 func
def decorator1(func): # func = house
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('铺地板')
        print('刷漆')

    return wrapper  # 返回给 house

# 将第一层的 wrapper 作为第二层的 func
def decorator2(func):  # func = 第一层的 wrapper
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('买衣柜')
        print('买沙发')
        print('买电视')

    return wrapper

@decorator2  # 第二次装饰
@decorator1  # 注意：谁离被装饰函数最近，先先被装饰    --- 第一次装饰
def house():  # house = 第二层的 wrapper 的值
    print('毛坯房')

house()

'''
执行过程：
    。执行decorator1
        。毛坯房
        。铺地板
        。刷漆
    。执行decorator2
        。买衣柜
        。买沙发
        。买电视
'''