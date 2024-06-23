# Writeup for `salad`

|        author       | category | value |
|---------------------|----------|-------|
| yellowsubmarine1447 |  crypto  |  100  |

This flag is protected with military-grade encryption (historically speaking): DGIKPPGT{ecguct_ucncf_ecguct_ekrjgt}

| cost |                               content                                |
|------|----------------------------------------------------------------------|
|  0   | This is a very rudimentary cipher, named after Roman general Julius! |

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

The hint of this challenge says the cipher used here is named after a Roman general called Julius. Even if you have no idea what any of this means, you can still solve this challenge! A surprisingly useful trick is to just look up key words used as hints or information in a challenge: looking up "Julius cipher" gives results of a cipher called the Caesar cipher!

### Walkthrough

Going to an online Caesar cipher decoder, we find that the key is a single number. Entering our encrypted flag and bruteforcing possible numbers, we find that 2 works as a key and gives our decrypted flag!

### Flag(s)

- `BEGINNER{caesar_salad_caesar_cipher}`

</details>
