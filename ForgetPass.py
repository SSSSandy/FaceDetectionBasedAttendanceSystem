import ttk
from Tkinter import *
import sqlite3
import tkMessageBox

def resetAdmin(tablename,eadminusername, eadminhint, topwindow,eadminPass,eadminPass2):
    try:
        if eadminPass.get() != eadminPass2.get() :
            raise Exception("Both password are not same !!!")
        con=sqlite3.connect("Student.db")
        if tablename is "admin":
            query="select adminID from "+tablename+" where username=? and hint=?"
        else:
            query = "select ID from " + tablename + " where username=? and hint=?"
        cursor=con.execute(query,(eadminusername.get(), eadminhint.get()))
        cursor_blank=0
        for n in cursor:
            sn=n
            cursor_blank=1
        if cursor_blank is 0:
            tkMessageBox.showerror("Error", "Invalid UserID or Hint")
            return
        if tablename is "admin":
            query="update "+tablename+" set pass=? where adminID= ?"
        else:
            query = "update " + tablename + " set pass=? where ID= ?"
        con.execute(query,(eadminPass.get(),sn[0]))
        con.commit()
        con.close()
        tkMessageBox.showinfo("Done", "Password Changed!!!!!")
        topwindow.destroy()
    except Exception, e:
        tkMessageBox.showerror("Error", e)
        topwindow.destroy()
        return




def forgetAdmin(window,tablename):
    topwindow=Toplevel(window)
    topwindow.title("Reset Password")
    frame1=ttk.Frame(topwindow)
    ttk.Label(frame1, text="Username").grid(row=0,column=0,padx=5,pady=5, sticky='E')
    ttk.Label(frame1, text="Password Hint").grid(row=1,padx=5,pady=5, sticky='E')
    ttk.Label(frame1, text="Password").grid(row=2, padx=5, pady=5, sticky='E')
    ttk.Label(frame1, text="Re-Type Password").grid(row=3, padx=5, pady=5, sticky='E')
    eadminusername=ttk.Entry(frame1,width=25)
    eadminhint = ttk.Entry(frame1, width=25)
    eadminPass=ttk.Entry(frame1,width=25, show="*")
    eadminPass2 = ttk.Entry(frame1, width=25)
    eadminusername.grid(row=0, column=1,columnspan=2,padx=5,pady=5)
    eadminhint.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
    eadminPass.grid(row=2, column=1,columnspan=2,padx=5,pady=5)
    eadminPass2.grid(row=3, column=1,columnspan=2,padx=5,pady=5)
    ttk.Button(frame1, text="Submit", command=lambda: resetAdmin(tablename,eadminusername,eadminhint,topwindow,eadminPass,eadminPass2)).grid(row=4,column=2)
    frame1.pack()
