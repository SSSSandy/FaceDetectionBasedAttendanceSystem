from Tkinter import *
import ttk

from SqlFunction import GetStatus,SetStatus
from test import createReport
from stuFaceRecog import facerecognizer


def reportView(eRsubjcode, eRbranch, eRsem, window,facultyId):
    reportwindow=Toplevel(window)
    s=eRsubjcode.get()
    s1=eRbranch.get()
    s2=eRsem.get()
    reportwindow.title("Report")
    createReport(reportwindow,eRsubjcode, eRbranch, eRsem,facultyId)

def Aclear(eAsubjcode,eAbranch,eAsem,eAperiod):
    eAbranch.delete(0, END)
    eAsubjcode.delete(0, END)
    eAsem.delete(0, END)
    eAperiod.delete(0, END)

def clear(eAsubjcode,eAbranch,eAsem):
    eAsem.delete(0, END)
    eAbranch.delete(0, END)
    eAsubjcode.delete(0, END)
    return

def Cclear(eCsubjcode,eCbranch,eCsem,eCperiod,eCdate,eCsrno,eCstatus):
    eCstatus.delete(0, END)
    eCbranch.delete(0, END)
    eCdate.delete(0, END)
    eCperiod.delete(0, END)
    eCsem.delete(0, END)
    eCsrno.delete(0, END)
    eCsubjcode.delete(0, END)
    return

def faculty(id, name):
#def faculty():
    facultyId=id
    facultyName=name
    window = Tk()
    window.title("Faculty Control")
    window.geometry("400x450")
    frame = ttk.Frame(window)
    notebook = ttk.Notebook(frame)
    attendance = ttk.Frame(frame)
    Report = ttk.Frame(frame)
    Update=ttk.Frame(frame)
    notebook.add(attendance, text="Attendance")
    notebook.add(Report, text="Report")
    notebook.add(Update,text="Correction")


#Take Attendance Control Details
    wlabel = ttk.Label(attendance, text="Welcome in Attendance Section", font=('times', 15))
    wlabel.grid(sticky=E + W, columnspan=3, padx=10, pady=10)
    hellolabel=ttk.Label(attendance, text="Hello "+facultyName,font=('times',12))
    hellolabel.grid(row=1, columnspan=2, sticky='W',padx=5,pady=5)
    Asubjcode=ttk.Label(attendance, text="Subject Code")
    eAsubjcode=ttk.Entry(attendance, width=30)
    Abranch=ttk.Label(attendance, text="Branch")
    eAbranch = ttk.Entry(attendance, width=30)
    Asem=ttk.Label(attendance, text="Semester")
    eAsem = ttk.Entry(attendance, width=30)
    Aperiod=ttk.Label(attendance, text="Period")
    eAperiod = ttk.Entry(attendance, width=30)
    Asubjcode.grid(row=2,padx=5, sticky='E',pady=5)
    eAsubjcode.grid(row=2, column=1,columnspan=2)
    Abranch.grid(row=3,padx=5, sticky='E',pady=5)
    eAbranch.grid(row=3, column=1,columnspan=2)
    Asem.grid(row=4,padx=5, sticky='E',pady=5)
    eAsem.grid(row=4, column=1,columnspan=2)
    Aperiod.grid(row=5,padx=5, sticky='E',pady=5)
    eAperiod.grid(row=5, column=1,columnspan=2)
    ttk.Button(attendance,text="Start Attendance",
               command=lambda :facerecognizer(eAsubjcode,eAbranch,eAsem,eAperiod,facultyId)).grid(row=6,column=1)
    ttk.Button(attendance, text="Reset",command=lambda :Aclear(eAsubjcode,eAbranch,eAsem,eAperiod)).grid(row=6, column=2)

