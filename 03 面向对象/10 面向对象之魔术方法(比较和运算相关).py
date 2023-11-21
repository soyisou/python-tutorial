# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
运算相关的魔术方法：
    # 对象的比较
    。__gt__  -->   >
    。__lt__  -->   <
    。__eq__  -->   equals ==
    。__le__  -->   <=
    。__ge__  -->   >=
    。__ne__  -->   !=

算术运算相关的魔术方法：
    。__add__(self, other)  # 定义加法的行为
    。__sub__(self, other)  # 定义减法的行为
    。__mul__(self, other)  # 定义乘法的行为
    。__truediv__(self, other)  # 定义真除法的行为
    。__floordiv__(self, other)  # 定义整数除法的行为
    。__mod__(self, other)  # 定义取模算法的行为
    。__divmod__(self, other)  # 定义当被 divmod() 调用时的行为
    。__pow__(self, other[, modulo])  # 定义当被 power() 调用或 ** 运算时的行为
    。__lshift__(self, other)  # 定义按位左移的行为
    。__rshift__(self, other)  # 定义按位右移的行为
    。__and__(self, other)  # 定义按位与的行为
    。__xor__(self, other)  # 定义按位异或的行为
    。__or__(self, other)  # 定义按位或的行为
    ···

一元运算相关魔术方法：
    。__pos__(self)  # 定义正号的行为
    。__neg__(self)  # 定义负号的行为
    。__abs__(self)  # 定义当被 abs() 调用时的行为
    。__invert__(self)  # 定义按位求反的行为

类型转换相关魔术方法：
    。__complex__(self)  # 定义当被 complex()调用时的行为（需要返回恰当的值）
    。__int__(self)  # 定义当被int()调用时的行为（需要返回恰当的值）
    。__float__(self)  # 定义当被float()调用时的行为（需要返回恰当的值）
    。__round__(self[,n])  # 定义当被round()调用时的行为（需要返回恰当的值）
    。__index(self)__
        。当对象是被应用在切面表达式中时，实现整型强制转换
        。如果你定义了一个可能在切片时用到的定值的数值型，你应该定义 index
        。如果index被定义，则int也需要被定义，且返回相同的值

'''
class Cat:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    # 对象的比较：小于
    def __lt__(self, other):  # other相当于符号后面的值
        return self.age < other.age

    # 对象的比较：大于
    def __gt__(self, other):
        return self.age > other.age

    # 对象的比较：等于
    def __eq__(self, other):
        # print('---->')  # 两个对象相等的比较，优先进入__eq__, 不匹配再进入其他比较的方法
        return self.age == other.age

    # 对象的加运算
    def __add__(self, other):  # 仅支持两个对象之间的操作 ！
        return self.age + other.age

    # 将对象转为str
    def __str__(self):
        return str(self.age)  # 转成str

    def __int__(self):
        return self.age

c1 = Cat('花花', 2)
c2 = Cat('喵喵', 1)
c3 = Cat('嘀嘀', 3)

print(c1 < c2)  # 直接比较：'>' not supported between instances of 'Cat' and 'Cat'
print(c1 > c2)  # 直接比较：'>' not supported between instances of 'Cat' and 'Cat'
print(c1 == c2)  # 直接比较：'>' not supported between instances of 'Cat' and 'Cat'

# 两个猫对象相加
result = c1 + c2
print(result)  # 3

# 定义 __int__魔术方法
result = c1 + c2 + int(c3)  # 6
print(result)

