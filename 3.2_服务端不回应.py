# 章晓妍
# 开发时间：2022/6/5 21:05
import socket
import time

# SOCK_DGRAM 表示使用UDP协议
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定IP和端口
server.bind(('127.0.0.1', 10006))

while True:

    # 接收信息
    message, address = server.recvfrom(1024)

    # 获取当前时间
    cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"{cur_time}\t{address}\t{message.decode()}")

