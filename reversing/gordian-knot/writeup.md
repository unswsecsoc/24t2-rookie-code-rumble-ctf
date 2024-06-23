# Writeup for `gordian knot`

|  author  |  category | value |
|----------|-----------|-------|
| Ixbixbam | reversing |  100  |

I saw my friend creating a file in COMP1521 that acts as a password manager, and he says that its super secure because no one can read his obfuscated assembly anyway.

You can run the code [here](https://cgi.cse.unsw.edu.au/~cs1521/mipsy/) and open the documentation [here](https://cgi.cse.unsw.edu.au/~cs1521/24T2/resources/mips-guide.html).


| cost |                                                                                                                  content                                                                                                                  |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0   | One approach could be to incrementally add comments and rename the code as you understand it more and recognise patterns within it. Afterwards, you could insert extra assembly which prints interesting information as the program runs. |
|  0   | The program exits early if the flag is incorrect at any point, but there a way to change the script to disable this unfavourable feature, allowing you to determine the entire flag at once.                                              |

## Files

- [src/code.s](src/code.s): A MIPS program that checks if a password is valid.

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

Reverse engineering MIPS to find input data that takes a particular path through the program. 

### Walkthrough

1) Add comments to understand the gist of the program. For example the program starts with the C 

	```
        char[40] user_input;
        fgets(user_input, 40, stdin);
        int i = 0;
	        
        value_a = 36;
        value_b = user_input[i];
        if (value_a != value_b) goto print_incorrect;
        i++;
        go to next one```

2) From the comments, it is clear that the values in `value_a` are the decimal representing each ascii character of the flag. This can be confirmed by double checking that the first few characters are the start of the flag prefix since the program initially branches to `d`, representing the character `B` and subsequently branches to `e`, representing `E`. 
3) Instead of exiting if the character is incorrect, we want to know what the correct character is as this is what the flag needs to be at that point. Since the program exits early using the `BNE` instruction, we can `find and replace` it with code that prints the character in `$t2`. 
   Specifically, `        bne     $t1, $t2, print_incorrect` is replaced with ```
        li  $v0, 11
        move $a0, $t1
        syscall```

This prints the flag to the screen when the script is executed.

### Flag(s)

- `BEGINNER{pr0oF_by_in$pec7ion}`

</details>
