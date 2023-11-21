# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
module_b
'''

def test_b1():
    print('----> pack2 module_b2 testb1')

def test_b2():
    '''
    将导入语句放入函数后，可以延迟导入，避免循环导入
    '''
    print('----->test_b2 start')

    # 使用到module_a
    from pack1.module_a import test_a

    # test_a()
    print('----->test_b2 end')

test_b2()

# from pack1.module_a import test_a