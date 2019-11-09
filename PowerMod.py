from functools import partial
from random import randint

def EEA(a, b):
    if b == 0:
        return a, 1, 0
    q = a // b
    d1, x1, y1 = EEA(b, a % b)
    d, x, y = d1, y1, (x1 - q * y1)
    return d, x, y

def power_mod(b, e, m):
    return (b ** e) % m


p_prime_number = 47
q_prime_number = 71
n_number = p_prime_number * q_prime_number
phi_number = (p_prime_number - 1) * (q_prime_number - 1)
e_number = 79  # between 1-phi and GCD(e_number,phi) = 1. Public key (e_number,n_number)
d_number = EEA(phi_number, e_number)[2]  # Private key = (d_number,n_number)
crypt = partial(power_mod, e=e_number, m=n_number)
decrypt = partial(power_mod, e=d_number, m=n_number)

print("public key (e,n): ", (e_number, n_number))
print("private key (d,n)", (d_number, n_number))

mess = int(input("give me a integer number to encrypt: "))
c = crypt(mess)
print("Encrypt: ", mess, c)
print("Decrypt: ", c, decrypt(c))
