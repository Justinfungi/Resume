import cv2 as cv
import numpy as np


people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling',"Cats"]
haar_cascade = cv.CascadeClassifier("haar_face.xml")

#features= np.load("features.npy")
#labels=np.load("labels.npy")
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("faced_train.yml")


capture = cv.VideoCapture(0)
# if argument is 0, turn on camera
while True:
    istrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 13)
    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h,x:x+w]
        label, confidence = face_recognizer.predict(faces_roi)
        print(f'{people[label]} with a confidence of {confidence}')
        if confidence >= 70:
            cv.putText(frame, str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("Video",frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break
capture.release()
cv.destroyAllWindows
