###Dit is de GUI voor ons ns kaartautomaat systeem###
from tkinter import *
import requests
import xmltodict
import NS
import NSAsmterdam
from tkinter.messagebox import showinfo


###Wat er gaat gebeuren nadat er op de knop is gedrukt voor info over Utrecht###
def clicked1():
    ###Maakt nieuwe window met een titel###
    toplevel = Toplevel(root)
    toplevel.title('Reisinformatie Utrecht')
    toplevel.focus_set()
    toplevel.iconbitmap('nsicon.ico')

    ###Voegt een vertikale scrollbar toe aan de rechterkant###
    vscrollbar = Scrollbar(toplevel,orient=VERTICAL)
    vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)

    ###Voegt de scrollbar toe aan het scherm en geeft een achtergrond met kleur en tekst###
    canvas = Canvas(toplevel,bd=0, highlightthickness=0,
                    yscrollcommand=vscrollbar.set,
                    background='#FECE22',width=775, height=600)
    canvas.pack(fill=BOTH, expand=TRUE)                             ###zorgt dat gehele scherm gevuld wordt####
    canvas_id = canvas.create_text(10, 10, anchor='nw')
    canvas.itemconfig(canvas_id, font=('Helvetica', 16, 'bold italic'), fill='darkblue')
    canvas.insert(canvas_id, 20, 'Dit zijn de vertrek tijden van de treinen in het traject Utrecht:\n')

    ###voegt tekstvak toe####
    tekstvak = Text(toplevel, height=25, width=75, background='darkblue',
                    font=('Helvetica', 12,), foreground='white')
    tekstvak.place(x=10, y=40)

###Wat er gaat gebeuren nadat er op de knop is gedrukt voor info over Amsterdam##
def clicked2():
    toplevel = Toplevel(master=root, background='#FECE22',width=794, height=600)
    toplevel.title('Reisinformatie Amsterdam')
    toplevel.focus_set()
    toplevel.iconbitmap('nsicon.ico')

    ###Voegt een vertikale scrollbar toe aan de rechterkant###
    vscrollbar = Scrollbar(toplevel,orient=VERTICAL)
    vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)

    ###Voegt de scrollbar toe aan het scherm en geeft een achtergrond met kleur en tekst###
    canvas = Canvas(toplevel,bd=0, highlightthickness=0,
                    yscrollcommand=vscrollbar.set,
                    background='#FECE22',width=775, height=600)
    canvas.pack(fill=BOTH, expand=TRUE)                             ###zorgt dat gehele scherm gevuld wordt####
    canvas_id = canvas.create_text(10, 10, anchor='nw')
    canvas.itemconfig(canvas_id, font=('Helvetica', 16, 'bold italic'), fill='darkblue')
    canvas.insert(canvas_id, 20, 'Dit zijn de vertrek tijden van de treinen in het traject Amsterdam:\n')

    ###voegt tekstvak toe####
    tekstvak = Text(toplevel, height=25, width=75, background='darkblue',
                    font=('Helvetica', 12,), foreground='white')
    tekstvak.place(x=10, y=40)

###Hoofdscherm###
root = Tk()
root.title('NS beginscherm')
root.iconbitmap('nsicon.ico')

beginscherm = PhotoImage(file="beginscherm.png")


label = Label(master=root, image=beginscherm)
label.pack(expand=YES, fill=BOTH)


###Creëer een nieuwe button met tekst, kleur en font###
button1 = Button(master=root,
                 text='Reisinformatie station Utrecht',
                 background='darkblue',
                 foreground='white',
                 font=('Helvetica', 12, 'bold italic'),
                 command=clicked1)
button1.place(x=120, y=400)


###Creëer een nieuwe button met tekst, kleur en font###
button2 = Button(master=root,
                 text='Reisinformatie station Amsterdam',
                 background='darkblue',
                 foreground='white',
                 font=('Helvetica', 12, 'bold italic'),
                 command=clicked2)
button2.place(x=410, y=400)


root.mainloop()
