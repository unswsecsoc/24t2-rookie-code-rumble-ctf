# Writeup for `blaise`

|        author       | category | value |
|---------------------|----------|-------|
| yellowsubmarine1447 |  crypto  |  100  |

Help Blaise decrypt the flag `QKKHCTIQ{l0c_cnJ_IvzrQ3h_ln_i0h3_j3nri5r}`.

You want the key? Don't have it!


| cost |                                       content                                       |
|------|-------------------------------------------------------------------------------------|
|  0   | What does "Blaise" have to do with cryptography??                                   |
| Is there a part of the flag you DEFINITELY know? Can this help you recover the key? |                                          10                                         |

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### Walkthrough

Looking up "Blaise" and "cipher" together returns results for a vigenere cipher; this is probably what we have to use!

There's many ways to explain how a vigenere cipher works. The way I'll explain it as follows. 

You have a message you want to encrypt (say `MESSAGE`) and a key you use to encrypt with (say `KEY`). Then, each letter will be converted into a number via `A1Z26` (so "A" becomes 1, "B" becomes 2... and so on), so our example has `KEY` become the numbers "11", "5" and "25", because that's their positions in the alphabet. Then, you shift the first letter of the message with the first number from the key via a normal Caesar shift (wrapping around from "Z" to "A") *but shift back by one afterwards*, then the second letter with second number and so on until we reach the end of our key or message - in our example, "M" gets shifted by 11-1 to "W", "E" gets shifted by 5-1 to "I", "S" gets shifted by 25-1 to "Q". If we reach the end of our key before reaching the end of our message, we go back to the start of our key and repeat the process, looping back through the key as many times as needed until we reach the end of the key. So continuing our example, "S" gets shifted by 11-1, "A" gets shifted by 5-1, and so on.

We know the flag starts with `BEGINNER`. A key property of the Vigenere cipher described before is if we align the encrypted cipher with a known part of the text and use the shifting process described before to decode it, we'll actually end up with that part of our key from the rotation (try and figure out why this is the case). So, trying to decrypt our flag with the key `BEGINNER` to test this out gives us the following "decoded" text:
```
PGEZPGEZ...
```

Note that the letters `PGEZ` repeat cyclically in the "decoded" text, which is a key characteristic of a vigenere cipher's key when encrypting and decrypting! This indicates a high likelihood that `PGEZ` is the key used to encrypt the flag via the Vigenere cipher, and sure enough, trying to decode the encrypted text with it gives us our flag!

### Flag(s)

- `BEGINNER{w0w_yoU_CracK3d_my_c0d3_k3yle5s}`

</details>
