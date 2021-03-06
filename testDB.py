import cv2
import numpy as np
import urllib

from FileHalding import addName, Faceeye
from MLBPHFunction import mlbph

url="http://192.168.43.143:8080/shot.jpg"
faceDetector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml");


cam = cv2.VideoCapture(0)
name = 4
path="dataset"
if name is not 0:
        sampleno = 0
        while (True):
            cv2.waitKey(200)
            ret, img = cam.read()

            '''imgResp = urllib.urlopen(url)
            imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
            img = cv2.imdecode(imgNp, -1)'''
            gray = img
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceDetector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                face1 = gray[y:y + h, x:x + w];
                face=cv2.medianBlur(face1,5) #MLBPH Implimetation
                i = Faceeye(face)  # Check For eye in Sample Image
                if i == 2:
                    sampleno = sampleno + 1;
                    cv2.putText(img, "FaceCapture" + str(sampleno), (x + w / 2, y - 5), cv2.FONT_HERSHEY_DUPLEX, .4,
                                (255, 255, 255))
                    cv2.imwrite(path+"/user." + str(name) + "." + str(sampleno) + ".jpg", face)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.waitKey(200)
                    cv2.imshow("Captured", face)
            cv2.imshow("face", img);
            if (sampleno >= 15):
                break;
        #cam.release();
        cv2.destroyAllWindows();