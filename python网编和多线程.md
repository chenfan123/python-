# 网编和多线程

## 网络编程

### 网络编程三要素

ip 端口号 协议

- ip: 每一台计算机的唯一标识，通过 ip 地址来找到指定的计算机
- 端口: 标识进程的逻辑地址，通过端口来找到指定的进程（0 ～ 65535，0 ～ 1023 已经被系统占用或者作为保留端口)
- 协议: 定义通信规则，符合协议则可以通信，不然无法正常通信。

> ifconfig 命令：可以查看本机的 ip 地址
> ping: 测试网络连通性

#### TCP 协议和 UDP 协议

##### TCP 协议

传输控制协议，是一种面向连接的、可靠的、基于字节流的传输层通信协议，效率相对较低。

###### 三次握手

1. 客户端向服务端发送请求，等待服务端确认
2. 服务端收到请求后知道客户端请求建立连接，回复给客户端以确认连接请求。
3. 客户端收到确认后，再次发送请求确认服务端，服务端收到正确请求后，则建立连接成功。

###### 四次挥手

1. 当主机 A 完成数据传输后，提出停止 TCP 连接的请求
2. 主机 B 收到请求后，对其做出响应，确认这一方向上的 tcp 连接将关闭。
3. 主机 B 提出反向的连接关闭请求
4. 主机 A 收到请求后进行确认，双方向的关闭结束

### socket

是进程之间通信的工具，数据在 socket 之间通过数据包（UDP 协议）或者字节流（TCP 协议）的形式进行传输。

```python
# 倒入socket模块
import socket

# 创建socket对象:socket(AddressFamily,Type)，AF_INET表示使用IPv4地址，SOCK_STREAM表示使用TCP协议
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
socket.bind(('127.0.0.1', 8080))

# 监听连接
socket.listen(5)
```

#### TCP 程序开发流程

1. socket()创建 socket 对象
2. bind(address)方法：绑定地址(host,port)到 socket，在 AF INET 下，以元祖(host,port)的形式传入
3. listen(backlog)方法：最大监听数，指定在拒绝连接之前，操作系统可以挂起的最大连接数，最少为 1，大部分设置为 5 就可以了。最大 128.
4. accept()方法：等待监听连接的客户端,会返回一个元祖，元祖的第一个参数是负责和客户端交互的 socket 信息，第二个参数是地址。
5. send(data)：发送数据，data 为要发送的数据，以 bytes 二进制形式发送。
6. recv(bufsize)：接收数据,数据以 bytes 二进制形式返回，bufsize 指定要接收的最大数据量。
7. close()：关闭连接
   setsockopt(level,optname,value): 可设置端口号复用，让程序退出端口号并立即释放 level 可指定为 SQL_SOCKET,optname 可指定为 SO_REUSEADDR,value 可指定为 True

步骤说明：1. 创建服务端套接字对象 2. 绑定端口号 3. 设置监听 4. 等待接受客户端的连接请求 5. 发送数据 6. 接收数据 7. 关闭套接字

```python
# 创建socket对象:socket(AddressFamily,Type)，AF_INET表示使用IPv4地址，SOCK_STREAM表示使用TCP协议
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

注意事项：

1. TCP 服务端必须绑定端口号
2. accept()前的套接字是被动套接字，只负责接收新的客户端的连接请求，不能收发消息
3. tcp 客户端和服务端连接成功后，tcp 服务器端会产生一个新的套接字，用于首发客户端消息
4. 若关闭 accept()返回的被动连接套接字，则表示和这个客户端已经通信完毕
5. 当客户端的套接字调用 close 后，服务器端的 recv 会解阻塞，返回的数据长度为 0，用于判断客户端是否已经下线。

##### 编解码

`decode('utf-8'\'gbk')\encode('utf-8'\'gbk')`方法：将字符串转换为二进制（encode）或者将二进制转换为字符串（decode）。
