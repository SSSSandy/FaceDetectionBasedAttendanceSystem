import tkMessageBox
from Tkinter import*

from Trainner import trainner


def recog(frame):
    label=Label (frame, text="Welcome in Trainer Section", font=('times', 15))
    label.grid(sticky=E + W, columnspan=4)
    # DropDown Menu for Branch Selection
    global branchvar
    blabel = Label(frame, text="Select Branch", font=('times', 10))
    blabel.grid(row=1, column=0, pady=15, sticky=E)
    branchvar = StringVar(frame)
    choice = {'CSE', 'ME', 'ET', 'EE'}
    branchvar.set('CSE')
    ddmenu = OptionMenu(frame, branchvar, *choice)
    ddmenu.grid(row=1, column=1, padx=0, pady=15, sticky=W)

    # Drop Down Menu for Year Selection
    global yvar
    ylabel = Label(frame, text="Select Branch", font=('times', 10))
    ylabel.grid(row=1, column=2, pady=15, sticky=E)
    yvar = IntVar(frame)
    ychoice = {1, 2, 3, 4}
    yvar.set(1)
    ddmenu = OptionMenu(frame, yvar, *ychoice)
    ddmenu.grid(row=1, column=3, pady=15)

    #Button for Recognizer
    recbutton=Button(frame, text="Start Recognizer Training", command=recgnizer)
    recbutton.grid(row=2, columnspan=4)

    return

def recgnizer():
    branch=branchvar.get()
    year=yvar.get()
    batch=branch+str(year)
    flag= trainner(batch)
    if flag is 1:
         tkMessageBox.showinfo("Traning", "Recognition Training successfully Completed")
    else :
        tkMessageBox.showerror("Error", str(flag))
        return