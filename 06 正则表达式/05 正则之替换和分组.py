# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
re模块中的：
    。sub(pattern, rep1, str)替换
    。rep1可以是 str类型，也可以是 callable类型

分组操作：
    。分组命名匹配
'''

import re

s = 'xiaohua=20 xiaoming=21 xiaohong=19'
s = re.sub(r'\d+', '20', s)
print(s)  # xiaohua=20 xiaoming=20 xiaohong=20
#
print('=' * 50)
# 思考1：替换，且年龄都加一岁，怎么处理？
'''
def change(match_obj):
    print(match_obj)
    return '21'
<re.Match object; span=(8, 10), match='20'>
<re.Match object; span=(20, 22), match='20'>
<re.Match object; span=(32, 34), match='20'>
'''

def change(match_obj):
    # 返回匹配内容 --- str类型
    content = match_obj.group()
    # 还可以往里面加一些我们需要的判断条件
    result = int(content) + 1
    return str(result)

s = re.sub(r'\d+', change, s)
print(s)  # xiaohua=21 xiaoming=21 xiaohong=21

print('=' * 50)

'''
分组命名匹配: 
    。()表示分组
    。分组常和捕获想关联  --- group(1) group(2)
    。() + \number: \number表示引用组匹配的内容
'''
# 获取名字: Jack Tom Lucy Linda
s = 'hello Jack'

# 思考2：如何使用正则实现呢？
res = re.search(r'(jack|tom|lucy|linda)', s, re.I)  # 一个()表示一组，如果多个成员可以使用'|'表示或者关系
print(res.group())  # Jack

print('=' * 50)
s = 'hello Linda'
# 思考3：能否有多个组呢？可以，分两组！ 注意：分组的时候，要保持格式与之前的内容一致！比如本例当中，分组之间要有空格！
match_obj = re.search(r'(hi|hello) (lucy|linda)', s, re.I)  # 一个()表示一组，如果多个成员可以使用'|'表示或者关系
if res:
    print(match_obj.group())  # hello Linda
else:
    print('None!')

print('=' * 50)
# 思考3：如果想要取到每一组匹配的内容，怎么办呢？
print(match_obj.group(1))  # hello
print(match_obj.group(2))  # Linda

print('=' * 50)
# 思考4：如何匹配邮箱呢？  126,163，qq 而且必须符合邮箱的格式 xxx@163.com   xxx的长度4-16位之间

email = input('请输入邮箱号码：')
match_obj = re.search(r'^(\w{4,16})@(126|163|qq).com$', email)
if match_obj:
    email_name = match_obj.group(1)
    email_type = match_obj.group(2)
    print('符合邮箱格式！')  # 符合邮箱格式！
    print('邮箱名:{} 邮箱类型:{}'.format(email_name, email_type))  # 邮箱名:878665865 邮箱类型:qq
else:
    print('不符合邮箱格式！')

