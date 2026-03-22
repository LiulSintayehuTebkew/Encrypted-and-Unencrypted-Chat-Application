import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',5050))
s.listen(1)

print('listening on port 5050')

c,addr = s.accept()
print('connected to',str(addr))

key = c.recv(1024).decode()
c.send('Agreed on key'.encode())

while True:
    m = c.recv(1024).decode()
    decrypted = ''
    for i in m:
        if i.isspace()or i =='%':
            decrypted += ' '
        else:
            decrypted += chr(((ord(i) - 97 - 3) % 26)  + 97) 
    print(decrypted)
    mg = input("you: ").lower()
    encrypted = ''
    for i in mg:
        if i.isspace():
            encrypted += ' '
        else:
            encrypted += chr(((ord(i) - 97 + 3) % 26) + 97)
    c.send(encrypted.encode())
    if mg == 'bye':
        break
c.close()
s.close()