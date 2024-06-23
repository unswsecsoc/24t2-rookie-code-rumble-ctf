# Writeup for `number checker`

| author | category | value |
|--------|----------|-------|
| rdttl  |  binary  |  100  |

The checker of numbers is willing to trade for something they haven't seen yet...

| cost |                                                       content                                                       |
|------|---------------------------------------------------------------------------------------------------------------------|
|  0   | The checker of numbers doesn't like people all that much. How can we give them an offer without them asking for it? |
|  0   | Actual numbers seem to be out of the question. What is something that we can insert instead??                       |
|  0   | This binary is IEEE754 compliant.                                                                                   |

## Files

- [src/chal](src/chal): The program binary.

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

Through inspection of the decompiled code, a solution doesn't stand out
immediately.

This is because the flag lies beyond the two paths that check for what's *meant*
to cover for all cases (`num <= 0.0` and `0.0 < num`).

```
  if (num <= 0.0) {
    if (0.0 < num) {
      puts("wait no");
      printFile();
      uVar1 = 0;
    }
    else {
      puts("Hmmmm! No thanks!");
      uVar1 = 1;
    }
  }
```

However, we can identify that it's a `double`. Float comparisons with `NaN` breaks
the intention of this check, and permits the program to bypass it and continue
execution.

### Walkthrough

1. We need to overflow the buffer, and then write the double NaN into num to
bypass the checks.

2. A sample solution is provided with more detail.

### Flag(s)

- `BEGINNER{th4ts_4_c00L_"numb3r"_d4wg!}`

</details>
