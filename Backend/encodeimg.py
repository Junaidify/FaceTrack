import face_recognition as fr 
from fastapi.responses import JSONResponse
from fastapi import FastAPI, UploadFile, File
import os 
import pickle

app = FastAPI('/save-encoding')
async def encodingImagesOfStudents(image_received : UploadFile = File(...)) : 
    try : 
        student_img = image_received.read()

        if not student_img : 
            return JSONResponse(content={"Error" : "Failed to receive image"})
        
        unknown_img = fr.load_image_file(student_img)
        unknown_img_location = fr.face_locations(unknown_img)
        unknown_img_encoding = fr.face_encodings(unknown_img, known_face_locations = unknown_img_location)

        encoding = unknown_img_encoding[0]

        known_dir = './uploads'
        if not os.path.exists(known_dir) : 
            os.mkdir("uploads")

        filename = os.path.splitext(encoding)[0]
        filepath = os.path.join(known_dir, f"{filename}.pkl")

        with open(filepath, 'wb') as f : 
            pickle.dump(encoding, f)

        return JSONResponse(content={"message" : f"file is saved as {filepath}.pkl"}, status_code=200)

    except Exception as e : 
        import traceback 
        traceback.print_exc()
        return JSONResponse(content={"Error" : f"Didn't receive the image, {str(e)} "}, status_code=500)