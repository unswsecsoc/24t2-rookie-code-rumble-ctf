def main():
	hex_string = input("Enter hexadecimal: ")

	# Split the hex string into a list of equivalent integers
	bytes_list = hex_string.split()
	byte_values = [int(byte, 16) for byte in bytes_list]

	# Xor the bytes to extract the flag
	byte_values = xorCycle(byte_values)
	byte_values = xorCycle(byte_values)

	# Write the xor'd input to a file
	with open("solved.txt", "wb") as f:
		f.write(bytes(byte_values))
      
    
def xorCycle(byte_values):
	back = len(byte_values) - 1
	for front in range(0, len(byte_values)):
		byte_values[front] ^= byte_values[back]
		back -= 1
	return byte_values

main()




'''
xorCycle:
We can make this easy to follow along by using two pointers into an array, a
"front", and "back" pointer.

  Front																	  Back
|------------------------------------------------------------------------------|
|	2 	|	4	|	2	|	1	|	10	|	5	|	5	|	2	|	2	|	1  |
|------------------------------------------------------------------------------|
Front = Front XOR Back
Front = 2 XOR 1
	  = 3


   ---->  Front													  Back  <----
|------------------------------------------------------------------------------|
|	3 	|	4	|	2	|	1	|	10	|	5	|	5	|	2	|	2	|	1  |
|------------------------------------------------------------------------------|
Front = Front XOR Back
Front = 4 XOR 2
	  = 6

...
We continue this process beyond the midpoint of the list, until we reach the end

  		  						  Back	  Front
|------------------------------------------------------------------------------|
|	3 	|	6	|	0	|	4	|	15	|	5	|	5	|	2	|	2	|	1  |
|------------------------------------------------------------------------------|

...
End. Note how the latter half is simply a reflection of the original first half.

  Back																	  Front
|------------------------------------------------------------------------------|
|	3 	|	6	|	0	|	4	|	15	|	10	|	1	|	2	|	4	|	2  |
|------------------------------------------------------------------------------|
'''
