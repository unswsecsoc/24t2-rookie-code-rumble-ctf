### Counter Writeup

| author | category | value |
|--------|----------|-------|
|  poi   |   misc   |  100  |

## Challenge Description:
A simple counter where you can increment and decrement a number!

## Files
- [src/server.py](src/server.py): Server code

## Challenge Solution:
<details>
<summary>Click here to reveal the solution</summary>

This challenge involves exploiting a race condition created through the common access of the counting variable across multiple threads/users.
The little delay between sending a command and recieving the value is supposed to be indicative of some background/serverside checks. All we have to do is spawn 2 threads (make 2 connections from different terminals) and get the counter to 9. After that, send `plus` in both terminals within quick succession. In the both threads, the server will think the counter is 9 and execute both `plus` commands before the comparison to 10. As such we jump straight to 11 which is how we get the flag.

## Flag
`BEGINNER{t00_qu1ck_5l0w_d0wn}`

</details>