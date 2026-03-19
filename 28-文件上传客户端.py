"""
客户端
1. 创建客户端Socket对象
2. 连接服务器端的ip端口号
3. 关联数据源文件，读取内容，写给服务器
4. 
"""

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('10.100.39.250', 10086))

# 关联数据源文件
with open('./data/send.txt', 'rb') as f:
    # 循环读取内容
    while True:
        # 读取操作
        bys = f.read(8192)
        # 发送给服务器
        client_socket.send(bys)
        # 判断是否读取到数据
        if len(bys) == 0:
            break

# 等待服务器确认消息
data = client_socket.recv(1024)
print(f'接收到的数据：{data.decode("utf-8")}')

# 释放资源
client_socket.close()
