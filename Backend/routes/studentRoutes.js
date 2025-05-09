const router = require("express").Router();
const FormData = require("form-data");
const axios = require("axios");

router.post("/attendance", async (req, res) => {
  try {
    const {image} = req.body;

    if (!image) {
      console.error("Image couldn't receive...");
      return res.status(400).json({ error: "Image isn't provided." });
    }

    const base64Data = image.replace(/^data:image\/\w+;base64,/, "");
    const binaryImg = Buffer.from(base64Data, "base64");

    const form = new FormData();
    form.append("studentImg", binaryImg, {
      filename : 'studnet.png', 
      contentType : 'image/png'
    });

    const response = await axios.post("http://localhost:5000", form, {
      headers: form.getHeaders(),
    });

    res.status(200).json(response.data);
  } catch (err) {
    console.error("Error during attendance", err);
    res.status(500).json({ Error: "Internal server error!" });
  }
});

module.exports = router;
