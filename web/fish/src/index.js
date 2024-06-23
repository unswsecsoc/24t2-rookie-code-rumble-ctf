const express = require("express");
const app = express();
const port = 9999;

const Ascii85 = require("./ascii85.js");
const ascii85 = new Ascii85();

const pako = require("./pako.js");

app.use(express.json());

app.post("/", async (req, res) => {
    let saveDataString = req.body.saveDataString;

    if (!ascii85.isSave(req.body.saveDataString)) {
        return res.status(400).json({ error: "This doesn't look like a valid save file - all the ones I've seen start with <~ and end with ~>." });
    }

    saveDataString = ascii85.decode(req.body.saveDataString);

    let saveData;
    try {
        saveDataString = pako.inflate(saveDataString, { to: "string" });
        saveData = JSON.parse(saveDataString);

        if (saveData.resources.fish.amount >= 42 * 1e100) {
            return res.json({ success: "BEGINNER{s0_lon6_&_7hanks_foR_a11_th3_fi5h}" });
        }
    } catch (err) {
        return res.status(400).json({ error: "This save file appears corrupted." })
    }

    return res.json({ error: "This isn't enough fish!" });
});

app.use(express.static("static"));

app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});
