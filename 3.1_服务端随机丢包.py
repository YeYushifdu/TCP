# 章晓妍
# 开发时间：2022/6/5 20:10
import socket
import random
import time

# SOCK_DGRAM 表示使用UDP协议
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定IP和端口
server.bind(('127.0.0.1', 10001))

while True:
    # 生成一个随机数，用于模拟丢包的情况
    rand = random.randint(0, 10)

    # 接收信息
    message, address = server.recvfrom(1024)

    # 获取当前时间
    cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"{cur_time}\t{address}\t{message.decode()}")

    # 如果随机数小于2，就不响应本次数据，模拟丢包
    if rand < 2:
        continue
    # 收到报文就回复
    if message != 0:
        server.sendto(b"get message!", address)
