const router = require("express").Router();
const fs = require("fs");
const path = require("path");
const childProcess = require("child_process");
const studentSchema = require("../models/studentschema");

router.post("/attendance", (req, res) => {
  const { image } = req.body;

  const base64Data = image.replace(/^data:image\/\w+;base64,/, "");
  const filename = `student_${Date.now()}.png`;
  const imagePath = path.join(__dirname, base64Data, filename)

  const python = childProcess.spawn("C:/Junaid Khan/Python/FaceTrack/backend/venv/Scripts/python.exe", [
    "face_recognition.py",
     imagePath,
  ]);
git 
  let result = "";
  python.stdout.on("data", (data) => {
    result += data.toString();
  });

  python.stderr.on("data", (err) => {
    console.error("Python error", err);
  });

  python.on("close", (code) => {
    console.log(`Python code returned ${code}`);
    res.status(200).json({ status: "Completed", result: result.trim() });
  });
});

module.exports = router;
