# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
client端: 浏览器客户端
server端: 自制服务器    --- 通过协程来做的哦 ~  [淘宝等底层也都是这样的！]

浏览器发出请求
server端相应 ---> 送到浏览器

request 请求
    。请求行  请求方法(get)   http/1.1
    。请求头： key:value 形式
    。请求体: POST(get的请求体一般都为空！)

response 相应
    。响应行   http/1.1   200 ok
    。响应头： key:value 形式
    。响应体
'''
# from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from gevent import monkey, socket
import gevent

'''
注意：
    。当我们用协程的时候，我们就不能用socket里面的socket啦，而应该用gevent里面的socket
    。这是因为 monkey里面的socket不能替换socket里面的socket！
    
    思考：这两个socket有什么不同呢？
    。monket中的socket在socket中的socket的基础上，进行了一些封装。
'''

# 使用猴子补丁
monkey.patch_all()  # 先打补丁，否则就不会认为咱们当前的socket是一个耗时操作，也就不会进行切换啦！

# 创建服务器对象
server = socket.socket()  # socket函数仍然是socket库的那个socket，只不过对monket中的socket进行了一些封装

con_address = ('10.28.81.248', 9001)
# 绑定端口号
server.bind(con_address)  # ''默认为本机IP，端口号9001

# 开启监听状态
server.listen(5)  # 设置backlog参数，表示设置堆积数量

def handle_client(socket):
    print('-------')
    # 接收数据
    recv_data = socket.recv(1024).decode('utf-8')
    print(recv_data)

    # 浏览器会接收么？不会！浏览器还有个重要参数--状态码！有请求头和请求体才是有效的！因此我们需要构建响应信息。

    # 为了保证符合网页中的格式，因此我们也需要加上\r\n, 而且最后三者还需要拼接好!

    response_line = 'HTTP/1.1 200 OK\r\n'  # 响应行： 协议-状态码-描述
    response_header = 'Content-Type: text/html;charset=utf-8\r\nServer: BWS/1.1\r\n'  # 值如果还有就加分号分割即可
    response_body = '\r\n<div>哈哈，你来啦！</div> <div style="color:red">欢迎</div>'  # 响应体，即msg

    # 拼接后的结果
    response = response_line + response_header + response_body
    socket.send(response.encode('utf-8'))
    # 关闭socket
    socket.close()

while True:
    socket, addr_info = server.accept()
    print(addr_info, '来啦！')
    # 创建，并启动 greenlet对象[协程]
    gevent.spawn(handle_client, socket)

