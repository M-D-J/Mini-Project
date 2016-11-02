###Dit is de GUI voor ons ns kaartautomaat systeem###
from tkinter import *
import requests
import xmltodict


###informatie ophalen van traject Utrecht###
def reisInfo(Station1):

        auth_details = ('mike.m.dejong@student.hu.nl', 'H4cctzd6FrJVd55syghnqpr9B3yCgb-GzIiXhuqZHI6J5fNR5zCwKQ')
        api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
        response = requests.get(api_url, auth=auth_details)
        vertrekXML = xmltodict.parse(response.text)
        gegevens = ''

        for vertrek in vertrekXML ['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = vertrek['EindBestemming']

            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]
            gegevens += str('Om '+vertrektijd+' vertrekt er een trein naar '+ eindbestemming + '\n')
        return gegevens


###informatie ophalen van traject Amsterdam###
def reisInfo(Station2):

    auth_details = ('mike.m.dejong@student.hu.nl', 'H4cctzd6FrJVd55syghnqpr9B3yCgb-GzIiXhuqZHI6J5fNR5zCwKQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=amsterdam'
    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)
    gegevens = ''

    for vertrek in vertrekXML ['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:16]
        gegevens += str('Om '+vertrektijd+' vertrekt er een trein naar '+ eindbestemming + '\n')
    return gegevens


###Wat er gaat gebeuren nadat er op de knop is gedrukt voor info over Utrecht###
def clicked1():

    ###Maakt nieuwe window met titel Reisinformatie Utrecht Centraal###
    Station1 = 'Utrecht'
    toplevel = Toplevel(root)
    toplevel.title('Reisinformatie Utrecht Centraal')
    toplevel.focus_set()
    toplevel.iconbitmap('nsicon.ico')

    ###Scrollbar toevoegen###
    s = Scrollbar(toplevel)
    s.pack(side=RIGHT, fill=Y)

    ###Voegt een achtergrond met kleur en tekst toe aan het scherm###
    canvas = Canvas(toplevel,bd=0, highlightthickness=0,
                    background='#FECE22',width=775, height=600)
    canvas.pack(fill=BOTH, expand=TRUE)                             ###zorgt dat gehele scherm gevuld wordt####
    canvas_id = canvas.create_text(10, 10, anchor='nw')
    canvas.itemconfig(canvas_id, font=('Helvetica', 16, 'bold'), fill='#01236a')
    canvas.insert(canvas_id, 20, 'Dit zijn de vertrektijden van de treinen vanuit Utrecht Centraal:\n')

    ###voegt tekstvak toe####
    gegevens = reisInfo(Station1)
    tekstvak = Text(toplevel, height=25, width=75, background='white',
                    font=('Helvetica', 12,), foreground='darkblue', borderwidth='5')
    tekstvak.insert(INSERT, gegevens)
    tekstvak.place(x=10, y=40)

    ###scrollbar configuren###
    s.config(command=tekstvak.yview)
    tekstvak.config(yscrollcommand=s.set)

    ###Geeft actie aan om de toplevel windows te sluiten###
    def Close():
        toplevel.deiconify()
        toplevel.destroy()

    ###Knop om terug te keren naar het beginscherm####
    stopbutton = Button(master=toplevel, font=('Frutiger', 10, 'bold'), foreground='white', background='red',
                        text='Terugkeren naar \nhet beginscherm', command=Close)
    stopbutton.place(x=640, y=540)

###Wat er gaat gebeuren nadat er op de knop is gedrukt voor info over Amsterdam##
def clicked2():
    Station2= 'Amsterdam'
    toplevel = Toplevel(master=root, background='#FECE22',width=794, height=600)
    toplevel.title('Reisinformatie Amsterdam')
    toplevel.focus_set()
    toplevel.iconbitmap('nsicon.ico')

    ###Scrollbar toevoegen###
    s = Scrollbar(toplevel)
    s.pack(side=RIGHT, fill=Y)

    ###Voegt een achtergrond met kleur en tekst toe aan het scherm###
    canvas = Canvas(toplevel,bd=0, highlightthickness=0,
                    background='#FECE22',width=775, height=600)
    canvas.pack(fill=BOTH, expand=TRUE)                             ###zorgt dat gehele scherm gevuld wordt####
    canvas_id = canvas.create_text(10, 10, anchor='nw')
    canvas.itemconfig(canvas_id, font=('Helvetica', 16, 'bold'), fill='#01236a')
    canvas.insert(canvas_id, 20, 'Dit zijn de vertrektijden van de treinen vanuit Amsterdam Centraal:\n')

    ###voegt tekstvak toe####
    gegevens = reisInfo(Station2)
    tekstvak = Text(toplevel, height=25, width=75, background='white',
                    font=('Helvetica', 12,), foreground='#01236a', borderwidth='5')
    tekstvak.insert(INSERT, gegevens)
    tekstvak.place(x=10, y=40)

    ###scrollbar configuren###
    s.config(command=tekstvak.yview)
    tekstvak.config(yscrollcommand=s.set)

    ###Geeft actie aan om de toplevel windows te sluiten###
    def Close():
        toplevel.deiconify()
        toplevel.destroy()

    ###Knop om terug te keren naar het beginscherm####
    stopbutton = Button(master=toplevel, font=('Frutiger', 10, 'bold'), foreground='white', background='red',
                        text='Terugkeren naar \nhet beginscherm', command=Close)
    stopbutton.place(x=640, y=540)

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
                 background='#01236a',
                 foreground='white',
                 font=('Helvetica', 12, 'bold'),
                 command=clicked1)
button1.place(x=120, y=400)


###Creëer een nieuwe button met tekst, kleur en font###
button2 = Button(master=root,
                 text='Reisinformatie station Amsterdam',
                 background='#01236a',
                 foreground='white',
                 font=('Helvetica', 12, 'bold'),
                 command=clicked2)
button2.place(x=410, y=400)


root.mainloop()
