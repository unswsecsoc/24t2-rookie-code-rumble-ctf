	.text
main:	
	li	$v0, 8
	li	$a0, user_input
	li	$a1, 40
	syscall
	li	$t0, 0
	b	d

a:
	li	$t1, 36
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	r

b:
	li	$t1, 48
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	q

c:
	li	$t1, 55
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	o

d:
	li	$t1, 66
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	e

e:
	li	$t1, 69
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	ble	$t0, 3, g
	b	j

f:
	li	$t1, 70
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	k

g:
	li	$t1, 71
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	h

h:
	li	$t1, 73
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	i

i:
	li	$t1, 78
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	ble	$t0, 5, i
	b	e

j:
	li	$t1, 82
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	u

k:
	li	$t1, 95
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	ble	$t0, 15, l
	b	o

l:
	li	$t1, 98
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	t

m:
	li	$t1, 99
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	c

n:
	li	$t1, 101
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	m

o:
	li	$t1, 105
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	ble	$t0, 24, p
	b	q

p:
	li	$t1, 110
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	ble	$t0, 21, a
	b	v

q:
	li	$t1, 111
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	ble	$t0, 23, f
	b	p

r:
	li	$t1, 112
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	ble	$t0, 14, s
	b	n

s:
	li	$t1, 114
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	b

t:
	li	$t1, 121
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	k

u:
	li	$t1, 123
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	r

v:
	li	$t1, 125
	lb	$t2, user_input($t0)
	bne	$t1, $t2, print_incorrect
	addi	$t0, $t0, 1
	b	print_correct

print_correct:
	li	$v0, 4
	li	$a0, correct_flag_text
	b	epilogue
print_incorrect:
	li	$v0, 4
	li	$a0, incorrect_flag_text
epilogue:
	syscall
	li	$v0, 1
	jr 	$ra

	.data
user_input:
	.space 40
prompt:
	.asciiz "Enter the flag:"
correct_flag_text:
	.asciiz "Access granted"
incorrect_flag_text:
	.asciiz "Access denied :("