#Report  Control Details
    wlabel = ttk.Label(Report, text="Welcome in Report Section", font=('times', 15))
    wlabel.grid(sticky=E + W, columnspan=3, padx=10, pady=10)
    hellolabel=ttk.Label(Report, text="Hello "+facultyName,font=('times',12))
    hellolabel.grid(row=1, columnspan=2, sticky='W',padx=5,pady=5)
    Rsubjcode=ttk.Label(Report, text="Subject Code")
    eRsubjcode=ttk.Entry(Report, width=30)
    Rbranch=ttk.Label(Report, text="Branch")
    eRbranch = ttk.Entry(Report, width=30)
    Rsem=ttk.Label(Report, text="Semester")
    eRsem = ttk.Entry(Report, width=30)
    Rsubjcode.grid(row=2,padx=5, sticky='E',pady=5)
    eRsubjcode.grid(row=2, column=1,columnspan=2)
    Rbranch.grid(row=3,padx=5, sticky='E',pady=5)
    eRbranch.grid(row=3, column=1,columnspan=2)
    Rsem.grid(row=4,padx=5, sticky='E',pady=5)
    eRsem.grid(row=4, column=1,columnspan=2)
    ttk.Button(Report,text="View Report",
               command=lambda :reportView(eRsubjcode,eRbranch,eRsem,window,facultyId)).grid(row=5,column=1)
    ttk.Button(Report, text="Reset",command=lambda :clear(eRsubjcode,eRbranch,eRsem)).grid(row=5, column=2)


#Correction Controls Details
    wlabel = ttk.Label(Update, text="Welcome in Correction Section", font=('times', 15))
    wlabel.grid(sticky=E + W, columnspan=3, padx=10, pady=10)
    hellolabel=ttk.Label(Update, text="Hello "+facultyName,font=('times',12))
    hellolabel.grid(row=1, columnspan=2, sticky='W',padx=5,pady=5)
    Csubjcode=ttk.Label(Update, text="Subject Code")
    eCsubjcode=ttk.Entry(Update, width=30)
    Cbranch=ttk.Label(Update, text="Branch")
    eCbranch = ttk.Entry(Update, width=30)
    Csem=ttk.Label(Update, text="Semester")
    eCsem = ttk.Entry(Update, width=30)
    Cperiod=ttk.Label(Update, text="Period")
    eCperiod = ttk.Entry(Update, width=30)
    Csrno=ttk.Label(Update, text="SrNo")
    eCsrno = ttk.Entry(Update, width=30)
    Cdate=ttk.Label(Update, text="Date")
    eCdate = ttk.Entry(Update, width=30)
    Cperiod=ttk.Label(Update, text="Period")
    eCperiod = ttk.Entry(Update, width=30)
    Cstatus=ttk.Label(Update, text="Status")
    eCstatus = ttk.Entry(Update, width=30)
    Csubjcode.grid(row=2,padx=5, sticky='E',pady=5)
    eCsubjcode.grid(row=2, column=1,columnspan=2)
    Cbranch.grid(row=3,padx=5, sticky='E',pady=5)
    eCbranch.grid(row=3, column=1,columnspan=2)
    Csem.grid(row=4,padx=5, sticky='E',pady=5)
    eCsem.grid(row=4, column=1,columnspan=2)
    Csrno.grid(row=5,padx=5, sticky='E',pady=5)
    eCsrno.grid(row=5, column=1,columnspan=2)
    Cdate.grid(row=6,padx=5,pady=5,sticky='E')
    eCdate.grid(row=6,column=1,columnspan=2)
    Cperiod.grid(row=7,padx=5,pady=5,sticky='E')
    eCperiod.grid(row=7,column=1,columnspan=2)
    Cstatus.grid(row=8,sticky='E',padx=5,pady=5)
    eCstatus.grid(row=8,column=1,columnspan=2)
    ttk.Button(Update,text="Get" ,command=lambda:GetStatus(eCsubjcode,eCbranch,eCsem,eCperiod,eCdate,eCsrno,eCstatus,facultyId)).grid(row=7,column=3)
    ttk.Button(Update,text="Update",command=lambda:SetStatus(eCsubjcode,eCbranch,eCsem,eCperiod,eCdate,eCsrno,eCstatus,facultyId)).grid(row=9,column=1)
    ttk.Button(Update, text="Reset",command=lambda:Cclear(eCsubjcode,eCbranch,eCsem,eCperiod,eCdate,eCsrno,eCstatus)).grid(row=9, column=2)

    notebook.grid()
    frame.grid()
    window.mainloop()
#faculty()