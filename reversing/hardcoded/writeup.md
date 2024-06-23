# Writeup for `hardcoded`

| author |  category | value |
|--------|-----------|-------|
| rdttl  | reversing |  100  |

We've managed to intercept the output of some "encryption" function. Is it possible to reverse this?

| cost |                                                       content                                                        |
|------|----------------------------------------------------------------------------------------------------------------------|
|  0   | The output appears to have reflected the first half of its output; we can still piece together *exactly* half of it. |
|  0   | This program XORs every single byte of the file with something else in the file. What is passed into `xorFunction`?  |
|  0   | What would happen if we were to repeat the same process again?                                                       |

## Files

- [src/chal](src/chal): The program binary.

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

This program simply XORs the i-th byte in the file with the (n-i-1)th byte. This
repeats until the end of the array has been reached.

This is evident by decompiling and stepping the given binary. An int here is 4
bytes in length, hence the jumping around.

```
  for (i = 0; i < fileLen; i = i + 1) {
    targetByte = (undefined4 *)((long)i * 4 + (long)filePtr);
    xorResult = xorFunction(*(undefined4 *)((long)filePtr + (long)i * 4),
                            *(undefined4 *)((long)filePtr + 
                            (long)(fileLen - i) * 4 + -4));
    *targetByte = xorResult;
  }
```

The effect of this is that the latter half of the array has a XOR with itself
and the opposite byte at the front. This yields the opposite byte's original
value, effectively flipping the former to the latter half, but obsfucating the
front.


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

### Walkthrough

1. This means that we can perform these XOR operations again twice, and it will
revert back to normal.

2. Pipe into grep to find the flag.

3. A sample solution is provided with more detail.

### Flag(s)

- `BEGINNER{Im_5ur3_u_d0nt_w4nt_x0r}`

</details>
