import sqlite3
import tkMessageBox
from Tkinter import *
import ttk

import math


class HorizontalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        '''vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        vscrollbar.config(command=canvas.yview)'''
        #for horizontal
        xscrollbar = Scrollbar(self, orient=HORIZONTAL)
        xscrollbar.pack(fill=X, side=BOTTOM, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        xscrollcommand=xscrollbar.set)
        xscrollbar.config(command=canvas.xview)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width() and interior.winfo_reqheight() != canvas.winfo_height():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth(),height=interior.winfo_reqheight())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width() and interior.winfo_reqheight() != canvas.winfo_height():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width(), height=canvas.winfo_height())
        canvas.bind('<Configure>', _configure_canvas)

maxcount=20
def addReport(frame,attlist,page):
    #page=0
    count=page*maxcount
    mac=count+maxcount
    i=0
    r=1
    j=0
    for att in attlist:
       if count <= i < mac:
           j=0
           print att
           for tup in att:
                ttk.Label(frame.interior, text=tup, font=('times', 10)).grid(row=r, column=j)

                j=j+1
           r=r+1
       i = i + 1
       if i>mac:
           break
    if(i<mac):
        while(i<mac):

            for k in range(j):
                ttk.Label(frame.interior, text="                 ", font=('times', 10)).grid(row=r, column=k)
            r=r+1
            i=i+1



def getSr(name,batch):
    sno=name[3:]
    con=sqlite3.connect("Student.db")
    try:

        query = "select Srno from " + batch + " where sno= " + sno
        result = con.execute(query)
        for n in result:
            sr = n[0]
            y2 = sr % 10
            sr = sr / 10
            y1 = sr % 10
            sr = sr / 10
            srno = str(sr) + "/" + str(y1) + str(y2)
            con.close()
            return srno
    except Exception,e:
        tkMessageBox.showerror("Error", e)
        return

def createReport(reportwindow,eAsubjcode, eAbranch, eAsem,facultyId):
    try:
        year = int(math.ceil(float(eAsem.get()) / 2))
        con = sqlite3.connect("Student.db")
        batch = eAbranch.get() + str(year)
        subtable = eAsubjcode.get() + eAbranch.get() + str(eAsem.get())
        query="select FacultyID from subj where subjCode= '"+eAsubjcode.get()+"'"
        result=con.execute(query)
        for rs in result:
            if rs[0]is not facultyId:
                raise Exception("You are Not Authorised")
        query = "PRAGMA table_info(" + subtable + ")"
        result = con.execute(query)
        i = 0
        column = []

        for n in result:
            if (i > 1):
                column.append(getSr(n[1], batch))
            else:
                column.append(n[1])
            i = i + 1
        print column
        root = reportwindow
        frame = HorizontalScrolledFrame(root)
        j = 0
        # ttk.Style().configure("TLabel", padding=6, relief="groove")
        for col in column:
            ttk.Label(frame.interior, text=col, font=('times', 15), relief="groove").grid(row=0, column=j, sticky='W',
                                                                                          padx=2, pady=1)
            j = j + 1
        query = 'Select * from  ' + subtable
        result = con.execute(query)
        r = 1;
        attlist = []
        # ttk.Style().configure("TLabel", padding=6, relief="flat")
        for res in result:
            attlist.append(res)

        buttons = int(math.ceil(float(attlist.__len__() / float(maxcount))))
        frame.pack()
        print buttons
        for i in range(buttons):
            ttk.Button(root, text=i, command=lambda b=0 + i: addReport(frame, attlist, b), width=5).pack(side='left')
        # addReport(attlist,frame,0)
        con.close()
    except Exception,e:
        con.close()
        tkMessageBox.showerror("Error", e)