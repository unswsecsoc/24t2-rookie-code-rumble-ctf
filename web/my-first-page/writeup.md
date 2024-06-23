# Writeup for `my first page`

| author | category | value |
|--------|----------|-------|
|  poi   |   web    |  100  |

This is my first website! It is under construction.

| cost |                                 content                                 |
|------|-------------------------------------------------------------------------|
|  0   | I'm beginning to think this field can do more than just HTML and CSS... |

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

We have a simple website with an input field which claims it can render some basic html and css. Let's have a poke around to see what we can do.

This challenge has an input field that allows for directory traversal, but does not allow you to read files through the initial page.
Since `.` will show us the current directory, we can navigate the local system through appending to the url. For instance, if I wanted to visit `bootstrap.css` I would append `/static/css/boootstrap.css` to the url. As these are not blocked we can read the file. You might have seen `suspicious.png` while looking in the file system. If you try to navigate to it, you will get a 451, which is very suspicious. In `bootstrap.css` we can see that the default img element will try to fetch this image. There is no img element in the html so even if we could load the new css, nothing would happen. Luckily, the whole point of this site is to look at html elements, meaning we can insert our own `<img>` tag. Once this is done, we can simply inspect element the Link tag in the header and change the `href` attribute to `"../static/css/bootstrap.css"`. This should then display the image with the flag.

### Flag(s)

- `BEGINNER{h1_im_j3ss3}`

</details>
