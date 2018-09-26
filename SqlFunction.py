import sqlite3
import tkMessageBox
from Tkinter import*

import math


def getsn(batch,roll):
    name,srno,sn=getdetail(batch, roll)
    return sn


def getdetail(batch,roll):
    name=""
    srno=""
    query = " create table if not exists "+batch +" (Rollno INTEGER PRIMARY KEY NOT NULL,SRno INTEGER UNIQUE NOT NULL,name STRING NOT NULL,sno INTEGER UNIQUE NOT NULL)"
    query2 = "select rollno,name,srno,sno from " + batch+" where Rollno="+roll
    con = sqlite3.connect("Student.db")
    con.execute(query)
    con.commit()
    try:

        cursor = con.execute(query2)
        cursor_blank = 0
        for n in cursor:
            sn = n
            cursor_blank = 1
        if cursor_blank is 1:
            srno=sn[2]
            name=sn[1]
            sn=sn[3]
            con.commit()
            con.close()
            return name, srno, sn
        query = "select count(sno) from " + batch
        cursor = con.execute(query)
        for n in cursor:
            sn = str(n)
        sn = sn[1:sn.index(',')]
        sn = int(sn)
        return name, srno, sn + 1
    except Exception,e :
        print e
        return name,srno, e


def insert(rollno,srno,name,sno,batch):
    try:
        con = sqlite3.connect("Student.db")
        query = "select name from " + batch + " where sno=" + str(sno)
        cursor = con.execute(query)
        cursor_blank = 0
        for n in cursor:
            sn = str(n)
            cursor_blank = 1
        if cursor_blank is 1:
            con.commit()
            con.close()
            con = sqlite3.connect("Student.db")
            query = "update " + batch + " set Rollno=?, srno=?, name=? where sno=?"
            con.execute(query, (rollno, srno, name, sno))
            con.commit()
            con.close()
            return 1
        query = "insert into " + batch + "(rollno, srno, name, sno) values(?,?,?,?)"
        con.execute(query, (rollno, srno, name, sno))
        con.commit()
        con.close()
        return 1
    except Exception,e:
        print e
        return e


def getcredential(username, pawd):
    con = sqlite3.connect("Student.db")
    query = "select adminID from admin where username= '"+str(username) +"' and Pass= '"+str(pawd)+"'"
    cursor = con.execute(query)
    cursor_blank = 0
    for n in cursor:
        sn = str(n)
        cursor_blank = 1
    if cursor_blank is 1:
        con.commit()
        con.close()
        return 1
    else:
        con.commit()
        con.close()
        return 0

# Add Admin
def addAdmin(eadminId, eadminName, eadminUserName, eadminpass, eadminpass2, eadminHint):
    try:
        if eadminpass.get() != eadminpass2.get() :
            raise Exception("Both password are not same !!!")
        con=sqlite3.connect("Student.db")
        query="insert into admin (adminID, username, pass,name, hint) values(?,?,?,?,?)"
        con.execute(query,(eadminId.get(),eadminUserName.get(),eadminpass.get(),eadminName.get(),eadminHint.get()))
        con.commit()
        query = "insert into faculty (ID, name, username,pass, hint) values(?,?,?,?,?)"
        con.execute(query,(eadminId.get(), eadminName.get(),eadminUserName.get(),eadminpass.get(),eadminHint.get()))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Done", "Data Successfully Saved")
        eadminId.delete(0,END)
        eadminName.delete(0,END)
        eadminUserName.delete(0,END)
        eadminpass.delete(0,END)
        eadminpass2.delete(0,END)
        eadminHint.delete(0,END)
        return
    except Exception, e:
        print e
        tkMessageBox.showerror("Error", e)
        return

# Search Admin
def findAdmin(eadminId, eadminName, eadminUserName, eadminpass, eadminpass2, eadminHint):
    query="select * from admin where adminid=?"
    try:
        con=sqlite3.connect("Student.db")
        cursor=con.execute(query, eadminId.get())
        cursor_blank = 0
        for n in cursor:
            sn = n
            cursor_blank = 1
        if cursor_blank is 1:
            eadminUserName.delete(0,END)
            eadminUserName.insert(0,sn[1])
            eadminpass.delete(0,END)
            eadminpass.insert(0,sn[2])
            eadminpass2.delete(0,END)
            eadminpass2.insert(0,sn[2])
            eadminName.delete(0,END)
            eadminName.insert(0,sn[3])
            eadminHint.delete(0,END)
            eadminHint.insert(0,sn[4])
        else:
            tkMessageBox.showinfo("Details", "No Detail Found")
            con.close()
    except Exception, e:
        tkMessageBox.showerror("Error", e)
        con.close()
        return



# Update Admin Info
def updateAdmin(eadminId, eadminName, eadminUserName, eadminpass, eadminpass2, eadminHint):
    query="update admin set username=?, pass=?, name=?, hint=? where adminid= ?"
    try:
        con=sqlite3.connect("Student.db")
        if eadminpass.get() != eadminpass2.get() :
            raise Exception("Both password are not same !!!")
        con.execute(query,(eadminUserName.get(),eadminpass.get(),eadminName.get(),eadminHint.get(),eadminId.get()))
        con.commit()
        tkMessageBox.showinfo("Done", "Saved Successfully")
    except Exception , e:
        tkMessageBox.showerror("Error", e)
        con.close()
        return




