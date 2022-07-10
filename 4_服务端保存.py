# 章晓妍
# 开发时间：2022/6/6 22:07
import socket

# 创建套接字对象，AF_INET基于TCP/UDP通信，SOCK_STREAM以数据流的形式传输数据，这里就可以确定是TCP了
server = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# 绑定ip地址和端口，127.0.0.1代表回环地址，只能当前计算机访问
server.bind(('127.0.0.1',8082))

# 建立半链接池，允许存放5个请求
server.listen(5)

# 等待建立连接请求，会返回两个值，一个是连接会话，一个是连接的客户端IP与端口
conn,ip_addr = server.accept()

while True:
    # 接收客户端传递的数据，不能超过1024字节
    res = conn.recv(1024)
    print(res.decode('utf-8'))
    with open("save.txt", 'a')as fp:
        fp.write(str(res.decode('utf-8')))
        fp.close()
    # 将客户端的数据接收到以后，转换成大写再编码后发送给客户端
    ans='get message '
    conn.send(ans.encode('utf-8'))

    # 注意：close不能放在这里面，因为在这里面的话，只能一次后就关闭了

# 关闭与客户端的连接
conn.close()

# 关闭套接字
server.close()