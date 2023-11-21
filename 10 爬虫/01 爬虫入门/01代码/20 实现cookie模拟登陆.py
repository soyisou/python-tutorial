# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
python爬虫实现Cookie模拟登陆CSDN
'''
import requests
from lxml import etree
import random
import os

class CsdnSpider:
    def __init__(self):
        self.url = 'https://www.csdn.net/'
        self.headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'cookie': 'uuid_tt_dd=10_37472237500-1635915499729-571653; c_segment=5; dc_sid=d51df8400e730b5b2b69cbd8dab236e6; c_dl_um=-; SESSION=d85b12f1-cc87-42d4-b3e0-1bf5c43a7b28; UserName=qq_44714448; UserInfo=b344a77f2dec417ea92a7f673654279e; UserToken=b344a77f2dec417ea92a7f673654279e; UserNick=water+lover; AU=F51; UN=qq_44714448; BT=1636469821048; p_uid=U010000; ssxmod_itna=GqUxgD0DuDnDcBYDX7G7maG=fQdkKWfGRmQC0DBkW4iNDnD8x7YDvm+OKimDmxEvqePboWxIQeRmRDqPLbUCip3Ei7aboDHxY=DUEAvmxbDeW=D5xGoDPxDeDADYoXDAqiOD7qDdUEwNNBDi3Db2=Df4DmDGYyiqDgDYQDGMPUD7QDIu6=i06PgS2MUjtPFm3yD0UQxBd57cuokZaeSkrTE3IzYDDH/hy3iDxz5YwEYQPnDB=pxBjlUuNXUmyB/TN4ZhhWShxoBE5RC7PrKAEPSG4f4ToKeFM3YDAzS2GoUG5lxD3qeTj3eD; ssxmod_itna2=GqUxgD0DuDnDcBYDX7G7maG=fQdkKWfGRmQCD8q6+0xGX3DOexFE+r2UcPAP584DunL4=e9KB3K6pQYDuYiPUQiwHcOU77wguwkuQmy9sjSpdwUzEXEIHpC23dFI=9NsvLUK+kkkIvOjE3DL7DkF+Xy/oA4dbNlfBYZAMAe2LQyYWTUWj=Yo36dMwKV+ldMtwoy3fchtfaXB3QAGZoZWTWcmjnWqRWHbL2vtmH/QmoGPQKpcw0h+ErGs7aqv8eLYl9pzuap9Rv1L+5iwOERzRCkIqIRD6++8CYFj2F7t+6hezH8Uq3VNHf34SWbXQwpbcrYBrKId0H4Mv8iAO3+ZGP=W0WU7KobWtYHBBkSnLSmjKceooAUB5TeokabFo1SmqiGqZACSApKi=N+Ypr5ZE7RhN2Ti4WfzT8t3GGGa3Fr53lifmSES3m4/27CitC0D933D072DxqGxyuK3Ajn0xQwomcjbPth76RhKoDDLxD2iGDD=; c_first_ref=www.baidu.com; csrfToken=k2y7MJzv9_DLQI0EeYvXJFEa; c_utm_source=app; c_pref=https%3A//www.baidu.com/link; c_dl_prid=1637571610271_324014; c_dl_rid=1637759718039_613103; c_dl_fref=https://www.baidu.com/link; c_dl_fpage=/tagalbum/1367916; c_first_page=https%3A//blog.csdn.net/qq_35028612/article/details/72810884; c_ref=https%3A//blog.csdn.net/qq_35028612/article/details/72810884; log_Id_click=56; firstDie=1; dc_session_id=10_1637924064228.209558; c_page_id=default; dc_tos=r36f8w; log_Id_pv=104; log_Id_view=817'
        }

    def get_html(self, url):
        html = requests.get(url=self.url, headers=self.headers).text
        self.parse_html(html)

    def parse_html(self, html):
        # 创建解析对象
        ps_html = etree.HTML(html)
        xpath_bds = ''



