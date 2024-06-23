# Writeup for `doggi`

| author |  category | value |
|--------|-----------|-------|
| rdttl  | forensics |  100  |

This lil' guy melted my heart. So much that I needed to go to the doctor. But I forgot when my heart melted... can you help?

**Note**: Your flag should look like `BEGINNER{YYYY:MM:DD_HH:MM:SS}`.


| cost |                          content                           |
|------|------------------------------------------------------------|
|  0   | How can we find the date and time embedded inside a photo? |

## Files

- [doggi.jpg](doggi.jpg): The image file.

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

We need to look for the file metadata, which among other fields, offers an insight into when the photo was taken.

### Walkthrough

1. We are looking for the file metadata. This can be discovered through a tool such as `exiftool`, or through online file metadata checkers.

2. In particular, we're looking for a field such as "Date/Time Original", the time the image was created, not the creation time of the file you downloaded.

### Flag(s)

- `BEGINNER{2024:06:15_17:55:50}`

</details>
