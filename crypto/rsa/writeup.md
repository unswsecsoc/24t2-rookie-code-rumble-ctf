# Writeup for `RSA`

|        author       | category | value |
|---------------------|----------|-------|
| yellowsubmarine1447 |  crypto  |  100  |

Can't believe they invented RSA.

You'll find comments in the source code provided explaining how RSA encryption works and how we can break, feel free to do your own research though!

## Files

- [src/rsa.py](src/rsa.py): The Python program which encrypts our flag with RSA, leaking some devious information...
- [src/output.txt](src/output.txt): The output of the Python program, containing some devious details...

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

We're leaked $p^2 - q^2$ and $p - q$. A super useful identity in maths is that $p^2 - q^2 = (p-q)(p+q)$, and since we have two parts of this equation, we can figure out the third!

### Walkthrough

Have a look at [src/solution.py](solution.py) which showcases the below steps.
1. Rearranging, we can figure out $p + q = \frac{p^2 - q^2}{p-q}$, so first we calculate this.
2. Add/subtract $p + q$ with $p - q$ to get the primes! (note adding/subtracting will give us twice each prime)
3. Now use the script described in the source code to decrypt the flag!

### Flag(s)

- `BEGINNER{is_rsa_5igma_0r_Is_it_skib1Di}`

</details>
