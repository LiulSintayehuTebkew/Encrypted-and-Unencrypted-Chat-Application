import socket
import random
import math

def get_prime():
    n = random.randint(100,200)
    for i in range(2,n):
        if n%i == 0:
            return get_prime()
    return n
def generate_key():

    p = get_prime()
    q = get_prime()

    n = p * q

    phi_n = (p-1) * (q-1)

    e = 0
    for i in range(7,phi_n):
        if math.gcd(i,phi_n) == 1:
            e = i

    d = 0
    for i in range(phi_n):
        if i*e % phi_n == 1:
            d = i
            
    return [(n,e),(n,d)]

def encrypt_message(message,pub_key):
    return pow(message,pub_key[1],pub_key[0])

def decrypt_message(cipher,pr_key):
    return pow(cipher,pr_key[1],pr_key[0])

def start_chat():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',5151))
    s.listen(1)
    print('listening on port ')
    c,addr = s.accept()
    key = generate_key()
    c.send(f'{key[0]}'.encode())
    apuk = c.recv(1024).decode()[1:-1].split(',')
    apuk = [int(i) for i in apuk]
    print(apuk)
    while True:
        m = c.recv(1024).decode()
        print(m)
        plain = [decrypt_message(int(i),key[1]) for i in m[1:-1].split(',')]
        plain = "".join([chr(i) for i in plain])
        print(plain)
        mg = input('You: ')
        cipher = [encrypt_message(ord(i),apuk) for i in mg]
        c.send(str(cipher).encode())
        if mg == 'bye':
            break

    s.close()
    c.close()

key = generate_key()
m = 2
 
c = encrypt_message(m,key[0])
dec = decrypt_message(c,key[1])

print('message:',m)
print('cipher:',c)
print('message:',dec)
print('B-Pu',key[0])
print('B-Pr',key[1])

start_chat()

