import socket   #导入socket库
host='127.0.0.1'    #主机名IP
port=8080       #端口号
web=socket.socket() #创建stocket对象
web.bind((host,port))    #绑定IP和端口
web.listen(5)   #设置最大连接数
print("Hi, Here is the server")
print("Server is listening on port",port)
# 开启死循环
while True:
    conn,addr=web.accept()  #建立客户端连接
    print("Connection from",addr)
    data=conn.recv(1024)    #获取客户端发送的数据
    print("Received data:",data.decode())
    print(data) #打印接收到的数据
    conn.send(b"\nHello, client!\n")
    conn.send(b'HTTP/1.1 200 OK\r\n\r\nHello, World!')  #向客户端发送数据
    conn.close()    # 关闭连接