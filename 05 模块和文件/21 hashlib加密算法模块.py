# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
hashlib
    。md5
    。sha1
    。sha256

    正常情况下，以上三种算法，都是加密不可逆

base4 -- 加密可逆
'''
import hashlib


# 需加密内容
s = '微笑天使：何思雨'
# md5原始为空，需要将其进行更新
# 方法一：先创建md5对象（为空类型），再更新md5的值即可
# md5 = hashlib.md5()  # md5 加密 ---一种散列算法 --- 比较老的一种算法，破解比较容易一些
# md5.update(s.encode('utf-8'))  # 需要将要加密的内容编码为utf-8格式

# 方法二：直接一步到位即可
md5 = hashlib.md5(s.encode('utf-8'))
# print(md5.digest())
print(md5.hexdigest())  # 16进制
'''
注册：
    。用户名
    。密码
    ---> 数据库
    admin  123456  --> 不能将密码以明文的方式直接存储，需要对其进行加密，然后再保存至数据库，保证数据的安全性
    
    我们日后用数据库的时候用的就是256的，并且加盐，加一部分动态内容，进一步增加安全性
'''
print('=' * 50)
sha1 = hashlib.sha1(s.encode('utf-8'))
# 思考：是否还需要调用 update ? 不用,因为sha1没有reshape方法，在创建对象的时候直接传入规定格式的字符串即可

print(sha1.hexdigest())

# 注意：现在在数据库存数据的时候，基本都用sha256,甭管多长！
# sha256
sha256 = hashlib.sha256(s.encode('utf-8'))
print(sha256.hexdigest())

# 思考：如何知道使用各种加密算法后，各自的加密结果[转换为16进制]多长呢？
print(len(md5.hexdigest()))  # 32
print(len(sha1.hexdigest()))  # 40
print(len(sha256.hexdigest()))  # 64  sha256本来就是256位[二进制]，因为我们转为16进制，所以是64位


