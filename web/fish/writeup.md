# Writeup for `fish`

|  author  | category | value |
|----------|----------|-------|
| Ixbixbam |   web    |  100  |

I really like fish and want `tons` of it, could you give me a save file for [SharkGame](https://dev.shark.tobot.dev/) with at least 42 googol fish in it please?

| cost |                                                                                                                                                                content                                                                                                                                                                |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0   | There are multiple approaches to this challenge: One idea is trying to analyse the save file format and try to manually decode it and re-encode it, potentially using CyberChef. Another is to set a breakpoint midway through the program's execution to modify the save file to change the property that stores the amount of fish. |
|  0   | In some web browsers' developer tools (accessible by right click `Inspect`), you can see what code executes when a button is pressed using the `Event Listeners` menu item in the `Elements` tab.                                                                                                                                     |
|  0   | This project is well documented, so it could helpful to look around some of the files and search for key words in every file until something interesting pops up.                                                                                                                                                                     |

## Solution

<details>
<summary>Click here to reveal the solution!</summary>

### The Big Idea

Reverse engineering a real life application to cheat at a game.

### Walkthrough

There are many equally valid ways to solve this challenge, the following is just one way:

1) Work out that you can export a save through the options menu at the bottom and that it appears to be in an obscure format. 
2) Use the `Inspect` tool to select the _export_ button in the `Elements` tab and open the `Event Listeners` pane to see that `panes.ts:354` is executed when the export button is clicked.
3) Notice that the source map is unavailable, so disable it in settings and repeat step two to visit `panes.js:281`.
4) Search for the `exportData` function which is in `saves.ts` and set a breakpoint to view the contents of `saveData`, so that the amount of fish in it can be modified.
5) Notice that the `saveData` is already encoded, so repeat with the `saveGame` function.
6) Change the `saveData` object to include more fish with the command `saveData.resources.fish.amount += 42e100`.
7) Resume script execution and paste the new save file into the website to verify it.
8) Paste in the website field input for the flag.

### Flag(s)

- `BEGINNER{s0_lon6_&_7hanks_foR_a11_th3_fi5h}`

</details>
