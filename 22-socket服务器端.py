'''
演示socket:服务器端
'''
import socket
# 创建socket对象:socket(AddressFamily,Type)，AF_INET表示使用IPv4地址，SOCK_STREAM表示使用TCP协议
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket_obj)

# 绑定地址和端口
socket_obj.bind(('10.100.39.250', 10086))

# 设置监听
socket_obj.listen(5)

# 等待接受客户端的连接请求
accept_socket, client_info = socket_obj.accept()
print(f'客户端{client_info}连接成功')

# 发送数据
accept_socket.send('hello'.encode('utf-8'))

# 接收数据
data = accept_socket.recv(1024)
print(f'接收到的数据：{data.decode("utf-8")}')

# 关闭连接
accept_socket.close()
# 关闭服务端套接字 一般不关闭
# socket_obj.close()
