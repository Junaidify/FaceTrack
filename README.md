# FaceTrack
Let your face mark your place.

# FaceTrack 🎓📸

**FaceTrack** is a smart, AI-powered attendance system that uses facial recognition to mark students as present — no manual roll calls, no cards, no touch.

With just a webcam snap, FaceTrack verifies the student’s identity and logs their attendance directly into an Excel sheet. Designed for simplicity, security, and speed — it’s your modern classroom assistant.

---

## 🔍 Features

- 🧠 Face Recognition using OpenCV + face_recognition
- 📸 Capture via React and Webcam
- 📊 Attendance stored in Excel (easy to share)
- 🧪 Works offline or in secure classrooms
- 🔧 Node.js + Python hybrid backend

---

## 🚀 Tech Stack

- **Frontend:** React, react-webcam
- **Backend:** Node.js (Express)
- **Image Processing:** Python, OpenCV, face_recognition
- **Storage:** Excel via Pandas and OpenPyXL

---

## 🌱 How to Use

1. Capture image from React webcam
2. Image sent to Node.js backend
3. Backend saves image & calls Python script
4. Python script checks face & updates attendance
5. Response sent back to frontend

---

## 📦 Future Enhancements

- Google Sheets integration
- Face training panel for admins
- JWT-based user auth (Teacher / Student)
- QR fallback or RFID support

---

> Built with ❤️ by Junaid Khan
