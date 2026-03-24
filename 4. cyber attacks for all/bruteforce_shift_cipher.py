common_pattern = ['in','the','to','this','that','hello','bye']

key = 0
cipher = 'khoor zruog'

for i in range(26):
    dec = ''
    print('working on key:',i)
    for k in cipher:
        if k == ' ':
            dec += ' '
        else:
            print('\tworking on char:',k)
            dec += chr(((ord(k)-97-i)%26)+97)
    if dec.split(' ')[0] in common_pattern:
        key = i
        break
    print(dec)
plain = [chr(((ord(i)-97-key)%26)+97) for i in cipher]
print(plain)
print(key)