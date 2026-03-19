"""
1. 创建客户端Socket对象
2. 连接服务器端，指定：服务器端ip和端口号
3. 发送数据
4. 接收数据
5. 关闭Socket对象
"""

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('10.100.39.250', 10086))
data = client_socket.recv(1024)
print(f'接收到的数据：{data.decode("utf-8")}')

client_socket.send('hello1111'.encode('utf-8'))

client_socket.close()
