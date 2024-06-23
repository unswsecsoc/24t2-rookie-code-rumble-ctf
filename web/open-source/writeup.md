# Writeup for `open source`

|        author       | category | value |
|---------------------|----------|-------|
| yellowsubmarine1447 |   web    |  100  |

Apparently you can "open" the "source" of a website! On a separate note, did you know websites can stop search engines from indexing certain pages?!

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

"Opening" the "source" of a website refers to viewing the source code of a webpage, for example by opening devtools (via a right-click) or opening them with some keyboard shortcut (for Chromium, this is `Ctrl+U`)

Furthermore, one way websites can stop search engines can stop certain pages from being indexed is to create a `robots.txt` file that's visible on the `/robots.txt` endpoint of the website, containing a list of said webpages.

### Walkthrough

1. Open the page source and find the first part of the flag `BEGINNER{th1s_is_Th3_first_part_` in a HTML comment
2. Open `robots.txt` and discover the `/super_secret_admin_page_haha` endpoint (contained in its contents)
3. Visit the `/super_secret_admin_page_haha` endpoint and obtain the second part of the flag `7hi5_1S_th3_seconD_P4rt}`

### Flag(s)

- `BEGINNER{th1s_is_Th3_first_part_7hi5_1S_th3_seconD_P4rt}`

</details>
