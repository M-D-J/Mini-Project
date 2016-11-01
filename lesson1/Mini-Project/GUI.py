# Dit is de GUI voor ons ns kaartautomaat systeem
import os
from tkinter import *


def clicked1():
    toplevel = Toplevel(master=root, background='#FECE22',width=794, height=600)
    toplevel.title('Reisinformatie Utrecht')
    toplevel.focus_set()
    os.system('NS.py')

def clicked2():
    toplevel = Toplevel(master=root, background='#FECE22',width=794, height=600)
    toplevel.title('Reisinformatie Amsterdam')
    toplevel.focus_set()
    os.system('NSAsmterdam.py')


root = Tk()
root.title('NS beginscherm')


beginscherm = PhotoImage(file="beginscherm.png")


label = Label(master=root, image=beginscherm)
label.pack()

button1 = Button(master=root,
                 text='Reisinformatie station Utrecht',
                 background='darkblue',
                 foreground='white',
                 font=('Helvetica', 12, 'bold italic'),
                 command=clicked1)
button1.place(x=120, y=400)


button2 = Button(master=root,
                 text='Reisinformatie station Amsterdam',
                 background='darkblue',
                 foreground='white',
                 font=('Helvetica', 12, 'bold italic'),
                 command=clicked2)
button2.place(x=410, y=400)


root.mainloop()
