import os
import tkMessageBox
import ttk
from Tkinter import*

from DatabaseCreater import databaseCreater
from SqlFunction import *
from recogfunction import recog


def getmgframe(awindow):
    frame=ttk.Frame(awindow)
    tabs=ttk.Notebook(frame)
    admin=ttk.Frame(frame)
    faculty=ttk.Frame(frame)
    subj=ttk.Frame(frame)
    drop=ttk.Frame(frame)
    tabs.add(admin, text="Add Admin")
    tabs.add(faculty, text="Add Faculty")
    tabs.add(subj, text="Add Subject")
    tabs.add(drop, text="Drop Table")
    tabs.grid()

# Detail Add Admin Frame
    wlabel = Label(admin, text="Welcome in Add Admin Section", font=('times', 15))
    wlabel.grid(sticky=E + W, columnspan=3,padx=10, pady=10)
    adminId=ttk.Label(admin, text="Admin ID")
    eadminId=Entry(admin, width=25)
    ttk.Button(admin, text='Search',
                        command=lambda: findAdmin(eadminId, eadminName, eadminUserName, eadminpass, eadminpass2,
                                                 eadminHint)).grid(row=1,column=4,sticky='W')
    adminName = ttk.Label(admin, text="Admin Name")
    eadminName = Entry(admin, width=25)
    adminUserName = ttk.Label(admin, text="Admin UserName")
    eadminUserName = Entry(admin, width=25)
    adminpass = ttk.Label(admin, text="Password")
    eadminpass = Entry(admin, width=25, show='*')
    adminpass2 = ttk.Label(admin, text="Re-Enter Pass")
    eadminpass2 = Entry(admin, width=25)
    adminHint=ttk.Label(admin, text="Password Hint")
    eadminHint = Entry(admin, width=25)
    adminId.grid(row=1,padx=5, sticky='E',pady=5)
    eadminId.grid(row=1,column=1, columnspan=2)
    adminName.grid(row=2,padx=5, sticky='E',pady=5)
    eadminName.grid(row=2, column=1, columnspan=2)
    adminUserName.grid(row=3, padx=5, sticky='E', pady=5)
    eadminUserName.grid(row=3, column=1, columnspan=2)
    adminpass.grid(row=4,padx=5, sticky='E',pady=5)
    eadminpass.grid(row=4,column=1, columnspan=2)
    adminpass2.grid(row=5,padx=5, sticky='E',pady=5)
    eadminpass2.grid(row=5, column=1, columnspan=2)
    adminHint.grid(row=6,padx=5, sticky='E',pady=5)
    eadminHint.grid(row=6, column=1, columnspan=2)
    submit=ttk.Button(admin, text='ADD New', command=lambda :addAdmin(eadminId,eadminName,eadminUserName,eadminpass,eadminpass2,eadminHint))
    submit.grid(row=7,column=1, sticky='E')
    clear=ttk.Button(admin, text='Update',command=lambda: updateAdmin(eadminId,eadminName,eadminUserName,eadminpass,eadminpass2,eadminHint))
    clear.grid(row=7, column=2)
    ttk.Button(admin, text='Clear',
    command=lambda: clearAdmin(eadminId, eadminName, eadminUserName, eadminpass, eadminpass2, eadminHint)).grid(row=7,column=4,sticky='W')
    style=ttk.Style()
    style.configure('TLabel', foreground='blue')

# Add Faculty Details
    label = Label(faculty, text="Welcome in Add Faculty Section", font=('times', 15))
    label.grid(sticky=E + W, columnspan=3, padx=10, pady=10)
    facultyId=ttk.Label(faculty, text='Faculty ID')
    efacultyId=Entry(faculty, width=25)
    ttk.Button(faculty, text='Search',
               command=lambda: findfaculty(efacultyId,efacultyName,efacultyUserName,efacultyPass,efacultyPass2,efacultyHint)).grid(row=1, column=3, sticky='W')
    facultyName = ttk.Label(faculty, text='Faculty Name')
    efacultyName = Entry(faculty, width=25)
    facultyUserName = ttk.Label(faculty, text='Faculty User Name')
    efacultyUserName = Entry(faculty, width=25)
    facultyPass = ttk.Label(faculty, text='Password')
    efacultyPass = Entry(faculty, width=25, show='*')
    facultyPass2 = ttk.Label(faculty, text='Re-Enter Password')
    efacultyPass2 = Entry(faculty, width=25)
    facultyHint = ttk.Label(faculty, text='Password Hint')
    efacultyHint = Entry(faculty, width=25)
    facultyId.grid(row=1,sticky='E',padx=5,pady=5)
    efacultyId.grid(row=1,column=1, columnspan=2)
    facultyName.grid(row=2, sticky='E',padx=5,pady=5)
    efacultyName.grid(row=2, column=1, columnspan=2)
    facultyUserName.grid(row=3, sticky='E',padx=5,pady=5)
    efacultyUserName.grid(row=3, column=1, columnspan=2)
    facultyPass.grid(row=4, sticky='E',padx=5,pady=5)
    efacultyPass.grid(row=4, column=1, columnspan=2)
    facultyPass2.grid(row=5, sticky='E',padx=5,pady=5)
    efacultyPass2.grid(row=5, column=1, columnspan=2)
    facultyHint.grid(row=6, sticky='E',padx=5,pady=5)
    efacultyHint.grid(row=6, column=1, columnspan=2)
    ttk.Button(faculty,text='Add New',
                command= lambda:AddFaculty(efacultyId,efacultyName,efacultyUserName,efacultyPass,efacultyPass2,efacultyHint)).grid(row=7,column=1,sticky="E")
    ttk.Button(faculty, text='Update',
               command=lambda: updateFaculty(efacultyId, efacultyName, efacultyUserName, efacultyPass, efacultyPass2,
                                          efacultyHint)).grid(row=7, column=2, sticky="E")
    ttk.Button(faculty, text='Clear',command=lambda:clearFaculty(efacultyId,efacultyName,efacultyUserName,efacultyPass,efacultyPass2,efacultyHint)).grid(row=7, column=3, sticky="W")

