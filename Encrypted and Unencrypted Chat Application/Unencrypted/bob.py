import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',5151))
s.listen(2)
print('server is listening on port 5151')

c,addr = s.accept()
print('connected to '+str(addr))

while True:
    m = c.recv(1024).decode()
    print(m)
    mg = input('you : ')
    c.send(mg.encode())
    if mg == 'bye':
        break
c.close()
s.close()
