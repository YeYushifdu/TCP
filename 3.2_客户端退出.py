# 章晓妍
# 开发时间：2022/6/5 21:05
import socket
import time
with open("test1.txt","r") as f:
    data=f.read()


# SOCK_DGRAM 表示使用UDP协议
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 设置超时时间为2秒
client.settimeout(2)

# 服务端的ip和端口
server_addr = ('127.0.0.1', 10006)

for i in range(1):
    # 发送报文
    client.sendto(data.encode('utf-8'), server_addr)
    send_time = time.time()

    try:
        message, _ = client.recvfrom(1024)

        recv_time = time.time()

        print(f"{i}\t{message.decode()}\tSpend: {(recv_time - send_time) * 1000:.2f}ms")
    except socket.timeout as e:  # 超时就打印丢包
        # 再次发送报文
        client.sendto(data.encode('utf-8'), server_addr)
        send_time=time.time()
        try:
            message, _ = client.recvfrom(1024)

            recv_time = time.time()

            print(f"{i}\t{message.decode()}\tSpend: {(recv_time - send_time) * 1000:.2f}ms")
        except socket.timeout as e:  # 超时就打印丢包
            client.sendto(data.encode('utf-8'), server_addr)
            send_time = time.time()
            try:
                message, _ = client.recvfrom(1024)

                recv_time = time.time()

                print(f"{i}\t{message.decode()}\tSpend: {(recv_time - send_time) * 1000:.2f}ms")
            except socket.timeout as e:  # 超时就退出
                print('丢包！')
                client.close()

