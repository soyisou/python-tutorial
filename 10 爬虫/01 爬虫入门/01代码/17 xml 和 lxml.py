# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
XML和 lxml
    。lxml 是 Python的第三方解析库，完全使用 Python语言编写，它对 Xpath表达式提供了良好的支持，因此能够高效地解析
     HTML/XML文档。lxml 库提供了一个 etree模块，该模块专门用来解析 HTML/XML文档。
    。调用 etree模块的 HTML()方法来创建 HTML解析对象。
    。HTML()方法能够将 HTML标签字符串解析为 HTML文件，该方法可以自动修正 HTML文本
    。tostring() -- Serialize an element to an encoded string representation of its XMLtree.
                    即，将元素序列化为其 XML的编码字符串表示形式
    。

树
'''
# 1. 导入模块
from lxml import etree

html_str = '''
<div>
    <ul>
         <li class="item1"><a href="link1.html">Python</a></li>
         <li class="item2"><a href="link2.html">Java</a></li>
         <li class="site1"><a href="c.biancheng.net">C语言中文网</a>  # 缺少一个</li>标签
         <li class="site2"><a href="www.baidu.com">百度</a></li>
         <li class="site3"><a href="www.jd.com">京东</a></li>
     </ul>
</div>
'''

# 2. 创建解析对象
parse_html = etree.HTML(html_str)  # HTML()方法能够将 HTML标签字符串解析为 HTML文件，该方法可以自动修正 HTML文本

# 编码为XML字符串格式和解码为utf-8形式
# result = etree.tostring(parse_html)  # 编码为XML字符串形式
# print(result.decode('utf-8'))  # 解码为utf-8形式

# 3. 调用xpath表达式
html = '''
<div class="wrapper">
    <a href="www.biancheng.net/product/" id="site">website product</a>
    <ul id="sitename">
    <li><a href="http://www.biancheng.net/" title="编程帮">编程</a></li>
    <li><a href="http://world.sina.com/" title="新浪娱乐">微博</a></li>
    <li><a href="http://www.baidu.com" title="百度">百度贴吧</a></li>
    <li><a href="http://www.taobao.com" title="淘宝">天猫淘宝</a></li>
    <li><a href="http://www.jd.com/" title="京东">京东购物</a></li>
    <li><a href="http://c.bianchneg.net/" title="C语言中文网">编程</a></li>
    <li><a href="http://www.360.com" title="360科技">安全卫士</a></li>
    <li><a href="http://www.bytesjump.com/" title=字节">视频娱乐</a></li>
    <li><a href="http://bzhan.com/" title="b站">年轻娱乐</a></li>
    <li><a href="http://hao123.com/" title="浏览器">搜索引擎</a></li>
    </ul>
</div>
'''
# 1. 创建解析对象
parse_html = etree.HTML(html)

# 任务1：提取所有a标签内的文本信息

# 2. 创建xpath表达式
xpath_bds = '//a/text()'

# 3. 提取目标信息
r_list = parse_html.xpath(xpath_bds)
# 打印数据列表
print(r_list)

# 任务2：获取所有的href属性值
xpath_bds = '//a/@href'
r_list = parse_html.xpath(xpath_bds)
print(r_list)

# 任务3：获取所有title属性值
xpath_bds = '//a/@title'
r_list = parse_html.xpath(xpath_bds)
print(r_list)

# 任务4：不匹配href="www.biancheng.net/priduct"
xpath_bds = '//ul[@id="sitename"]/li/a/@href'
r_list = parse_html.xpath(xpath_bds)
print(r_list)

# xpath_bds = '//li/text()'
# r_list = parse_html.xpath(xpath_bds)
# print(r_list)


