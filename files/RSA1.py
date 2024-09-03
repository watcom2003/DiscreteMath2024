import random
from sympy import mod_inverse, isprime

def generate_prime_candidate(length):
    """Generate an odd integer randomly"""
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    """Generate a prime number of given bit length"""
    p = 4
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p

def generate_keypair(keysize):
    p = generate_prime_number(keysize)
    q = generate_prime_number(keysize)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# ใช้โปรแกรม
keysize = 512  # กำหนดขนาดของกุญแจ
public_key, private_key = generate_keypair(keysize)

print("Public Key:", public_key)
print("Private Key:", private_key)

# ข้อความที่ต้องการเข้ารหัส
message = "Hello RSA!"

# เข้ารหัส
encrypted_msg = encrypt(public_key, message)
print("Encrypted Message:", encrypted_msg)

# ถอดรหัส
decrypted_msg = decrypt(private_key, encrypted_msg)
print("Decrypted Message:", decrypted_msg)
