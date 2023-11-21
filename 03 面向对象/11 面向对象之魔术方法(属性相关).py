# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
跟容器相关魔术方法：
    。__len__(self)  # 定义当被 len() 调用时的行为(返回容器中元素的个数)
    。__getitem__(self, key)  # 定义获取容器中指定元素的行为，相当于 self[key]
    。__setitem__(self, key, value)  # 定义设置容器中指定元素的行为，相当于self[key] = value
    。__delitem__(self, key)  # 定义删除容器中指定元素的行为，相当于 del self[key]
    。__iter__(self)  # 定义当迭代容器中的元素的行为
    。__reversed__(self)  # 定义当被 reversed() 调用时的行为
    。__contains__(self, item)  # 定义当使用成员测试运算符(in 或 not in) 时的行为

跟属性相关的魔术方法：
    。__getattr__
        。触发时机：获取不存在的对象成员时触发
        。参数：一个是接收当前对象的self，一个是获取成员名称的字符串
        。返回值：必须有值
        。作用：为访问不存在的属性设置值
        。注意：getattribute无论何时都会在getattr之前触发，触发了getattribute就不会触发getattr了

    。__setattr__
        。触发时机：设置对象成员值的时候触发
        。参数：一个当前对象的self，一个是要设置的成员名称字符串，一个是要设置的值
        。返回值：无 -- 过程操作
        。作用：接管设置操作，可以在设置前之前进行判断验证等行为
        。注意：在当前方法中，无法使用 成员 = 值 的方式直接设置成员，否则会无限递归，必须借助object的设置方法完成
               object.__setattr__(参数1, 参数2, 参数3)

    。__delattr__
        。触发时机：删除对象成员时触发
        。参数：一个当前对象的self
        。返回值：无
        。作用：可以在删除成员时进行验证

    。__getattribute__
        。触发时机：使用对象成员时触发，无论成员是否存在
        。参数：一个接收当前对象self，一个是获取的成员的名称字符串
        。返回值：必须有
        。作用：在具有封装操作（私有化时），为程序考部分访问权限使用

    。__dir__
        。触发时机：dir(对象)的时候触发
        。参数：一个接收当前对象self
        。返回值：必须为序列类型(列表、元组、集合)
        。作用：可以自定义成员列表的返回值

'''
class Person:
    def __init__(self, name):
        self.name = name

    # 魔术方法之获取对象, 专门为访问不存在的属性而设置
    def __getattr__(self, item):
        if item == 'age':
            return 20
        elif item == 'gender':
            return '男'
        else:
            return '不存在此属性: {}'.format(item)

    # 作用：接管设置操作，可以在设置前之前进行判断、验证等行为    注意：真正的设置过程不能往该处加！
    def __setattr__(self, key, value):  # 只要有赋值操作，就会调用该方法！
        print(key, value)
        if key == 'phone' and value.startswith('139'):
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

        # 只要有赋值，默认调用该方法，因此此处会反复执行__setattr__方法
        # self.key = value  # RecursionError: maximum recursion depth exceeded while calling a Python object
        # 只要有赋值，千万不要出现在 __setattr__方法中，否则会有递归操作，一直递归！

# 直接访问
p = Person('老王')  # 有赋值操作，会调用__setattr__

# print(p.name)  # 老王

# 直接访问不存在的属性，报错
print(p.age) # 20 # 如果不设置，则会出现：AttributeError: 'Person' object has no attribute 'age'
print(p.phoneno)  # 不存在此属性: phoneno

# p.name = '隔壁老王'
# print(p.name)

# p.phoneno = '110'
# print(p.phoneno)

# 设置对象成员值  注意：不能通过 成员 = 值 的方式， 而要通过 object.__setattr__(参数1, 参数2, 参数3)
p.__setattr__('phoneno', '1395683')

print('=' * 50)

print(p.__dict__)  # 获取p对象自身的属性，并以字典的形式返回


