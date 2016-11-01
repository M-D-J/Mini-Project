# Dit is de GUI voor ons ns kaartautomaat systeem
from tkinter import *

def clicked1():
    toplevel = Toplevel(master=root, background='#FECE22',width=794, height=600)
    toplevel.title('Reisinformatie Utrecht')
    toplevel.focus_set()

def clicked2():
    toplevel = Toplevel()
    toplevel.title('Reisinformatie Amsterdam')
    toplevel.focus_set()

root = Tk()

beginscherm = PhotoImage(file="beginscherm.png")
achtergrondscherm = PhotoImage(file="achtergrond.png")


label = Label(master=root, image=beginscherm)
label.pack()

button1 = Button(master=root,
                 text='Reisinformatie station Utrecht',
                 background='blue',
                 foreground='white',
                 font=('Helvetica', 12, 'bold italic'),
                 command=clicked1)
button1.place(x=150, y=400)


button2 = Button(master=root,
                 text='Reisinformatie station Amsterdam',
                 background='blue',
                 foreground='white',
                 font=('Helvetica', 12, 'bold italic'),
                 command=clicked2)
button2.place(x=410, y=400)


root.mainloop()
