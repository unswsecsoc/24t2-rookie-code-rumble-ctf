# Writeup for `runic riddles`

| author | category | value |
|--------|----------|-------|
|  poi   |  crypto  |  100  |

Larethor stands before you, connect to hear what he has to say.

| cost |                      content                       |
|------|----------------------------------------------------|
|  0   | Each fragment has 3 steps.                         |
|  0   | The first stage is always base64.                  |
|  10  | Output results to a file and use the file command. |

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

Each fragment goes through 3 transformations. The first a mutator, then a compression algorithm then base64 encoding.
The first step is to decode from base64. Base64 often ends with == for padding purposes but there are also more identifying features.
You can use the command line `echo <base64 string> | base64 --decode` to decode it.
I recommend sending the decoded output to a file which will be useful for the next step. `echo <base64 string> | base64 --decode > output`
The next step is to reverse the compression. The generator picks one of a set of compression algorithms so it will vary each execution.
Use the `file` command on your output to check what kind of compression is being used. At this point you might find it helpful to append the relevant file type to your output file. Eg. if the compression is XZ, rename your file output.xz otherwise xz might not recognise it.
The list of compression algorithms are

    - gzip
    - zlib
    - bz2
    - lzma
    - lz4

Each of these should have a simple commandline tool to decompress the file.

Once this is done, the final step is to reverse the mutator. There is no set method, so I'll just tell you the things it could be.

    - ROT47
    - Caesar Cypher shift +1
    - Caesar Cypher shift -1
    - Bitwise XOR with 0xFF
    - Base32 encoding
    - URL encoding

Some of these might be more obvious than others. I'd recommend using Cyberchef to help test these options out.

Once you have done this for all fragments, you should be able to combine them to make the flag.

### Flag(s)

- `BEGINNER{p0w3r_0f_fr13nd5h1p}`

</details>
