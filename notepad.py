from tkinter import *

import os

def newfile():
    print(filenameentry.get()+" has been created successfully")
    os.system("touch "+filenameentry.get())
    
    
    
def openfile():
    f = open(filenameentry.get(),"r")
    x = f.read()
    print("the file "+filenameentry.get()+" has been opened successfully")
    textbox.delete(0.0,END)
    textbox.insert(0.0,x)
    f.close()
def savefile():
    f = open(filenameentry.get(),"w+")
    x = textbox.get(0.0,END)
    f.write(x)
    print("the file"+filenameentry.get()+"has been saved successfully")
    


root = Tk()
root.minsize(width=400,height=400)

filenamelabel = Label(root,text="enter file name")
filenamelabel.grid()
filenameentry = Entry(root)
filenameentry.grid(row=0,column=1)

button1 = Button(root,text="Create a new file",command=newfile)
button1.grid(row=1,column=0)

button2 = Button(root,text="Open the file",command=openfile)
button2.grid(row=1,column=1)

button3 = Button(root,text="save the file",command=savefile)
button3.grid(row=1,column=2)
labeltext = Label(root,text="text editor below")
labeltext.grid()

textbox = Text(root,width=100,height=100)
textbox.grid(row=4)

root.mainloop()
