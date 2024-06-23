# Writeup for `grandmaster`

|  author  |  category | value |
|----------|-----------|-------|
| Ixbixbam | forensics |  100  |

I heard the US censored correspondence chess games during under rumours spies were hiding information within them, which gave me an idea. Here's my working out to hide the word `jazz`. Can you figure out the message this attached game is hiding?

*Update*: It turns out that I forgot to delete one of the encoding script's debugging files from the recycle bin. If the police found the working out paper in a raid, they'd also find the hard drive and find the file through forensic analysis, so it's only fair if I give it to you too.

*Note*: Your answer should be the text that was hidden, you do not need to wrap your answer with `BEGINNER{}`. For example, if you think the answer is `jazz`, then supply `jazz` as the flag.


| cost |                                                                              content                                                                              |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0   | Can you work out what game is being played using the metadata of the game file or the grid in the image?                                                          |
|  0   | There's a similar algorithm for chess games lurking on the internet, which could help you understand the encoding process.                                        |
|  10  | The algorithm is quite similar to converting bases of numbers, try to research how to convert decimal to hexadecimal for example.                                 |
|  10  | How many legal moves are there at the start of the `jazz` game, and after the first move? Also, what would be an intuitive way for a computer to sort the set of possible moves? |

## Files

- [src/ciphertext.txt](src/ciphertext.txt): A PDN file that stores the moves of a checkers game that has the text encoded.
- [src/image.jpg](src/image.jpg): Working out to encode the text `jazz` in a checkers game.
- [src/miami.debug.txt](src/miami.debug.txt): An exported file showing another example of `miami` being encoded in a checkers game.

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

Reverse engineering vague steps to encode data in a draughts game to decode secret data.

### Walkthrough

The method employed is similar to the one described by [James Stanley](https://incoherency.co.uk/blog/stories/chess-steg.html), and involves first converting text to a number, (456309 in the case of the example game) and encoding it in the index of the move chosen. There are 9 legal moves at the beginning of the game, which are placed in an array sorted in alphabetical order of their algebraic notation (eg "31-26"). The index of the move to be chosen is the number we are decoding remainder 9, and we divide the number by 9 to encode the rest of the data. This is how little-endian base conversions work, the only complication is that the base of the number dynamically changes based on the rules of checkers. 

The way to decode the game is similar to how convert a base back to decimal from the left without knowing how long it is. For example, the `0xAB12` can be found by starting with 10 then multiplying by 16 and adding the value of each digit - `(((10 \* 16 + 11) \* 16 + 1) \* 16 + 2)`. 

1) Searching Google for `[GameType "20,W,10,10,N2,0"]` returns results about checkers and the PDN format of specifying games, which confirms the hand-drawn checkers board. 
2) Import the game into `lidraughts`. 
3) Determine how many legal moves there are and the index of the chosen move in the array of sorted moves. Multiply the previous number (starting with 0) by the total number of legal moves and add the current move index. 
4) Repeat step 3 until all moves have been decoded. 
5) Convert the decimal number to base 26 with the symbols 'a' to 'z' to obtain the flag. 

Post-CTF edit: I apologise for the unituitive choice of sorting the moves in lexical order as ASCII strings, I didn't realise how weird it is to sort that way when decoding the game by hand. I'll learn from this _blunder_ of mine and be more careful when I create challenges in the future.

### Flag(s)

- `blunder`

</details>
