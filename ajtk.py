from tkinter import *
a=Tk()
a.title("tkinter practices")
a.geometry("400x900")
a.resizable(True, True)
a.configure(background="skyblue")

# l.place(x=20,y=30)

l= Label(a,text="Welcome")
e= Entry(a) 
e.pack() 

def dis():

    display = Label(a,text="abin")
    display.pack() 
    abc = Label(a,text=e.get())
    abc.pack()

btn=Button(a,text="print", command=dis)
btn.pack()


b=Button(a,text="click")

l.pack(pady=80)
# e.pack(pady=40)
b.pack(padx=20,pady=60)

a.mainloop()