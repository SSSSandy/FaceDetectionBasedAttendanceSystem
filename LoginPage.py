import ttk

from Administrator import Admin
from Faculty import faculty
from ForgetPass import forgetAdmin
from SqlFunction import *


def Window():
    global userEntry
    global passEntry
    global window
    window = Tk()
    window.geometry("740x350")
    window.title("LoginPage")
    wframe=ttk.Labelframe(window)
# Defining Administrator Login Frame
    labelfont=('times',40,'bold')
    adminframe=Frame(wframe, width=250, height=200)
    adminframe.config(highlightbackground="BLACK", highlightcolor="BLACK", highlightthickness=3)
    adminframe.pack(side=LEFT,padx=25, pady=50)
    infoLabel = Label(adminframe, text="  Administrator Login  ")
    infoLabel.config(font=('times',18))
    infoLabel.grid(columnspan=2)
    userLabel = Label(adminframe, text="UserName:")
    userLabel.grid(row=1, sticky=E)
    passLabel = Label(adminframe, text="Password:")
    passLabel.grid(column=0, row=2, sticky=E)
    userEntry = Entry(adminframe, width=25)
    userEntry.grid(row=1, column=1, columnspan=2)
    passEntry = Entry(adminframe, show="*", width=25)
    passEntry.grid(row=2, column=1,columnspan=2)
    abutton=Button(adminframe,text="Login", command=adminLogin)
    abutton.config(width=10)
    abutton.grid(row=3, column=1, sticky='E')
    Button(adminframe, text="Forgot Pass",command=lambda: forgetAdmin(window,"admin"),width=10).grid(row=3, column=2, sticky='W')

    sep=ttk.Separator(wframe, orient=VERTICAL).pack(side=LEFT, fill=Y)

#Defining Faculty Login Frame
    teacherframe=Frame(wframe, width=250, height=200)
    teacherframe.config(highlightbackground="BLACK", highlightcolor="BLACK", highlightthickness=3)
    teacherframe.pack(side=LEFT,padx=25, pady=50)
    tlabel=Label(teacherframe, text="        Faculty Login        ")
    tlabel.config(font=('times',18))
    tlabel.grid(columnspan=2)
    tuser = Label(teacherframe, text="UserName:")
    tuser.grid(row=1, sticky=E)
    tpass = Label(teacherframe, text="Password:")
    tpass.grid(column=0, row=2, sticky=E)
    etuser = Entry(teacherframe,width=25)
    etuser.grid(row=1, column=1,columnspan=2)
    etpass = Entry(teacherframe, show="*",width=25)
    etpass.grid(row=2, column=1,columnspan=2)
    tbutton = Button(teacherframe, text="Login", command=lambda: faclogin(etuser, etpass),width=10)
    tbutton.grid(row=3, column=1, sticky='E')
    Button(teacherframe, text="Forgot Pass",width=10,command=lambda: forgetAdmin(window,"faculty")).grid(row=3,column=2,sticky='W')
    wframe.grid()
    window.mainloop()


def adminLogin():
    username = userEntry.get()
    pawd=passEntry.get()
    flag=getcredential(username,pawd)
    if flag is 1:
        window.destroy()
        Admin()
    else:
        tkMessageBox.showerror("Error", "Please Enter Correct Credential !")

#Faculty Login
def faclogin(etuser, etpass):
    facid,facname,facerror=facultylogin(etuser,etpass)
    if facerror is not "":
        tkMessageBox.showerror("Error", facerror)
        return
    else:
        window.destroy()
        faculty(facid,facname)

def out():
    Window()

Window()
