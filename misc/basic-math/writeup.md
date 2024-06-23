# Writeup for `basic math`

| author | category | value |
|--------|----------|-------|
|  poi   |   misc   |  100  |

Is your basic math mathing?

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

Python Integer Caching. Python caches small integers between -5 and 256. Each time you refer to one of these numbers, it's actually an object that already exists.
Also the "is" and "is not" comparison is checking if it's the same object.

### Walkthrough

So we need a number X such that x+1 is the same object as 1+x. That is to say, x+1 is within the bounds [-5, 256] 
Similarly, we need to make sure that x+2 is a different object as 2+x. That is to say, x+2 is outside the bounds [-5. 256]
So logically the only number that satisfies this is 255.

### Flag(s)

- `BEGINNER{ca$h_or_cach3}`

</details>
