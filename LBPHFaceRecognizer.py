import cv2
import numpy as np
import sqlite3
import urllib
from FileHalding import presentId, presentId, getName


#databaseCreater()
#trainner()
from MLBPHFunction import mlbph

con=sqlite3.connect("Student.db")
query='select sno from CSE4'
cursor=con.execute(query)
l=[]
for row in cursor:
    for r in row:
     l.append(int(r))
No_of_Times_face_recognize=[]
for i in l:
    No_of_Times_face_recognize.append(0)
print l
faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)
#rec = cv2.createLBPHFaceRecognizer(radis,nebhiours,grid x,grid y)
rec = cv2.createLBPHFaceRecognizer()
rec.load("Recognizer\LBPHtrainnigData.yml")
id = 1
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_DUPLEX, 1, 1, 0, 1)
url="http://192.168.43.143:8080/shot.jpg"
while (True):
    i = 1
    while (i < 30):
        '''imgResp = urllib.urlopen(url)
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)'''
        ret, img = cam.read();
        img = cv2.flip(img,1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, conf = rec.predict(cv2.medianBlur((gray[y:y + h, x:x + h]),5))
            print id
            print conf
            if (conf < 100):
                # find index of recognize face id in List
                index = l.index(id)
                # NO of times a face Detect
                No_of_Times_face_recognize[index]=1 + No_of_Times_face_recognize[index]
                i = i + 1
                name=getName(id)
                cv2.cv.PutText(cv2.cv.fromarray(img), str(name) + " ," + str(conf), (x, y + h), font, (0, 0, 255));
        cv2.imshow("LBPHface", img);
        cv2.waitKey(20)
       # print i
    cv2.destroyAllWindows();
    rt=0
    for No_of_Times_face_recognize_items in No_of_Times_face_recognize:
        if(No_of_Times_face_recognize_items>18):
            recId=l[rt]
            #presentId(recId)
            print 'Present ' + str(recId)
        rt=rt+1
    rt=0
    for N in No_of_Times_face_recognize:
        No_of_Times_face_recognize[rt]=0
        rt=rt+1

    if (cv2.waitKey(200) == ord("q")):
        break;


