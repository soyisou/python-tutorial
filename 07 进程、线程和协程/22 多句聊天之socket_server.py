# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
多句聊天 --- 线程实现
'''
'''
服务器端两个线程：
    。send_msg()
    。receive_msg()
'''
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

# 创建服务器对象
server = socket(AF_INET, SOCK_STREAM)

con_address = ('10.28.81.248', 9001)
# 绑定端口号
server.bind(con_address)  # ''默认为本机IP，端口号9001

# 开启监听状态
server.listen(5)  # 设置backlog参数，表示设置堆积数量

# 发送信息
def send_msg(socket):
    while True:
        msg = input('服务器端要发送的消息: ')
        socket.send(msg.encode('utf-8'))

# 接收信息
def receive_msg(socket):
    while True:
        msg = socket.recv(512).decode('utf-8')
        if len(msg) == 0:
            break
        print('收到了客户端的消息:', msg)

while True:
    socket, addr_info = server.accept()  # 阻塞的

    # 创建线程
    t1 = Thread(target=send_msg, args=(socket, ))
    t2 = Thread(target=receive_msg, args=(socket, ))

    # 启动线程
    t1.start()
    t2.start()

    # t1.join()
    # t2.join()

    # 关闭socket对象
    # socket.close()
    # print(addr_info, '离开了！')