#Add Faculty
def AddFaculty(efacultyId, efacultyName, efacultyUserName, efacultyPass, efacultyPass2, efacultyHint):
    try:
        if efacultyPass.get() != efacultyPass2.get() :
            raise Exception("Both password are not same !!!")
        con=sqlite3.connect("Student.db")
        query="insert into faculty (ID, name, username,pass, hint) values(?,?,?,?,?)"
        con.execute(query,(efacultyId.get(),efacultyName.get(),efacultyUserName.get(),efacultyPass.get(),efacultyHint.get()))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Done", "Data Successfully Saved")
        efacultyId.delete(0,END)
        efacultyName.delete(0,END)
        efacultyUserName.delete(0,END)
        efacultyPass.delete(0,END)
        efacultyPass2.delete(0,END)
        efacultyHint.delete(0,END)
        return
    except Exception, e:
        print e
        tkMessageBox.showerror("Error", e)
        return


# Find Faculty
def findfaculty(efacultyId, efacultyName, efacultyUserName, efacultyPass, efacultyPass2, efacultyHint):
    query="Select * from faculty where ID=?"
    try:
        con=sqlite3.connect("Student.db")
        cursor=con.execute(query,(efacultyId.get()))
        cursor_blank=0
        for n in cursor:
            sn = n
            cursor_blank = 1
        if cursor_blank is not 1:
            tkMessageBox.showinfo("Detail", "No Details Found")
            con.close()
            return
        efacultyName.delete(0,END)
        efacultyName.insert(0,n[1])
        efacultyUserName.delete(0,END)
        efacultyUserName.insert(0,n[1])
        efacultyPass.delete(0,END)
        efacultyPass.insert(0,n[2])
        efacultyPass2.delete(0,END)
        efacultyPass2.insert(0,n[2])
        efacultyHint.delete(0,END)
        efacultyHint.insert(0,n[3])
        return
    except Exception, e:
        tkMessageBox.showerror("Error", e)
        return


# Update faculty info
def updateFaculty(efacultyId, efacultyName, efacultyUserName, efacultyPass, efacultyPass2, efacultyHint):
    query="update faculty set name=?, username=?, pass=?, hint=? where id=?"
    try:
        con=sqlite3.connect("Student.db")
        if efacultyPass.get() != efacultyPass2.get() :
            raise Exception("Both password are not same !!!")
        con.execute(query,(efacultyName.get(),efacultyUserName.get(), efacultyPass.get(), efacultyHint.get(),efacultyId.get()))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Done","Values Updated")
    except Exception, e:
        tkMessageBox.showerror("Error", e)
        return


#Add Subj
def AddSubj(esubjCode, esubjName, esubjFacultyId, esubjBranch, esubjSem):
    try:
        con=sqlite3.connect("Student.db")
        con.execute("PRAGMA foreign_keys = ON")
        con.commit()
        year = int(math.ceil(float(esubjSem.get()) / 2))
        query = "insert into subj (subjCode,subjname,facultyid,branch,sem) values(?,?,?,?,?)"
        con.execute(query,
                    (esubjCode.get(), esubjName.get(), int(esubjFacultyId.get()), esubjBranch.get(), esubjSem.get()))
        con.commit()
        batch = esubjBranch.get() + str(year)
        studentno = "select sno from " + batch
        result = con.execute(studentno)
        column = ""
        for sn in result:
            #sno = sn[1:sn.__len__ -2]
            column = column +"STU"+str(sn[0]) + " STRING,"
        tablename = esubjCode.get() + esubjBranch.get() + esubjSem.get()
        # Create Table for subject
        query = "create table " + tablename + "( date  DATE, Period INTEGER, " + column+ " PRIMARY KEY(date, Period));"
        con.execute(query)
        con.commit()
        con.close()
        tkMessageBox.showinfo("Done", "Data Successfully Saved")
        esubjCode.delete(0, END)
        esubjName.delete(0, END)
        esubjFacultyId.delete(0, END)
        esubjBranch.delete(0, END)
        esubjSem.delete(0, END)
        return
    except Exception,e:
        tkMessageBox.showerror("Error", e)
        con.close()
        return

# Find Subject Details
def findSubject(esubjCode, esubjName, esubjFacultyId, esubjBranch, esubjSem):
    query="select * from subj where subjcode= '"+esubjCode.get()+"'"
    try:
        con = sqlite3.connect("Student.db")
        cursor = con.execute(query)
        cursor_blank = 0
        for n in cursor:
            sn = n
            cursor_blank = 1
        if cursor_blank is not 1:
            tkMessageBox.showinfo("Detail", "No Details Found")
            con.close()
            return
        esubjName.delete(0,END)
        esubjName.insert(0,n[1])
        esubjFacultyId.delete(0,END)
        esubjFacultyId.insert(0,n[2])
        esubjBranch.delete(0,END)
        esubjBranch.insert(0,n[3])
        esubjSem.delete(0,END)
        esubjSem.insert(0,n[4])
        return
    except Exception,e:
        tkMessageBox.showerror("Error", e)
        con.close()
        return


