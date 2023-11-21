# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8

'''
异常：
    try:
        可能出现异常的代码[可能]
    except:
        如果存在异常执行的代码部分
    else:
        没有遇到异常执行的代码
    finally:  #无论是否存在异常都会执行的代码部分
        必执行的代码

    注意：
        。如果代码有返回值 + finally, 则肯定会执行 finally里面代码部分!
        。如果 finally之前有 return语句，则先执行 finally语句，再执行 return语句
        。如果 finally紧跟着还有 return语句，则执行完这两条语句后，再执行之前的 return语句
        。无论是否有异常，都会执行 finally里面的内容
        。finally应用场景：
            。在开发的时候，数据库的连接问题，或者网络的连接问题  --- 在最后的时候，使用finally释放资源，如: conn.close()
'''

def func(opr):
    result = 0
    try:  # try不能单独使用，必须结合except
        n1 = int(input('输入第一个数：'))
        n2 = int(input('输入第二个数：'))

        if opr == '+':
            print('正在进行加法运算···')
            result = n1 + n2
        elif opr == '-':
            print('正在进行减法运算···')
            result = n1 - n2
        elif opr == '*':
            print('正在进行乘法运算···')
            result = n1 * n2
        elif opr == '/':
            print('正在进行除法运算···')
            if n2:
                result = n1 / n2
            else:
                result = 0

        # return result  # 即便加了return语句，也会执行后面的finally语句，只不过finally延迟执行，再执行return语句
    except Exception as err:
        print('出错啦!', err)
    else:  # try和else是绑定使用的，如果try执行了，就不会执行else里面的语句了
        print('正常执行！')
        return result
    finally:  #无论是否存在异常都会执行的代码部分
        print('我是finally!')  # finally执行完后，才会执行return语句
        return result + 1

r = func('+')
print(r)