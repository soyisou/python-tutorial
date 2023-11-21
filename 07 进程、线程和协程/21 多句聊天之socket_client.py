# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''
多句聊天 --- 线程实现
'''

'''
客户端端两个线程：
    。send_msg()
    。receive_msg()
'''

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

# 创建客户端socket
client = socket(AF_INET, SOCK_STREAM)

# 连接地址
con_address = ('10.28.81.248', 9001)  # IP地址，端口号设置为9001

# 服务器地址和端口号
client.connect(con_address)

# 发送信息
def send_msg(socket):
    while True:
        msg = input('客户端要发送的消息:\n')
        if len(msg) == 0:
            print()
        socket.send(msg.encode('utf-8'))

# 接收信息
def receive_msg(socket):
    while True:
        msg = socket.recv(512).decode('utf-8')
        if len(msg) == 0:
            break
        print('收到了服务器端的消息:\n', msg)

# 创建线程
t1 = Thread(target=send_msg, args=(client, ))
t2 = Thread(target=receive_msg, args=(client, ))

# 启动线程
t1.start()
t2.start()
