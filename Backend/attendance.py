import cv2 as cv
import sys
import face_recognition as fr

# Ensure image file is provided
if len(sys.argv) < 2:
    print("Error: No image file provided")
    sys.exit(1)


try:
    known_img = fr.load_image_file('./images/reov.png')
    unknown_img = fr.load_image_file(sys.argv[1])
except FileNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)


try:
    known_encoding = fr.face_encodings(known_img)[0]
    unknown_encoding = fr.face_encodings(unknown_img)[0]
except IndexError:
    print("Error: No face found in one of the images.")
    sys.exit(1)

# Compare faces
results = fr.compare_faces([known_encoding], unknown_encoding)

if results[0]:
    print("Matched")
else:
    print("Unmatched")
