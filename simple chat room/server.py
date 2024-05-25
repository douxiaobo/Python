import socket
host=socket.gethostname()
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,addr=s.accept()
print("Connection from: ",addr)