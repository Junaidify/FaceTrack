const mongoose = require("mongoose");

mongoose
  .connect(process.env.MONGODB_URL)
  .then(() => console.log("MongoDB Connected!"))
  .catch((err) => console.log("MongoDB failed to connect!", err));

const student = new mongoose.Schema({
  name: {
    type: String,
    lowercase: true,
    required: true,
  },
  isPresent: {
    type: Boolean,
    required: true,
    default: false,
  },
});

const studentSchema = mongoose.model("Student", student);
module.exports = studentSchema;
