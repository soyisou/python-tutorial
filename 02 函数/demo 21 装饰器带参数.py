# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
装饰器参数：
    。三层函数实现
        def 装饰器名(装饰器参数):  # 可不是函数哦
            def second(函数参数):  # 前两层是系统搞定的
                def third(*args, **kwargs):
                    ···
                    ···
                return third
            return second

注：python装饰器(decorator)在实现的时候，被装饰后的函数其实已经是另外一个函数了(函数名等函数属性发生了改变)
'''
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('----start----')
#         func()
#         print('----end----')
#
#     return wrapper


def decorator(number):  # number = 10
    print('----->1')  # step1

    def decorator1(func):  # 加载, step4
        print('----->2')

        def wrapper(*args, **kwargs):
            print('----start----')
            func(*args, **kwargs)
            print('----end----')

        print('----->3')
        print('---->wrapper', wrapper)
        return wrapper

    print('----->4')  # step2
    print('---->decorator1', decorator1)
    return decorator1 # step3

@decorator(10)  # 注意：只要是装饰器带参，他是 3 层的函数嵌套
def show():
    print('调用 show 函数')

show()
print('---->show', show)

'''
执行过程：(个人总结)
1. 从 @decorator处开始执行，将能执行的语句全部执行，并将第二层的函数名返回
    。执行 print('----->1')
    。执行 print('----->2')
    。执行 return decorator1
    。执行函数调用show()，并顺序执行其中的语句
    。执行装饰器内层函数wrapper()
    。将wrapper地址赋值给show

2. show = wrapper, 即装饰后二者地址相同，此时的show已经不再是之前的show,而是wrapper
'''