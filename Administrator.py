from Tkinter import*
import os

from Mfunction import getmgframe
from Tfunctiion import*


def Admin():
    global frame
    global awindow
    global trframe
    global mgframe
    awindow=Tk()
    awindow.title("Admin Panel")
    awindow.geometry("620x350")
    frame = Frame(awindow)
    frame.config(padx=70, pady=50)
    frame.grid(row=0)
#button for Trainer
    tbutton=Button(frame,text="Registration", command=trainer)
    tbutton.config(font=('times',25))
    #tbutton.config(width=10, height=10)
    tbutton.grid(row=1,column=0)
# button for Management
    mbutton = Button(frame, text="Management", command=manage)
    mbutton.config(font=('times', 25))
    # tbutton.config(width=10, height=10)
    mbutton.grid(row=1,column=1, padx=100)

    trframe=trainerFrame(awindow)
    mgframe = getmgframe(awindow)
    awindow.wait_window()

def trainer():
    Button(awindow, text=" Back ", command=back,width=7).grid(row=0, column=1, sticky=NE)
    awindow.columnconfigure(0, weight=3)
    frame.grid_forget()
    trframe.grid(sticky=NW, row=0, column=0)


def manage():
    Button(awindow, text=" Back ", command=back,width=7).grid(row=0, column=1, sticky=NE)
    awindow.columnconfigure(0, weight=3)
    frame.grid_forget()
    mgframe.grid(sticky=NW, row=0, column=0)


def back():
    trframe.grid_forget()
    mgframe.grid_forget()
    Button(awindow, text="LogOut", command=logout,width=7).grid(row=0, column=1, sticky=NE)
    frame.grid()

def logout():
    awindow.destroy()

# Make this Comment before run project
#Admin()
