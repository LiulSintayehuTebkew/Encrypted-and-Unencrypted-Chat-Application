import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect_ex(('127.0.0.1',5151))

while True:
    mg = input('you : ')
    s.send(mg.encode())
    m = s.recv(1024).decode()
    print(m)
    if mg == 'bye':
        break
s.close()
