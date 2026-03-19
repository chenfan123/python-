# 文件上传到服务器端
"""
1. 创建服务器端socket对象
2. 绑定ip和端口号
3. 设置最大监听数
4. 等待客户端申请建立连接
5. 读取客户端上传的文件数据
6. 把读取到的数据写到目的地文件中
7. 释放资源
"""
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('10.100.39.250', 10086))

server_socket.listen(5)

# 等待客户端申请建立连接
accept_socket, client_info = server_socket.accept()

# 读取客户端上传的文件数据
with open('./data/receive.txt', 'wb') as f:

    # # 循环读取数据
    while True:
        # ## 接受客户端上传的数据
        bys = accept_socket.recv(8192)  # 8kb的缓冲区
        # ## 判断是否读取到数据
        if len(bys) == 0:  # 无数据结束即可
            break
        # ## 把读取到的数据写到目的地文件中
        f.write(bys)

# 发送确认消息
accept_socket.send('上传成功'.encode('utf-8'))

# 释放资源
accept_socket.close()
