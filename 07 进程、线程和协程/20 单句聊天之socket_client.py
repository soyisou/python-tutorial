# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''

'''
from socket import socket, AF_INET, SOCK_STREAM

# 创建客户端socket
client = socket(AF_INET, SOCK_STREAM)

# 连接地址
con_address = ('10.28.81.248', 9001)  # IP地址，端口号设置为9001

# 服务器地址和端口号
client.connect(con_address)

# 向服务器发送信息
# client.send('可以去吃饭啦！'.encode('utf-8'))  # 字节

while True:
    # 向服务器发送消息
    msg = input('客户端输入：')
    client.send(msg.encode('utf-8'))

    if msg == 'byebye':
        # 关闭客户端
        client.close()
        break

    # 接收服务器消息
    recv_msg = client.recv(512).decode('utf-8')  # recv也是一个阻塞式的方法
    if recv_msg:
        print('服务器会话：{}'.format(recv_msg))

    if recv_msg == 'byebye':
        # 关闭客户端
        client.close()
        break

# 思考：本聊天小程序，只能单句聊天，能不能连续聊天呢？有没有其他方法呢？   有！通过线程实现！