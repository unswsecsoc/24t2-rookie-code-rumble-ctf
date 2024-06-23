# Writeup for `creep stand`

|        author       | category | value |
|---------------------|----------|-------|
| yellowsubmarine1447 |  binary  |  100  |

bro help my autotests are failing

| cost |                                                              content                                                              |
|------|-----------------------------------------------------------------------------------------------------------------------------------|
|  0   | Try compiling the C code in GCC :P                                                                                                |
|  0   | Stack addresses are just numbers!                                                                                                 |
|  10  | ASLR will make the addresses of variables change, but the address difference between variables is fixed (and are multiples of 4)! |                                                                 10                                                                |

## Files

- [src/challenge.c](src/challenge.c): Source code of `challenge` executable
- [src/challenge](src/challenge): Executable hosted on `connection_info` host and port for this challenge

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

One of the hints of this challenge was to try and compile the C source code with GCC. Trying to do this will give us some warnings:
```
bin_chall.c: In function ‘main’:
bin_chall.c:15:28: warning: format ‘%ld’ expects argument of type ‘long int’, but argument 3 has type ‘int *’ [-Wformat=]
   15 |         printf("crep %d: %ld\n", i, stock+i); // pointer arithmetic ;)
      |                          ~~^        ~~~~~~~
      |                            |             |
      |                            long int      int *
      |                          %ls
bin_chall.c:19:22: warning: format ‘%ld’ expects argument of type ‘long int *’, but argument 3 has type ‘int **’ [-Wformat=]
   19 |     fscanf(stdin, "%ld", &age);
      |                    ~~^   ~~~~
      |                      |   |
      |                      |   int **
      |                      long int *
```

If it's not immediately obvious what the issue is, we're incorrectly using pointers, referencing and dereferencing (or lack there of for the latter). The first warning is a bit silly (and doesn't seem immediately obvious what it can be used for at first): it's printing the `stock` array itself plus some number.

If you haven't seen this before, this is called pointer arithmetic: you perform arithmetic (adding/subtracting *integers*) to pointers or arrays, essentially offsetting them to a different position. This works because variables that are pointers/arrays actually contain an address to some other memory location they're referencing (with that data type before the asterisk/square brackets), and addresses are actually just numbers!

Furthermore, array values are stored contiguously, so `stock+i` contains an address to `stock[i]`! (note that doing `+i` will actually add `4*i` to the numerical representation). The issue, however, is that we're printing the address directly, not dereferencing it (the program wants to print the value of `stock+i`, so it should've derefenced, but it left it as is, causing a mismatch where an integer was expected but a pointer was passed. C will implicitly typecast this and print the address as a number).

The second error is more interesting and subtle, because the pattern `scanf(stdin, "%d", &variable)` is very common in C programming: essentially, this line will read in an integer and store it in a variable, but you want to pass the address of the variable so you know *where* to store the read-in value. However, `age` is already a pointer (`int *`), so passing `&age` into the argument of `fscanf` will cause it to be interpreted as an `int**` data type - a pointer to a pointer!

More importantly, this draws us to the issue that the `fscanf` will write to the *address stored in `age`*., NOT to the place where it points. So, we can actually pass in whatever address we want into `age`, and now whatever `age` now points to will be set by the random number generated on line `22`. So, let's just set the `admin` variable and get our flag!

...except there's an issue. Executables in most opearting systems have this protection called "ASLR", which stands for Address Space Layout Randomisation. This causes addresses to be randomly shifted by different offsets. You can actually see this from the leaked `stock` addresses you get every time you run the challenge binary: the numbers change drastically every time! In a 64-bit machine, there's far too many possibitilies for what the base address could be; brute-forcing (at least in this CTF) is a no-go. Luckily, differences betweeen the addresses of variables will always be the same every time we run our program. For example, the address of `admin` and address of the `stock` array are always 28 bytes apart! This means the very first address printed in the beginning of our program can actually be used to figure out the address of admin: we just have to subtract `32` from it! (not `28`, since the first address printed is `4` after the `stock` array's address).

By the way, the offset of `32` can be figured out by simply bruteforcing multiple-of-4 differences and trying to subtract them from the initial array address (or writing your own script to do this), OR using GDB to print the variables' addresses dynamically OR statically disassmble the assembly code and figure out the difference between the two variables.

### Walkthrough

Feel free to also have a look at [src/solution.py](src/solution.py) to see a pwntools automating the below idea.
1. Connect to `pwn.ctf.secso.cc` on port `5001`
2. Copy the first number appearing on your screen
3. Subtract 32 from it
4. Input the new number
5. Get the flag

### Flag(s)

- `BEGINNER{i_s41d_h3lp_mE_n0T_H4ck_Me}`

</details>
