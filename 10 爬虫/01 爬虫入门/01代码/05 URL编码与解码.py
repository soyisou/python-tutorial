'''
URL 之所以需要编码，是因为 URL 中的某些字符会引起歧义，比如 URL 查询参数中包含了”&”或者”%”就会造成服务器解析错误；
再比如，URL 的编码格式采用的是 ASCII 码而非 Unicode 格式，这表明 URL 中不允许包含任何非 ASCII 字符（比如中文），
否则就会造成 URL 解析错误。URL 编码协议规定（RFC3986 协议）：URL 中只允许使用 ASCII 字符集可以显示的字符，比如
英文字母、数字、和- _ . ~ ! *这 6 个特殊字符。当在 URL 中使用不属于 ASCII 字符集的字符时，就要使用特殊的符号对
该字符进行编码，比如空格需要用%20来表示。

URL编码：
    。urlencode(dict|tuple)
    。quote(str)

URL解码：
    。unquote(str)

'''
# 导入parse模块
from urllib import parse

# 构建查询字符串字典
query_string = {
    'wd': '爬虫'
}

# 调用parse模块中的urlencode()进行编码
result = parse.urlencode(query_string)

# url
url = 'http://www.baidu.com/s?{}'.format(result)
print(url)  # http://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB

# 解码
url_decode = parse.unquote(url)
print(url_decode)  # http://www.baidu.com/s?wd=爬虫

# 调用parse模块中的quote()进行编码
str = '爬虫'
str_encode = parse.quote(str)
url = 'http://www.baidu.com/s?kw={}'.format(str_encode)
print(url)  # http://www.baidu.com/s?kw=%E7%88%AC%E8%99%AB

# 解码
url_decode = parse.unquote(url)
print(url_decode)  # http://www.baidu.com/s?wd=爬虫

'''
URL地址拼接方式
'''

# 1. 字符串相加
baseurl = 'http://www.baidu.com/s?'
params = 'wd=%E7%88%AC%E8%99%AB'
url1 = baseurl + params
print(url1)

# 2. 字符串格式化（占位符）
params = 'wd=%E7%88%AC%E8%99%AB'
url2 = 'http://www.baidu.com/s?%s' % params
print(url2)

# 3. format()方法
url3 = 'http://www.baidu.com/s?{}'
params = 'wd=%E7%88%AC%E8%99%AB'
url3 = url3.format(params)
print(url3)



