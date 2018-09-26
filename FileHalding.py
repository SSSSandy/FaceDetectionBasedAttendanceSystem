import sqlite3
def addName():
    id=raw_input('Enter Student Id ')
    name=raw_input('Enter Student name ')
    con=sqlite3.connect("Student.db")
    query='select Id from SdtDetail where id='+str(id)
    isAlreadyExisted=0
    cursor=con.execute(query)
    for row in cursor :
        isAlreadyExisted=1
    if isAlreadyExisted==1 :
        print("Student Already Registerd ")
        return 0
    else:
        query="Insert into SdtDetail (ID,Name) values("+str(id)+",'"+str(name)+"')"
    con.execute(query)
    con.commit()
    con.close()
    return id;

def presentId(i):
    con = sqlite3.connect("Student.db")
    query="Update CSE4 set Present='P' where id="+str(i)
    con.execute(query)
    con.commit()
    con.close()
    return

def getName(id):
    name=None
    con=sqlite3.connect("Student.db")
    query='Select name from CSE4 where sno='+str(id)
    cursor=con.execute(query)
    for n in cursor:
        name=str(n)
    con.close()
    name=name[3:]
    n=name.index(',')
    name=name[0:n-1]
    return name

import cv2
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def Faceeye(faces):
        eye = eye_cascade.detectMultiScale(faces)
        i=0
        for (ex, ey, ew, eh) in eye:
            i=i+1
        print "Detected Eye "+str(i)
        return i