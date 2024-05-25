import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8888))
print('绑定 UDP 到 8888 端口')
data,addr=s.recvfrom(1024)
data=float(data)*1.8+32
send_data='转换后的温度（单位：华氏温度）：'+str(data)
print('Received from %s:%s.' % addr)
s.sendto(send_data.encode(),addr)
s.close()