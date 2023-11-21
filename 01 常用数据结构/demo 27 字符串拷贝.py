# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
copy(): 复制
'''
list1 = ['张三', '赵四', '王五', '赵六']

list_copy = list1.copy()
print(list1)
print(list_copy)

print(id(list1))  # 33238248
print(id(list_copy))  # 33237864

print(list1 is list_copy)  # False

list1.pop()
list1.append('二狗')
print('----->改变后的：', list1)
print('----->list1副本：', list_copy)

# 浅拷贝

# python的内存管理中有个 intern 机制，字符串驻留区
print('=' * 30)
s1 = 'hello'  # s1 -> hello <- s2
s2 = 'hello'  # 又开了一块新的地址，将驻留区的内容地址按照 s1 的情况再复制一份, 即s1和s2地址不同，仅内容一样而已
print(s1 is s2)  # True


