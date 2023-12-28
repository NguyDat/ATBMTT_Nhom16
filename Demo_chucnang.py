import random
import math
#kiem tra co phai la so nguyen to hay k
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#tinh UCLN 
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
#Tinh phan tu nghich dao
def mod_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi
#Tao khoa
def generateKeys():
    p=4
    q=4
    while isprime(p)==False:
        p=random.randint(1000000000000,9000000000000)
    while isprime(q)==False:
        q=random.randint(1000000000000,9000000000000) 
    if p==q:
        p=random.randint(1000000000000,9000000000000)  
        q=random.randint(1000000000000,9000000000000) 
    n=p*q
    phi_n=(p-1)*(q-1)
    e=random.randrange(1,phi_n)
    while gcd(e,phi_n)!=1:
        e=random.randrange(1,phi_n)
    d=mod_inverse(e,phi_n)
    global pubKey
    pubKey=(e,n)
    global priKey
    priKey=(d,n)
#Ma hoa
def encrypt(msg,pubKey):
    e,n=pubKey
    banMa=""
    for i in msg:
        temp=ord(i)
        banMa +=str(pow(temp,e,n))+" "
    return banMa
#Giai ma        
def decrypt(cipher,priKey):
    d,n=priKey
    msg = ""
    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, n))
    return msg
generateKeys()





