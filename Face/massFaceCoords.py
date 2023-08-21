import os
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

loc = [0, 0, 0, 0]

images = []
for filename in os.listdir('./Face/Temp/'):
    img = cv2.imread(os.path.join('./Face/Temp/', filename))
    if img is not None:
        images.append(img)

for image in images:
    faces = face_cascade.detectMultiScale(image, 1.1, 4)

    if len(faces) != 0:
        cx, cy, cw, ch = faces[0]
        
        loc += [cx, cy, cw, ch]
    else:
        loc += [255, 255, 255, 255]
        
print(loc)