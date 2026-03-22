import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',5050))
s.send(('Shift is 3').encode())
agree = s.recv(1024).decode()
print(agree)
s.send('%'.encode())

while True:
    m = s.recv(1024).decode()
    decryted = ''
    for i in m:
        if i.isspace():
            decryted += ' '
        else:
            decryted += chr((ord(i) - 97 -3)%26+97)
    print(decryted)
    mg = input('You: ').lower()
    encrypted = ''
    for i in mg:
        if str(i).isspace():
            encrypted += ' '
        else:
            encrypted += chr(((ord(i) - 97 + 3) % 26) + 97)
    s.send(encrypted.encode())
    
    if mg == 'bye':
        break

s.close()