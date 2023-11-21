# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
正则之分组
'''

import re

# 思考1：1开头，不是以4、7结尾的手机号(11位)，或者 010-34567897 | 0311-37647326

'''
phone = input('输入手机号或者座机号：')
match_obj = re.search(r'1\d{9}[^47]|\d{3,4}-\d{8}$', phone)  # | 表示或者！
if match_obj:
    print('匹配成功！')
else:
    print('匹配失败！')

其余均正常，但是如果最后是1833911755a? 是否正确呢？ 不能！问题出现在哪里呢? [^47]
'''

# 思考2：怎么解决这个问题呢？ 将[^47]改为[0-35689]即可！
# phone = input('输入手机号或者座机号：')
# match_obj = re.search(r'1\d{9}[0-35689]|\d{3,4}-\d{8}$', phone)  # | 表示或者！
# if match_obj:
#     print('匹配成功！')
# else:
#     print('匹配失败！')


# 标签
'''
<img class="currentImg" id="currentImg" onload="alog &amp;&amp; alog('speed.set', 'c_firstPageComplete', +new Date); alog.fire &amp;&amp; alog.fire('mark');" src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic.soutu123.com%2Felement_origin_min_pic%2F17%2F03%2F05%2Ff4795c1d96ebfdc3b56973d3338f843f.jpg%21%2Ffw%2F700%2Fquality%2F90%2Funsharp%2Ftrue%2Fcompress%2Ftrue&amp;refer=http%3A%2F%2Fpic.soutu123.com&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=jpeg?sec=1639912150&amp;t=f98faf35030447933052d44e3631e6e2" width="461.29032258065" height="462" style="top: 93px; left: 0px; width: 488px; height: 488.751px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">
'''

# 思考3: 如何对标签中的内容做匹配呢？
s = '<div class="breadcrumb">詹姆斯</div>'  # div是一个块级标签，而里面的是行级标签
# s = '<div class="breadcrumb">詹姆斯</span>'  # div是一个块级标签，而里面的是行级标签  None

# 思考4：如何验证标签格式是否正确呢？
match_obj = re.fullmatch(r'<(.+) class="breadcrumb">(.+)</\1>', s)  # 如何保证前后的名字一样呢？\1表示引用第一组匹配的内容
print(match_obj)  # <re.Match object; span=(0, 33), match='<div class="breadcrumb">詹姆斯</div>'>
print(match_obj.group(2))  # 詹姆斯

print('*' * 50)
# 思考5：
s = '<div class="breadcrumb"><a href="http://www.baidu.com">詹姆斯</a></div>'  # div是一个块级标签，而里面的是行级标签
match_obj = re.fullmatch(r'<(.+) class="breadcrumb"><(.+) href="(.+)">(.+)</\2></\1>', s)
print(match_obj.group(1))
print(match_obj.group(2))
print(match_obj.group(3))
print(match_obj.group(4))
