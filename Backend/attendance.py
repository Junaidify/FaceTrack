import face_recognition as fr
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os

app = FastAPI()


@app.post('/')
async def imageReceived(studentImg: UploadFile = File(...)):
    try:
        contents = await studentImg.read()
        filename = studentImg.filename

        if not contents:
          return JSONResponse(status_code=400, content = {
             "message": "failed to receive image"
        })
          
        unknown_img = fr.load_image_file(contents)
        unknown_img_locations = fr.face_locations(unknown_img)
        unknown_img_encoding = fr.face_encodings(unknown_img, known_face_locations=unknown_img_locations, model='cnn')
        
        if not unknown_img_encoding : 
            return JSONResponse(status_code=400, content = {"message" : "No face detected in uploaded image"})
        
        
        unknown_encoding = unknown_img_encoding[0]
        knownDir = './uploads'
        
        for filename in os.listdir(knownDir) : 
            
          
    except Exception as e : 
        return JSONResponse({
            "Error" : "failed to process image!"
        })
