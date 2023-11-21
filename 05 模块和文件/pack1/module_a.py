# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
循环导入（引入）
    。一个模块用另一个模块，另一个模块又用本模块
    。避免
        。方法1：重构代码
            。缺点：当代码比较多的时候，需要付出的代价比较大
        。方法2：当导入的语句放在函数中[调用处]  --- 加载不是调用，函数里面的代码不会执行
            def 函数名():
                from ··· import ···
                pass
        。方法3：将导入语句放在最后    --- 注意：是特殊场景才能够使用的！
'''
# from pack2.module_b import test_b1

def test_a():
    print('----> test_a start')

    # 调研 module_b
    from pack2.module_b import test_b1
    test_b1()
    print('-----> test_a end')

if __name__ == '__main__':
    '''
    出现了循环引入问题，一个模块用另一个模块，另一个模块又用本模块
    
    思考：如何避免出现循环导入问题呢？
    '''
    # 调用test_a
    test_a()  # importError: cannot import name 'test_b1' from 'pack2.module_b'