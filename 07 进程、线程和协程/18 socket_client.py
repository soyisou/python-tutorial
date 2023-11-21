# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
网络编程

网络各层

端口号：
    。每一个应用都会有自己的端口号，用来标记每个应用，范围 0~65535
    。http 80
    。ftp 21

    思考：如何查看应用的端口号呢？ netstat-an

IP地址：
    。电脑在互联网上的标识

socket(简称：套接字):
    。是进程间通信的一种方式，它与其他进程间通信的一个主要不同是：它能实现不同电脑间的进程通信，我们网络上各种各样的
     服务大多都是基于 Socket 来完成通信的。假如我们每天浏览网页、QQ聊天、收发 email等

TCP：
    。SOCK_STREAM  -- TCP
    。SOCK_DGRAM   -- UDP

__slots__：
    。作用一： 限制外界动态创建属性
    。作用二：节约内存空间
'''

from socket import socket, AF_INET, SOCK_STREAM

# 表示创建了一个客户端的socket
client = socket(AF_INET, SOCK_STREAM)

# 连接地址
con_address = ('10.28.81.248', 9001)  # IP地址，端口号设置为9001

# 服务器地址和端口号
client.connect(con_address)

# 思考1：如何进行读或者写操作呢？

# 向服务器发送信息
client.send('可以去吃饭啦！'.encode('utf-8'))  # 字节

# 关闭客户端
client.close()

# 思考2：是否需要绑定地址呢？

# 思考3：是否可以直接在浏览器往咱的服务器发送呢？ 可以！  在搜索框中输入：10.28.81.248:9001