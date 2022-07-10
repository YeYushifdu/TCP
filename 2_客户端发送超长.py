# 章晓妍
# 开发时间：2022/6/3 20:21
import socket

with open("test2.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件

# 创建套接字对象，AF_INET基于TCP/UDP通信，SOCK_STREAM以数据流的形式传输数据，这里就可以确定是TCP了
client = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# 连接服务端
client.connect(('127.0.0.1',8081))

while True:
    inp = input('>>>：').strip()
    # 向服务端发送数据，需要转换成Bytes类型发送
    client.send(data.encode('utf-8'))
    print(data.encode('utf-8'))

    # 接收服务端回应给客户端的数据，不能超过1024字节
    res = client.recv(1024)


    print(res.decode('utf-8'))

# 套接字关闭
client.close()
