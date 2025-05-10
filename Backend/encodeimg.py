import face_recognition as fr 
from fastapi.responses import JSONResponse
from fastapi import FastAPI, UploadFile, File
import os 
import pickle
import uuid
from io import BytesIO

app = FastAPI()

@app.post('/save-encoding')
async def encodingImagesOfStudents(image_received : UploadFile = File(...)) : 
    try : 
        student_img = await image_received.read()

        if not student_img : 
            return JSONResponse(content={"Error" : "Failed to receive image"})
        
        unknown_img = fr.load_image_file(BytesIO(student_img))
        unknown_img_location = fr.face_locations(unknown_img)
        unknown_img_encoding = fr.face_encodings(unknown_img, known_face_locations = unknown_img_location)

        if not unknown_img_encoding : 
            return JSONResponse(content={"message" : "No face is detected"}, status_code=400)

        new_encoding = unknown_img_encoding[0]

        known_dir = './uploads'
        if not os.path.exists(known_dir) : 
            os.mkdir("uploads")


        for filename in os.listdir(known_dir) : 
            if filename.endswith('.pkl'): 
                filepath = os.path.join(known_dir, filename)
                
                with open(filepath, 'rb') as f : 
                    loading_encoding = pickle.load(f)
                    result = fr.compare_faces([loading_encoding], new_encoding, tolerance=0.6)

                    if result and result[0] : 
                        return JSONResponse(content={"message": "Image already exist"}, status_code=200)

        filename = str(uuid.uuid4())
        filepath = os.path.join(known_dir, f"{filename}.pkl")

        with open(filepath, 'wb') as f : 
            pickle.dump(new_encoding, f)

        return JSONResponse(content={"message" : f"file is saved as {filepath}.pkl"}, status_code=409)

    except Exception as e : 
        import traceback 
        traceback.print_exc()
        return JSONResponse(content={"Error" : f"Didn't receive the image, {str(e)} "}, status_code=500)