# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
需求：
    。找一张图片，根据图片链接，将图片下载到本地

<img class="currentImg" id="currentImg" onload="alog &amp;&amp; alog('speed.set', 'c_firstPageComplete', +new Date); alog.fire &amp;&amp; alog.fire('mark');" src="<img class="currentImg" id="currentImg" onload="alog &amp;&amp; alog('speed.set', 'c_firstPageComplete', +new Date); alog.fire &amp;&amp; alog.fire('mark');" src="https://pics6.baidu.com/feed/902397dda144ad34749074b8a4b10af331ad85f8.jpeg?token=ad5461d70c5de4d40843b0bfdb6725b4" width="409" height="362.374" style="top: 121px; left: 0px; width: 488px; height: 432.368px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">" width="409" height="362.374" style="top: 121px; left: 0px; width: 488px; height: 432.368px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">
'''

import re,requests
import os

# 三个图片的地址
list1 = [
'<img class="currentImg" id="currentImg" src="https://pics6.baidu.com/feed/902397dda144ad34749074b8a4b10af331ad85f8.jpeg" width="409" height="362.374" style="top: 121px; left: 0px; width: 488px; height: 432.368px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">" width="409" height="362.374" style="top: 121px; left: 0px; width: 488px; height: 432.368px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">',
'<img class="currentImg" id="currentImg" src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic.soutu123.com%2Felement_origin_min_pic%2F17%2F03%2F05%2Ff4795c1d96ebfdc3b56973d3338f843f.jpg" width="409" height="409.62923076923" style="top: 93px; left: 0px; width: 488px; height: 488.751px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">'
]

for img_tag in list1:
    m_obj = re.match(r'<img class="currentImg" id="currentImg" src="(.+?)"', img_tag)
    if m_obj:
        print(m_obj.group(1))
        url = m_obj.group(1)
        # # requests 是你的浏览器
        # response
        response = requests.get(url)
        # response:  header body
        data = response.content  # 文本用text，二进制文件用 content
        filename = os.path.split(url)[-1]
        print('--->', filename)
        with open('images'+ filename, 'wb') as ws:
            ws.write(data)
        print('{}保存完毕！'.format(filename))