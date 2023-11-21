# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
数据类型：字符串
'' “” 三引号

场景：
    截取字符串

    判断字符串中的某一部分

知识点：
    切片
    运算符
    内置字符串方法: find() index rindex()
        find 和 index的区别：
        功能类似，但在没有找到元素的时候处理方式是不一样的！
        没有找到，find 返回 -1，index 报错
'''

# 1. 切片
s = 'abcdefg'

# 下标 索引 角标 idex
print(s[0])

'''
for i in s:
    print(i)
'''

print(len(s))  # 返回字符串长度

index = 0  # 所有字符串的下标都是从 0 开始的
while index < len(s):
    print(s[index])
    index += 1

# 使用一下负数的下标
# print(s[-1])
print(s[-4])

# 切片格式：字符串 [start:[stop:[step]]] 包含start，不包含stop

# 逆向的话，一定要先控制方向 ！

# s = 'abcedefg'
print('='*30)
print(s[1:-1])  # 默认的取值方向都是从左往右
print(s[:-4])
print(s[::3])  # step 除了有步长功能外，还有控制方向.如果step是负数，就表示往左
print(s[::-1])  # 逆序

# abcde
print('=' * 10)
s = 'abcdefg'

# s = 'abcdefg'
# 取dec
print(s[4:1:-1])  # edc
print(s[-3:-6:-1])  # edc

# 取cba
print(s[2::-1])  # cba
print(s[-5::-1])  # cba

# 字符串是底层封装好的类
ss = 'https://www.baidu.com'
t = ss.find('/')  # 6, Return -1 on failure
p = ss.index('/')  # 6, Raises ValueError when the substring is not found.
tt = ss.find('/', 6)
print(t, p, tt)

pp = ss.rfind('/')  # 右侧搜索
print(pp)  # 7