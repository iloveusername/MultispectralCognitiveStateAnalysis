import cv2
# import numpy as np
# from scipy.io import savemat

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('./Face/test.jpg')

loc = [0, 0, 0, 0]

faces = face_cascade.detectMultiScale(img, 1.1, 4)

if len(faces) != 0:
    cx, cy, cw, ch = faces[0]
    print(faces[0])

    loc = [cx, cy, cw, ch]
    # print(cw, ch)
    
    # cv2.rectangle(img, (cx, cy), (cx+cw, cy+ch), (0, 0, 255), 2)

# loc = np.asarray(loc)
# mymat = {'loc': loc}

# savemat("face_location.mat", mymat)



# cv2.imshow('Image', img)

# cv2.waitKey(0)
 
# cv2.destroyAllWindows()