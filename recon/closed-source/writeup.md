# Writeup for `closed source`

|        author       | category | value |
|---------------------|----------|-------|
| yellowsubmarine1447 |  recon   |  100  |

open-source software is cringe anyway

| cost |                                content                                 |
|------|------------------------------------------------------------------------|
|  10  | First figure out where to SEARCH, then think about what to search for. |

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

We're given the website [http://myreallycoolwebsite.chickenkiller.com/](http://myreallycoolwebsite.chickenkiller.com/). Not much to go off of...

If we try and navigate to a different path in the website, such as [http://myreallycoolwebsite.chickenkiller.com/robots.txt](http://myreallycoolwebsite.chickenkiller.com/robots.txt), we get an error saying the requested file was not found, but more importantly it (implicitly) says the website is hosted with **GitHub Pages**.

This, as well as the challenge title, hints us to try and search GitHub for the source code of this website. You can try guessing what should be searched for, but a good way to motivate this is to read the GitHub Pages documentation, it states:
```
If you are publishing your site from a branch, this will create a commit that adds a CNAME file directly to the root of your source branch.
```

That is, there will be a file called `CNAME` in the source code repository of this website containing `myreallycoolwebsite.chickenkiller.com`! So, we only need to do a code search for this term, find the repository and discover a secret image file containing our flag. 

### Flag(s)

- `BEGINNER{you_c4n_run_BU7_y0u_c4n't_hide_9abe8}`

</details>
