# Writeup for `canary in a code mine`

| author | category | value |
|--------|----------|-------|
| rdttl  |  binary  |  100  |

We've gotten in trouble with the higher-ups for being too hackerish. They're using a compiled program with "security features". Find a way to get past this so we can delete the evidence.

| cost |                                   content                                   |
|------|-----------------------------------------------------------------------------|
|  0   | What is the program testing for before `printFile`?                         |
|  0   | The password field is a different length to the username field. Be careful! |

## Files

- [src/chal](src/chal): The program binary.

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

We can find that our "win" function, `printFile`, is protected by a few
checks.

That is, we not only need to set `admin` to `1`, but we also need to preserve the
integrity of the hardcoded canary, and make sure our username or password isn't
just all `A`.

### Walkthrough

1. The canary is simply two bytes: `\0`, and `A`. We can overwrite the
username slot, and then the canary, and then `p64(1)` for the admin variable.
Note that we can't simply use the same payload for the password, as it'll
overwrite the canary.

2. A sample solution is provided.

### Flag(s)

- `BEGINNER{ruFfL3d_s0me_F34th3r5}`

</details>
