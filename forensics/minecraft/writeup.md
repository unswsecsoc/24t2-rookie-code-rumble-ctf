# Writeup for `so we back in the mine`

| author | category | value |
|--------|----------|-------|
|  poi   |   misc   |  100  |

I've lost the coordinates for my base. They should be in the format `{XXX_YY_ZZZ}`. Round final numbers upwards.

| cost |                  content                   |
|------|--------------------------------------------|
|  0   | Don't ask why I have those items.          |
|  10  | Perhaps there is a picture in the picture? |

## Files

- [src/minecraft.png](src/minecraft.png): An inconspicuous screenshot.

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

The first step is to convert the numbers of the items in the player's hotbar into ascii characters. This comes out to DEADBEEF.
We can then unzip the image using this password to recieve the second image. This image shows the players current coordinates of `682.5, 67, 301.5`. 
We can also see they are facing West or the negative X direction. Hence 50.5 blocks away will be `682.5-50.5, 67, 301.5` which calculates to `632, 67, 301.5`.
Then due to the rounding mentioned in the description, the final coordinates are `632, 67, 302` in the form `{632_67_302}`.

### Flag(s)

- `BEGINNER{632_67_302}`

</details>
