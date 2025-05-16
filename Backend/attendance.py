import face_recognition as fr
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
from io import BytesIO

app = FastAPI()

@app.post('/')
async def imageReceived(studentImg: UploadFile = File(...)):
    try:
        student_img = await studentImg.read()

        if not student_img:
            return JSONResponse(status_code=400, content={
                "message": "Failed to receive image"
            })

        # Load and encode unknown image
        unknown_img = fr.load_image_file(BytesIO(student_img))
        unknown_img_locations = fr.face_locations(unknown_img)
        unknown_img_encodings = fr.face_encodings(
            unknown_img, known_face_locations=unknown_img_locations, model='cnn')

        if not unknown_img_encodings:
            return JSONResponse(status_code=400, content={
                "message": "No face detected in uploaded image"
            })

        unknown_encoding = unknown_img_encodings[0]

        # Compare with known images
        knownDir = './uploads'
        for filename in os.listdir(knownDir):
            filepath = os.path.join(knownDir, filename)
            known_img = fr.load_image_file(filepath)
            known_encodings = fr.face_encodings(known_img)

            if not known_encodings:
                continue  # Skip if no face found in known image

            match_result = fr.compare_faces([known_encodings[0]], unknown_encoding)

            if match_result[0]:
                return JSONResponse({
                    "status": "Present",
                    "matched_with": filename
                })

        return JSONResponse({"status": "Absent"})

    except Exception as e:
        return JSONResponse(content={
            "error": f"Image couldn't be processed: {str(e)}"
        }, status_code=500)