#Add Subject
    slabel = Label(subj, text="Welcome in Add Subject Section", font=('times', 15))
    slabel.grid(sticky=E + W, columnspan=3, padx=10, pady=10)
    subjCode=ttk.Label(subj, text="Subject Code")
    esubjCode=Entry(subj, width=30)
    ttk.Button(subj, text='Search',
               command=lambda: findSubject(esubjCode,esubjName,esubjFacultyId,esubjBranch,esubjSem)).grid(row=1, column=3, sticky='W')
    subjName=ttk.Label(subj, text='Subject Name')
    esubjName = Entry(subj, width=30)
    subjFacultyId = ttk.Label(subj, text='Faculty Id')
    esubjFacultyId = Entry(subj, width=30)
    subjBranch = ttk.Label(subj, text='Branch')
    esubjBranch = Entry(subj, width=30)
    subjSem = ttk.Label(subj, text='Semester')
    esubjSem = Entry(subj, width=30)
    subjCode.grid(row=1, sticky='E',padx=5,pady=5)
    esubjCode.grid(row=1, column=1,columnspan=2)
    subjName.grid(row=2, sticky='E',padx=5,pady=5)
    esubjName.grid(row=2, column=1,columnspan=2)
    subjFacultyId.grid(row=3, sticky='E',padx=5,pady=5)
    esubjFacultyId.grid(row=3, column=1,columnspan=2)
    subjBranch.grid(row=4, sticky='E',padx=5,pady=5)
    esubjBranch.grid(row=4, column=1,columnspan=2)
    subjSem.grid(row=5, sticky='E',padx=5,pady=5)
    esubjSem.grid(row=5, column=1,columnspan=2)
    ttk.Button(subj, text='Add New',
      command=lambda: AddSubj(esubjCode,esubjName,esubjFacultyId,esubjBranch,esubjSem)).grid(row=6,column=1, sticky='E')
    ttk.Button(subj, text='Update',
               command=lambda: updateSubj(esubjCode, esubjName, esubjFacultyId, esubjBranch,esubjSem)).grid(row=6,column=2,sticky='W')
    ttk.Button(subj, text='Clear',command=lambda: clearSubj(esubjCode,esubjName,esubjFacultyId,esubjBranch,esubjSem)).grid(row=6, column=3, sticky='W')

    # Add Drop Details
    label = Label(drop, text="Welcome in Drop Table Section", font=('times', 15))
    label.grid(sticky=E + W, columnspan=3, padx=10, pady=10)
    dtable = ttk.Label(drop, text="Table Name")
    edtable = Entry(drop, width=20)
    dtable.grid(row=1, sticky='E', padx=5, pady=5)
    edtable.grid(row=1, column=1, columnspan=2)
    ttk.Button(drop, text='Drop', command=lambda :dropTable(edtable)).grid(row=2, column=1, sticky='E')
    ttk.Button(drop, text='Clear Table', command=lambda :clearTable(edtable)).grid(row=2, column=2, sticky='W')


# return of this Function
    return frame


def clearAdmin(eadminId, eadminName, eadminUserName, eadminpass, eadminpass2, eadminHint):
    eadminId.delete(0, END)
    eadminName.delete(0, END)
    eadminUserName.delete(0, END)
    eadminpass.delete(0, END)
    eadminpass2.delete(0, END)
    eadminHint.delete(0, END)
    return


def clearFaculty(efacultyId,efacultyName,efacultyUserName,efacultyPass,efacultyPass2,efacultyHint):
    efacultyId.delete(0, END)
    efacultyName.delete(0, END)
    efacultyUserName.delete(0, END)
    efacultyPass.delete(0, END)
    efacultyPass2.delete(0, END)
    efacultyHint.delete(0, END)
    return

def clearSubj(esubjCode, esubjName, esubjFacultyId, esubjBranch, esubjSem):
    esubjCode.delete(0, END)
    esubjName.delete(0, END)
    esubjFacultyId.delete(0, END)
    esubjBranch.delete(0, END)
    esubjSem.delete(0, END)
    return