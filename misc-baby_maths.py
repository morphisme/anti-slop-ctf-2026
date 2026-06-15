# nc 178.105.199.41 22222
import pwn # pip install pwntools

def lrecv():
    r = bytes.decode(r0.recvline())[:-1]
    print(r)
    return r

def lsend(rep):
    print(rep)
    r0.sendline(str.encode(rep))

signes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=', '(', ')']
r0 = pwn.remote('178.105.199.41', 22222)  #, level = 'debug')
for k in range(4):
    lrecv()
for k in range(100):
    lrecv()
    a = ''
    while a == '' or 'Question' in a:
        a = lrecv()
    if 'divided by' in a:
        a = a.replace('divided by', '/')
    if 'I am a human' in a:
        lsend('I am a human')
        lrecv()
        continue
    x1 = 0
    while 1:
        if a[x1] in signes:
            break
        x1 += 1
    x2 = len(a) - 1
    while 1:
        if a[x2] in signes:
            break
        x2 -= 1
    b = eval(a[x1:1+x2])
    if 'floor' in a:
        b = int(b)
    lsend(str(b))
    lrecv()
for k in range(4):
    lrecv()
r0.close()
# flag: slopped{...}
