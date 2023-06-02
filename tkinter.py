from tkinter import *

a=Tk()

a.geometry('400x400')
a.resizable(False,True)
a.configure(background="red")

l=Label(a,text="Hi")
s=Label(a,text="go")
l.pack()
s.pack()

e= Entry(a)
e.pack()
a.mainloop()