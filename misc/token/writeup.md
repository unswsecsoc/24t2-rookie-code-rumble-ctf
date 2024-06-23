# Writeup for `token`

|   author  | category | value |
|-----------|----------|-------|
| larrabyte |   misc   |  100  |

I found this lying on the ground, what could it be?

`MTI1MzEzMDYxMzU0ODkxMjcyNA.G2Yex7.1ATGq5sMb7q1pS6hIpngC4PYc7j6Go_gpgJfnM`


| cost |                                 content                                  |
|------|--------------------------------------------------------------------------|
|  0   | Could you use this to login somewhere?                                   |
|  0   | If you've logged in, look for something that can't be deleted or edited. |

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

Most websites that have a form of authentication use a token to prevent users from having to repeatedly login with their username and password. In almost all cases, these tokens are stored in the browser's local storage and would allow attackers to gain unauthorised access to a site without ever knowing any credentials if they were to be leaked.

A Discord token was given for this challenge - inserting this token into local storage and then refreshing logs you into an account with only one server. Since multiple people may have gotten access at this point, any modifiable text will have potentially been overwritten and is thus not worth inspecting. However, Discord stores an audit log of changes that are made which is uneditable. Inspecting the audit log for changes thus reveals the flag.

### Flag(s)

- `BEGINNER{br04dc457_70_7he_w0rld_w1de_w3b}`

</details>
