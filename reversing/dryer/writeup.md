# Writeup for `dryer`

| author |  category | value |
|--------|-----------|-------|
|  poi   | reversing |  100  |

I accidentally put my program in the dryer and now it's all jumbled up. What program was I making a rudimentary copy of?

| cost |                 content                 |
|------|-----------------------------------------|
|  0   | I know I `return 0` at the end of main. |
|  0   | Have a look at trigraphs.               |

## Files

- [src/dryer.c](src/dryer.c): The C code.

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

This challenge involves understanding basic C function layout and simple rotational cyphers. The goal is to decode each line of code to create a functional program that is a pseduo-implementation of a popular program. 

The solution involves using the rot13 cypher on each line of code, but each sequential line is rotated by one more than the last. For instance, we know that the top line should probably be a header file, or line 26 looks like it has been fully rotated back to normal. Work forward or backwards and include empty lines.

```c
#include <stdio.h>

int main() {

    int numbers[10];
    for (int i = 0; i < 10; i++) {
        numbers[i] = i + 1;
    }

    for (int i = 0; i < 10; i++) {
        if (numbers[i] % 3 == 0 && numbers[i] % 5 == 0) {
            numbers[i] = 0;
        } else if (numbers[i] % 3 == 0) {
            numbers[i] = 0;
        } else if (numbers[i] % 5 == 0) {
            numbers[i] = 0;
        }
    }

    for (int i = 0; i < 10; i++) {
        printf("%d ", numbers[i]);
    }

    printf("\n");

    return 0;
}
```
The resulting program is a variant of fizzbuzz which instead of printing fizz or buzz, sets those values to 0 and prints the resulting array.

### Flag(s)

- `BEGINNER{fizzbuzz}`
- `BEGINNER{FIZZBUZZ}`

</details>
