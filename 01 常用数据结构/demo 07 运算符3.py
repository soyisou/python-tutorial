# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
"""
成员运算符：in, not in
身份运算符: is, is not
三目运算符: if else
运算符的优先级：
"""

# 成员运算符：in not in
names = ['张鹏', '刘旺', '王宁', '孙杨']
print('孙杨' in names)  # 判断一个元素是否在另一个 '容器'中，如果在 True, 否则 False
print('刘丽' in names, '刘丽' not in names)

s1 = 'abced'
print('a' in s1)

# 身份运算符： is, not is 比较地址
s1 = 'abc'
s2 = 'abc'
print(s1 == s2)  # 字符串驻留区(inter 机制) 类似于 小整数对象池
print(s1 is not s2)  # False

# 三目运算符：格式：结果 1 if 条件 else 结果 2
result = 5 + 6 if 5 > 6 else 5 - 6  # 在做列表推导式的时候，会用到此格式
print(result)  # -1

# 运算符的优先级
print(not 3 + 5)  # 先计算 3 + 5, 再计算 not

"""
总结：
常量：Python弱类型 赋值为什么类型，就为什么类型
     只要变量值为全大写，就默认为常量(不是规定，而是约定)

变量：
1. 变量定义的格式 变量名 = 值
2. 变量起名： 命名规范 5 条
3. 值：类型
    str, int, float, bool, bytes
    list, set, dict, tuple
4. str:' '," ", 三引号 + 
    str 与 int 转换：str(), int()
    
    print('hello' + '100')  # 左右连接，左右类型要相同，否则要进行类型转换
    
    s1 = '90'
    s2 = int(s1)
    print(type(s2), s2)
    
    ss = 88
    print('hello' + str(ss))
    
5. 运算符：
    算术：
    赋值：
    关系：
    逻辑：
    位： 进制： 十进制，二进制，八进制，十六进制
        进制之间的转换
        负数：补码，反码
        系统：bin(), int(), oct(), hex()
        &, |, ~, ^, >>, <<
    成员：in, not in
    身份： is, is not
    三目：结果1 if 条件 else 结果2
"""