# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
语法错误
    。IDE工具自动报红线
运行时错误
    。只有运行起来才知道那块出错
    。类别
        。ValueError
        。TypeError
        ···
'''

def func():
    print('-----> func')

# func(1)  # TypeError: func() takes 0 positional arguments but 1 was given

def div(a, b):
    return a / b

r = div(5, 2)
# r = div(4, 0)  # ZeroDivisionError: division by zero
print(r)

# r = div('10', '5')
# print(r)  # TypeError: unsupported operand type(s) for /: 'str' and 'str'

# 异常会终止后面代码的执行！因此，我们通常需要进行异常处理，将后面的代码正常执行。
# print('-------')

# 异常处理（处理异常）
'''
基础格式
    。格式
        try···except  # 也叫捕获异常
    
    。基础格式
        try:
            可能出现异常的代码[可能]
        except:
            如果存在异常执行的代码部分
    。扩展格式
        try:
            可能出现异常的代码
        except 异常类型1:
            如果存在异常执行的代码部分
        except 异常类型1:
            如果存在异常执行的代码部分
        ···
        
        Exception 是所有异常类型父类，Exception通常要放在最后，用于接收未知的异常类型
        如果想要获取错误xxxErro的报错信息，需要使用此种格式：
            except 异常类型 as 名字[如：erro]:  # error 即对象名
                ···
                do something
        
        try:
            可能出现异常的代码[可能]
        except:
            如果存在异常执行的代码部分
        else:
            没有遇到异常执行的代码
        finally:  #无论是否存在异常都会执行的代码部分
            必执行的代码
            
'''
# 除法运算
def div1(a, b):
    # 无异常执行此处代码
    try:  # 若有异常，则会扔出异常对象。怎么往外扔异常？借助 raise
        # 将字符串的类型也转换为可计算的整数类型
        a = int(a)
        b = int(b)  # 例如， t = TypeError('错误提示信息')  raise t
        return a / b
    # 有异常才会进入except执行此处代码
    # 说白了，Except就是用来接收异常对象的，底层：isinstance(obj, TypeErro) err = t
    except TypeError as err:  # 类型错误 ---- 继承Exception
        print('类型错误！', err)  # err就是错误对象
    except ZeroDivisionError as err:  # 除数为零错误---- 继承Exception
        print('除数为零错误！', err)
    except Exception as err:  # 异常 --- 大类型！ as err 仅仅是取个别名而已
        print('出错啦！', err)

print('===========')  # 该行代码正常执行

r = div1(10, 5)
print(r)  # 2.0

r = div1('10', '5')
print(r)  # 类型错误！

r = div1(2, 0)
print(r)  # 除数为零错误！division by zero [打印的不是异常对象,而是字符串,说明底层重写了__str__]

r = div1('af', 'afadf')
print(r)

# 思考：能不能将Exception往上放？不能，Exception会直接接收所有异常！下面的异常永远捕捉不到！因此千万不要将其放在最前端
