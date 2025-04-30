const router = require("express").Router();
const fs = require("fs");
const path = require("path");
const childProcess = require("child_process");

router.post("/attendance", (req, res) => {
  const { image } = req.body;

  if(!image){
    console.error("Image couldn't receive...");
    return res.status(400).json({error : "Image isn't provided."})
  }

  const base64Data = image.replace(/^data:image\/\w+;base64,/, "");
  const filename = `student_${Date.now()}.png`;

  const uploadDir = path.join(__dirname, 'uploads');

  if(!fs.existsSync(uploadDir)){
    fs.mkdirSync(uploadDir);
  }

  const imagePath = path.join(uploadDir, filename);

  fs.writeFileSync(imagePath, base64Data, 'base64');

  const python = childProcess.spawn("C:/Junaid Khan/Python/FaceTrack/Backend/venv/Scripts/python.exe", [
    "attendance.py",
     imagePath, 
     {cwd: "C:/Junaid Khan/Python/FaceTrack/Backend"}
  ]);

  let result = "";
  python.stdout.on("data", (data) => {
    result += data.toString();
  });

  python.stderr.on("data", (err) => {
    console.error("Python error", err.toString());
  });

  python.on("close", (code) => {
    console.log(`Python code returned ${code}`);
    res.status(200).json({ status: "Completed", result: result.trim() });
  });
});

module.exports = router;
