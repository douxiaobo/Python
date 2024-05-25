import socket   #导入stocket模块
s=socket.socket()   #创建socket对象 创建 TCP/IP套接字
host='127.0.0.1'    #获取主机地址
port=8080   #设置端口号
s.connect((host,port))  #主动初始化 TCP 服务器连接
print('Hi, Here is the Client!')
send_data=input("Enter the message to send: ")  #提示用户输入数据
s.send(send_data.encode())  #发送 TCP 数据
recv_data=s.recv(1024).decode() #接收对方发送过为的数据，最大接收1024个字节
print("Received message from server: ",recv_data)
s.close()   #关闭套接字