# Writeup for `alternative medicine`

|      author     | category | value |
|-----------------|----------|-------|
| scorpiontornado |   web    |  100  |

Seek a different form of injection.

| cost |                                    content                                    |
|------|-------------------------------------------------------------------------------|
|  10  | Did you know you can perform SQL injection on statements other than `SELECT`? |

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

The provided website allows us to login. The challenge description (and perhaps even the title) hints at some sort of injection vulnerability, perhaps SQL injection. However, the login page doesn't seem to yield any good results. We then turn to the register page, which conveniently has a debug page that allows us see the exact SQL statement executed when registering a new user.

We see that an `INSERT INTO` is used to add a new database entry, inserting `0` into the `admin` field on top of inserting the username and password we provide for login to the `username` and `password` fields (respectively). Our goal is probably, then, create an admin user (i.e. one that has `1` in its `admin` field), and login as them.


### Walkthrough

We can actually turn back to the challenge description and leverage a SQL injection to escape the quotes of, say, the password field, inject into the `admin` field, close the `INSERT INTO` query and comment out the rest of the query appended to it. For example, setting our username to `username` and password to `password", 1);--` will result in a SQL query looking like the following (which we can verify by enabling the debug checkbox field):
```sql
INSERT INTO user (username, password, is_admin) VALUES ("username", "password", 1);--", 0);
```

Thus, an admin user with username `username` and password `password` will be created. Logging in as them gives us our flag.

### Flag(s)

- `BEGINNER{Ins3RT_InT0_tH3_InSER7_1NTo!!}`

</details>
