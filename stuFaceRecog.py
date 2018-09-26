import tkMessageBox
import time
import cv2
import math
import sqlite3
from FileHalding import presentId, presentId, getName
from SqlFunction import attendance


def facerecognizer(eAsubjcode, eAbranch, eAsem, eAperiod,facultyId):
#Sql Query
 cam = cv2.VideoCapture(0)
 s1=eAsem.get()
 try:
    table=eAsubjcode.get()+eAbranch.get()+eAsem.get()
    Date="date('now')"
    con = sqlite3.connect("Student.db")
    query = "select FacultyID from subj where subjCode= '" + eAsubjcode.get() + "'"
    result = con.execute(query)
    for rs in result:
        if rs[0] is not facultyId:
            raise Exception("You are Not Authorised")
    batch=eAbranch.get()+str(int(math.ceil(float(eAsem.get())/2)))
    query="insert into "+table+" (date,period) values ("+Date+ ","+eAperiod.get()+")"
    con.execute(query)
    con.commit()
    query = 'select sno from '+batch
    cursor = con.execute(query)
    l = []
    for row in cursor:
        #st = str(row)
        #ids = st[1:st.index(',')]
        ids=row[0]
        l.append(int(ids))
    No_of_Times_face_recognize = []
    for i in l:
        No_of_Times_face_recognize.append(0)
    print l

    faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # rec = cv2.createLBPHFaceRecognizer(radis,nebhiours,grid x,grid y)
    rec = cv2.createLBPHFaceRecognizer()
    rec.load(batch+"\Recognizer\LBPHtrainnigData.yml")
    id = 0
    font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_DUPLEX, 1, 1, 0, 1)
    timeout=time.time()+60
    #print "Timeout  - "+str(timeout)
    while (timeout>time.time()):
        #print(time.time())
        i = 1
        while (i < 31):
            ret, img = cam.read();
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceDetector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, conf = rec.predict(cv2.medianBlur((gray[y:y + h, x:x + h]),5))  # MLBPH Implimented
                if (conf < 50):
                    # find index of recognize face id in List
                    index = l.index(id)
                    # NO of times a face Detect
                    No_of_Times_face_recognize[index] = 1 + No_of_Times_face_recognize[index]
                    i = i + 1
                    name = getName(id)
                    cv2.cv.PutText(cv2.cv.fromarray(img),
                                   str(name) + " ," + str(conf), (x, y + h), font, (0, 0, 255));
            cv2.imshow("LBPHface", img);
            cv2.waitKey(20)
            #print i
        cv2.destroyAllWindows();
        rt = 0
        ids=""
        for No_of_Times_face_recognize_items in No_of_Times_face_recognize:
            if (No_of_Times_face_recognize_items > 18):
                recId = l[rt]
                ids="STU"+str(recId)+"='P', "
                print 'Present ' + str(recId)
                attendance(ids[0:-2], table,eAperiod)
            rt = rt + 1

        con.close()
        for i in range(rt):
            No_of_Times_face_recognize[i] = 0
        print No_of_Times_face_recognize
        cv2.waitKey(200)
        if (cv2.waitKey(1) == ord("q")):
            break;
 except Exception as e:
     print e
     tkMessageBox.showerror("Error", e)
     con.close()
     cam.release()
     return