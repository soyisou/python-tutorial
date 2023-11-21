# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
函数的种类：
    。普通函数
    。匿名函数
    。高阶函数
    。递归函数
'''
count = 0

# 递归函数：在函数定义的时候，调用函数自身，递归函数
# 定义递归函数：1. 递归函数必须要有出口  2.不断向出口靠近
def func():
    global count
    if count == 100:
        print('----->count', count)
    else:
        print('----->count', count)
        count += 1
        func()

# 函数调用
# func()

# 1-50 的累加和（递归的方式实现）: 1 + 2 + 3 + 4 + 5 + 6 + ··· + 50
def get_sum(start, end):
    if start == end:
        return end
    else:
        return start + get_sum(start + 1, end)

t = get_sum(1, 5)
print(t)