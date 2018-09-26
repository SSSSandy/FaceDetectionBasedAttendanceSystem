import os
import tkMessageBox
import ttk
from Tkinter import*

from DatabaseCreater import databaseCreater
from SqlFunction import *
from recogfunction import recog


def trainerFrame(fram):
    frame = Frame(fram)
    note = ttk.Notebook(frame)
    trframe = ttk.Frame(note)
    recframe = ttk.Frame(note)
    trframe.grid(row=0)
    recframe.grid(row=0, column=1)
    note.add(trframe, text="DataSet")
    note.add(recframe, text="Recognizer")
    note.grid()
    wlabel = Label(trframe, text="Welcome in Trainnig Section", font=('times', 15))
    wlabel.grid(sticky=E + W, columnspan=4)


    # DropDown Menu for Branch Selection
    global branchvar
    blabel = Label(trframe, text="Select Branch", font=('times', 10))
    blabel.grid(row=1, column=0, pady=15, sticky=E)
    branchvar = StringVar(trframe)
    choice = {'CSE', 'ME', 'ET', 'EE'}
    branchvar.set('CSE')
    ddmenu = OptionMenu(trframe, branchvar, *choice)
    ddmenu.grid(row=1, column=1, padx=0, pady=15, sticky=W)


    # Drop Down Menu for Year Selection
    global yvar
    ylabel = Label(trframe, text="Select Branch", font=('times', 10))
    ylabel.grid(row=1, column=2, pady=15)
    yvar = IntVar(trframe)
    ychoice = {1, 2, 3, 4}
    yvar.set(1)
    ddmenu = OptionMenu(trframe, yvar, *ychoice)
    ddmenu.grid(row=1, column=3, pady=15)

    global cancelbutton
    # imageLabel=Label(trframe, text="Image", height=7, width=15, borderwidth=2, relief="solid")
    # imageLabel.grid(row=2, column=4, rowspan=5)
    cancelbutton = Button(trframe, text="Cancel", width=10, command=cancel)
    cancelbutton.grid(row=6, column=2, sticky=W)


    # form Details
    # Global Variable
    global eroll
    global ename
    global esrno
    global esno
    global trainbutton
    global searchbutton
    rollno = Label(trframe, text="Roll No. ")
    rollno.grid(row=2, column=0)
    eroll = Entry(trframe)
    eroll.grid(row=2, column=1)
    searchbutton = Button(trframe, text="search", command=find)
    searchbutton.grid(row=2, column=2, sticky=W)
    name = Label(trframe, text="Name ")
    name.grid(row=3, column=0)
    ename = Entry(trframe)
    ename.grid(row=3, column=1)
    srno = Label(trframe, text="SR No. ")
    srno.grid(row=4, column=0)
    esrno = Entry(trframe)
    esrno.grid(row=4, column=1)
    sno = Label(trframe, text="Serial no")
    sno.grid(row=5, column=0)
    esno = Entry(trframe)
    esno.grid(row=5, column=1)

    # Capture training Data set
    trainbutton = Button(trframe, text="Start", command=startcapture)
    trainbutton.config(width=15)
    trainbutton.grid(row=6, column=1, sticky=E)

    recog(recframe)
    return frame


#Function StartCapture
def startcapture():
    trainbutton.config(state=DISABLED)
    searchbutton.config(state=DISABLED)
    cancelbutton.config(state=DISABLED)
    branch=branchvar.get()
    year=yvar.get()
    rollno=eroll.get()
    name=ename.get()
    srno=esrno.get()
    batch=branch+str(year)
    sn=getsn(batch, rollno)
    mkDirectry(batch)
    status=insert(str(rollno),srno,name,sn,batch)
    if status is not 1:
        tkMessageBox.showerror("Error", str(status))
        enable()
        return
    databaseCreater(batch,sn)
    tkMessageBox.showinfo("Done","Data Successfully Saved")
    enable()
    return


def enable():
    eroll.delete(0, END)
    esrno.delete(0, END)
    ename.delete(0, END)
    esno.delete(0, END)
    trainbutton.config(state=NORMAL)
    searchbutton.config(state=NORMAL)
    cancelbutton.config(state=NORMAL)
    return

def mkDirectry(batch):
    filepath=batch
    if not os.path.exists(filepath):
        f1 = batch + "/dataset"
        f2 = batch + "/Recognizer"
        os.makedirs(f1)
        os.makedirs(f2)
        return

def cancel():
    eroll.delete(0, END)
    esrno.delete(0, END)
    ename.delete(0, END)
    esno.delete(0, END)
    return

def find():
    branch = branchvar.get()
    year = yvar.get()
    batch=branch+str(year)
    roll=eroll.get()
    name,srno,sno=getdetail(batch,roll)
    ename.delete(0, END)
    ename.insert(0, name)
    esrno.delete(0,END)
    esrno.insert(0,srno)
    esno.delete(0,END)
    esno.insert(0,sno)
    return
