import cv2
import numpy as np

from FileHalding import getName

faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
cam = cv2.VideoCapture(0);
rec = cv2.createEigenFaceRecognizer(15,4000);
rec.load("recognizer\EigentrainnigData.yml")
id = 0;
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 1, 2, 0, 1)
while (True):
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        eigenface=cv2.resize((gray[y:y + h, x:x + h]),(110,110))
        id, conf = rec.predict(eigenface)
        if (conf < 1400):
            id = getName(id)
            cv2.cv.PutText(cv2.cv.fromarray(img), str(id) + " ," + str(conf), (x, y + h), font, 255);
    cv2.imshow("Eigenface", img);
    if (cv2.waitKey(1) == ord("q")):
        break;

cam.release();
cv2.destroyAllWindows();

