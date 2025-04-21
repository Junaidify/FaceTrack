import cv2 as cv
import sys
import face_recognition as fr 

knownImg = fr.face_encodings(fr.load_image_file('./images/reov.png'))[0]
unknownImg = fr.face_encodings(fr.load_image_file(sys.argv[1]))[0]


results = fr.compare_faces([knownImg], unknownImg)

if results[0] : 
    print("Matched")
else : 
    print("Unmatched")



