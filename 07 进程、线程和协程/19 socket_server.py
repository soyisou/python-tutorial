# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
创建 socket服务器
'''
from socket import socket, AF_INET, SOCK_STREAM

# 创建服务器对象
server = socket(AF_INET, SOCK_STREAM)

con_address = ('10.28.81.248', 9001)
# 绑定端口号
server.bind(con_address)  # ''默认为本机IP，端口号9001

# 开启监听状态
server.listen(5)  # 设置backlog参数，表示设置堆积数量

while True:
    socket, addr_info = server.accept()  # 只要没人来的话，就是阻塞的，就干等着，如果有人进来了就不阻塞了···
    # print(socket, addr_info)

    # 接收客户端信息
    data = socket.recv(512).decode('utf-8')  # 返回值为字节
    if data:
        print('{} 发过来的消息是：{}'.format(addr_info[0], data))

    # 关闭socket对象
    socket.close()

    print(addr_info, '离开了！')