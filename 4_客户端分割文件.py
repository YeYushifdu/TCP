# 章晓妍
# 开发时间：2022/6/5 12:39

import socket

f=open("test3.txt", "r")   # 打开文件
data = f.readlines()  # 分行读取
line_list=[]
for line in data:
    line_list.append(line)

count = len(line_list) # 文件行数
print('源文件数据行数：',count)
# 创建套接字对象，AF_INET基于TCP/UDP通信，SOCK_STREAM以数据流的形式传输数据，这里就可以确定是TCP了
client = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# 连接服务端
client.connect(('127.0.0.1',8082))

while True:
    for line in data:
        inp = input('>>>:').strip()
        print(line.encode('utf-8'))
        client.send(line.encode('utf-8'))

    # 接收服务端回应给客户端的数据，不能超过1024字节
    res = client.recv(1024)
    print(res.decode('utf-8'))

# 套接字关闭
client.close()





