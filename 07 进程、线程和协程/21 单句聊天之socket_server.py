# author : LJM - Jeson
# Email  : 878665865@qq.com
# coding : utf - 8
'''

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

    while True:
        # 接收客户端信息
        data = socket.recv(512).decode('utf-8')  # 返回值为字节，recv也是一个阻塞式的方法
        if data:
            print('客户端说：{}'.format(data))
            if data == 'byebye':
                break
        send_msg = input('服务器输入：')
        socket.send(send_msg.encode('utf-8'))
        if data == 'byebye':
            break

    # 关闭socket对象
    socket.close()
    print(addr_info, '离开了！')