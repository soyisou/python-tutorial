# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
字符串能够支持的符号：
    +: str + str
    *: str * 5
    in: 内容 in 字符串 --> bool
    is: 两个字符串判断地址是否相等
    ==: 比较内容
    []: 下标或切片 s[0] s[:5]
    %: 字符串的格式化
    '名字：%s' % name
'''
print('abc' * 5)

s = 'abcdef'

if 'a' in s:
    print('出现')
else:
    print('没有找到')

