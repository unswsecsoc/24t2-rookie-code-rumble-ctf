from Crypto.Util.number import getPrime
from secrets import FLAG

# Start with random primes
p = getPrime(1024)
q = getPrime(1024)

# Encryption constants
n = p * q
e = 0x10001

# Turn flag into an integer and encrypt
m = int.from_bytes(FLAG, "big")
c = pow(m, e, n)

# Reveal necessary parts of RSA
print("This is c:", c)
print("This is e:", e)
print("This is n:", n)

# Reveal some things we're not supposed to :P
# I feel like I've seen this somewhere before in maths...
print("First leak:", p*p - q*q)
print("Second leak:", p - q)

# Usually, solving RSA CTF challenges involves finding p and q
# You can't do this with just c, e and n, maybe there's something else...
# Once you figure out p and q, here's some code to get back FLAG:
"""
t = (p - 1) * (q - 1)
d = pow(0x10001, -1, t)
m = pow(c, d, n)

print(m.to_bytes(100, "big").replace(b"\x00", b"").decode("latin-1"))
"""
