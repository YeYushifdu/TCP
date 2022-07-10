# 章晓妍
# 开发时间：2022/6/6 12:43
import socket
import time

# SOCK_DGRAM 表示使用UDP协议
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定IP和端口
server.bind(('127.0.0.1', 10008))
while True:
    i=0
    while i<3 :
        message, address = server.recvfrom(1024)
        # 获取当前时间
        cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(f"{cur_time}\t{address}\t{message.decode()}")
        i+=1
        continue

    server.sendto(b"get message!", address)
