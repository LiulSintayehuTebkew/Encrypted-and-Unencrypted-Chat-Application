import math
n = 143
e = 7
p = 0
q = 0

for i in range(2,n):
    print('brute force attack...')
    if n%i == 0:
        p = i

q = n // p
print('found p and q')

print('p:',p)
print('q:',q)
d = 0
phi_n = (p-1) * (q-1)


for i in range(phi_n):
    if i*e % phi_n == 1:
        d = i

def decrytion(c):
    p = [chr(pow(i,d,n)) for i in c]
    return ''.join(p)
print(d)

print(decrytion([int(i) for i in '19 121 98 83 98 59 21 98 65 33 34 59 49 98 119 45 39 33 100 62 49 98 45 119 98 16 39 32 59 79 62 98 65 83'.split(' ')]))