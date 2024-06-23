# Writeup for `artifacts`

|  author  |  category | value |
|----------|-----------|-------|
| Ixbixbam | forensics |  100  |

The AFP seized a black hat hacker's hard drive and found some interesting files...

| cost |                                                     content                                                      |
|------|------------------------------------------------------------------------------------------------------------------|
|  0   | Can you figure out what this folder represents, and make educated guesses what information would be interesting? |
|  0   | Try to research where interesting data is stored and what software can read the files.                           |

## Files

- [src/g5z58rzw.CTF.zip](src/g5z58rzw.CTF.zip): A zipped Chrome user directory.

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

Analysing a Chrome user data directory to find a URL to protected data and its password.

### Walkthrough

1) Upon unzipping the provided file, you will see a variety of files and subdirectories. Notice some start with the word "browser" and others refer to "cookies", which indicates that this is web browser data. 
2) There are several options here, such as performing dynamic analysis by loading the profile into a Firefox account, researching the structure of the data (eg [hacktricks](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/specific-software-file-type-tricks/browser-artifacts)), and exploring the data yourself. The natural first instinct is to view the person's search history either by importing the profile or by viewing the `places.sqlite`, which can be done using [this SQLite Viewer](https://inloop.github.io/sqlite-viewer/).
3) Try to load the pastebin URL (https://pastebin.com/sbA55NgE) and notice how it requires a password.
4) Search all the files for the literal text "password" using the linux command `grep -r "password" .` and notice that the `Binary file ./formhistory.sqlite matches`, which sounds promising because the user would have to type their password into a form. 
5) View the file and see the password `Fifth-Gradually-Across-Taste6-Bridge` which follows the format that the passphrase generator also in the search history (https://www.keepersecurity.com/features/passphrase-generator/) uses.
6) Enter the password into the pastebin webpage and view the flag.

### Flag(s)

- `BEGINNER{arch4e0logY_for_7he_modern_ag3}`

</details>
