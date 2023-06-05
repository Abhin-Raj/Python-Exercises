from tkinter import *
a=Tk()
a.title("tkinter practices")
a.geometry("400x500")
a.resizable(True, True)
a.configure(background="skyblue")
l= Label(a,text="Welcome")

e= Entry(a)
l.pack() 

e.place(y=50,x=130) 

a.mainloop()