# Update Subject Details
def updateSubj(esubjCode, esubjName, esubjFacultyId, esubjBranch, esubjSem):
    query="update subj set subjname=?, facultyid=?,branch=?,sem=? where subjcode=?"
    try:
        con=sqlite3.connect("Student.db")
        con.execute(query,(esubjName.get(), esubjFacultyId.get(), esubjBranch.get(),esubjSem.get(),esubjCode.get()))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Done", "Values Updated")
    except Exception, e:
        con.close()
        tkMessageBox.showerror("Error", e)
        return


#Drop Table
def dropTable(edtable):
    query="drop table "+edtable.get()
    try:
        con=sqlite3.connect("Student.db")
        con.execute(query)
        con.commit()
        con.close()
        tkMessageBox.showinfo("Done", "Table Dropped Successfully")
        edtable.delete(0,END)
        return
    except Exception,e:
        tkMessageBox.showerror("Error", e)
        con.close()
        return

# Delete All Vaulue from table Clear Table
def clearTable(edtable):
    query="delete  from "+edtable.get()
    try:
        con=sqlite3.connect("Student.db")
        con.execute(query)
        con.commit()
        con.close()
        tkMessageBox.showinfo("Done", "Table Empty Successfully")
        edtable.delete(0,END)
        return
    except Exception,e:
        tkMessageBox.showerror("Error", e)
        con.close()
        return

#Faculty Login Function
def facultylogin(etuser, etpass):
    try:
        id=""
        name=""
        con=sqlite3.connect("Student.db")
        query="select ID, name from Faculty where username=? and  pass=?"
        cursor=con.execute(query,(etuser.get(),etpass.get()))
        cursor_blank = 0
        for idname in cursor:
            id=idname[0]
            name=idname[1]
            cursor_blank=1
        if cursor_blank is not 1:
            con.close()
            return "", "", "No Credential found"
        else:
            con.close()
            return id, name, ""
    except Exception, e:
        con.close()
        return "", "", e

#For Attandance Sql

def attendance(ids, table,eAperiod):
    if ids=="":
        return
    try:
        con=sqlite3.connect("Student.db")
        query="update "+table+" set "+ids+" where date= date('now') and period= "+eAperiod.get()
        print(query)
        con.execute(query)
        con.commit()
        con.close()
        return
    except Exception,e:
        tkMessageBox.showerror("Error", e)
        con.close()
        return


#Get Attandance Status
def GetStatus(eAsubjcode,eAbranch,eAsem,eAperiod,eAdate,eAsrno,eAstatus,facultyId):
    con=sqlite3.connect("Student.db")
    year = int(math.ceil(float(eAsem.get()) / 2))
    batch = eAbranch.get() + str(year)
    s = eAsem.get()
    s1 = eAsubjcode.get()
    s2 = eAbranch.get()
    tablename = eAsubjcode.get() + eAbranch.get() + eAsem.get()
    try:
        query = "select FacultyID from subj where subjCode= '" + eAsubjcode.get() + "'"
        result = con.execute(query)
        for rs in result:
            if rs[0] is not facultyId:
                raise Exception("You are Not Authorised")
        query="select sno from "+batch+" where srno="+eAsrno.get()
        result=con.execute(query)
        cursor_blank=0
        for rs in result:
            sno = rs[0]
        sno = "STU" + str(sno)
        query = "select " + sno + " from " + tablename + " where date= '" + eAdate.get() + "' and period=" + eAperiod.get()
        result = con.execute(query)
        for rs in result:
            eAstatus.delete(0, END)
            for n in rs:
                cursor_blank = n
            if cursor_blank is None:
                eAstatus.insert(0, "A")
                return
            eAstatus.insert(0, (rs[0]))
            return
    except Exception,e:
        tkMessageBox.showerror("Error", e)
        return

def SetStatus(eCsubjcode,eCbranch,eCsem,eCperiod,eCdate,eCsrno,eCstatus,facultyId):
    con = sqlite3.connect("Student.db")
    year = int(math.ceil(float(eCsem.get()) / 2))
    batch = eCbranch.get() + str(year)
    tablename = eCsubjcode.get() + eCbranch.get() + eCsem.get()
    try:
        query = "select FacultyID from subj where subjCode= '" + eCsubjcode.get() + "'"
        result = con.execute(query)
        for rs in result:
            if rs[0] is not facultyId:
                raise Exception("You are Not Authorised")
        query = "select sno from " + batch + " where srno=" + eCsrno.get()
        result = con.execute(query)
        for rs in result:
            sno = rs[0]
        sno = "STU" + str(sno)
        query = "Update "+tablename+" set "+sno+" ='"+eCstatus.get()+"' where date= '"+eCdate.get()+"' and period= "+eCperiod.get()
        con.execute(query)
        con.commit()
        tkMessageBox.showinfo("Done", "Data Successfully Saved")
    except Exception,e:
        tkMessageBox.showerror("Error", e)
        return
