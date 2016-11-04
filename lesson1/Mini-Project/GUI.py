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
def reisInfo2(Station2):

    ###Authenticatie (gebruikersnaam en wachtwoord) die gebruikt wordt voor het ophalen van de API###
    auth_details = ('mike.m.dejong@student.hu.nl', 'H4cctzd6FrJVd55syghnqpr9B3yCgb-GzIiXhuqZHI6J5fNR5zCwKQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=amsterdam'
    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)

    ###lege lijst waar de gegevens in worden gezet###
    gegevens2 = ''

    for vertrek in vertrekXML ['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:16]
        gegevens2 += str('Om '+vertrektijd+' vertrekt er een trein naar '+ eindbestemming + '\n')
    return gegevens2

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
    gegevens2 = reisInfo2(Station2)
    tekstvak = Text(toplevel, height=25, width=75, background='white',
                    font=('Helvetica', 12,), foreground='#01236a', borderwidth='5')
    tekstvak.insert(INSERT, gegevens2)
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


###Wat er gaat gebeuren nadat er op de knop is gedrukt voor het veranderen naar de taal: engels##
def clicked3():
    ###sluit root af ###
    root.deiconify()
    root.destroy()

    ###opent een nieuw scherm###
    engels = Tk()
    engels.title('NS startscreen')
    engels.iconbitmap('nsicon.ico')


    ###informatie ophalen van traject Utrecht in het engels###
    def reisInfo3(Station3):

            auth_details = ('mike.m.dejong@student.hu.nl', 'H4cctzd6FrJVd55syghnqpr9B3yCgb-GzIiXhuqZHI6J5fNR5zCwKQ')
            api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
            response = requests.get(api_url, auth=auth_details)
            vertrekXML = xmltodict.parse(response.text)
            gegevens3 = ''

            for vertrek in vertrekXML ['ActueleVertrekTijden']['VertrekkendeTrein']:
                eindbestemming = vertrek['EindBestemming']

                vertrektijd = vertrek['VertrekTijd']
                vertrektijd = vertrektijd[11:16]
                gegevens3 += str('At '+vertrektijd+' a train leaves to '+ eindbestemming + '\n')
            return gegevens3

    def tripinfoutrecht():
        station3 = 'Utrecht'
        toplevel = Toplevel(master=engels, background='#FECE22',width=794, height=600)
        toplevel.title('Tripinformation Utrecht')
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
        canvas.insert(canvas_id, 20, 'These are the departures of the trains from Amsterdam Centraal:\n')

        ###voegt tekstvak toe####
        gegevens3 = reisInfo3(station3)
        tekstvak = Text(toplevel, height=25, width=75, background='white',
                        font=('Helvetica', 12,), foreground='#01236a', borderwidth='5')
        tekstvak.insert(INSERT, gegevens3)
        tekstvak.place(x=10, y=40)

        ###scrollbar configuren###
        s.config(command=tekstvak.yview)
        tekstvak.config(yscrollcommand=s.set)

        ###scherm sluiten###
        def Close():
            toplevel.deiconify()
            toplevel.destroy()

        ###Knop om terug te keren naar het beginscherm####
        stopbutton = Button(master=toplevel, font=('Frutiger', 10, 'bold'), foreground='white', background='red',
                        text='Back to the\n startscreen', command=Close)
        stopbutton.place(x=640, y=540)

    ###informatie ophalen van traject Amsterdam in het engels###
    def reisInfo4(Station4):

        auth_details = ('mike.m.dejong@student.hu.nl', 'H4cctzd6FrJVd55syghnqpr9B3yCgb-GzIiXhuqZHI6J5fNR5zCwKQ')
        api_url = 'http://webservices.ns.nl/ns-api-avt?station=amsterdam'
        response = requests.get(api_url, auth=auth_details)
        vertrekXML = xmltodict.parse(response.text)
        gegevens4 = ''

        for vertrek in vertrekXML ['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = vertrek['EindBestemming']

            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]
            gegevens4 += str('At '+vertrektijd+' a train leaves to '+ eindbestemming + '\n')
        return gegevens4

    def tripinfouamsterdam():
        station4 = 'Utrecht'
        toplevel = Toplevel(master=engels, background='#FECE22',width=794, height=600)
        toplevel.title('Tripinformation Amsterdam')
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
        canvas.insert(canvas_id, 20, 'These are the departures of the trains from Amsterdam Centraal:\n')

        ###voegt tekstvak toe####
        gegevens4 = reisInfo4(station4)
        tekstvak = Text(toplevel, height=25, width=75, background='white',
                        font=('Helvetica', 12,), foreground='#01236a', borderwidth='5')
        tekstvak.insert(INSERT, gegevens4)
        tekstvak.place(x=10, y=40)

        ###scrollbar configuren###
        s.config(command=tekstvak.yview)
        tekstvak.config(yscrollcommand=s.set)

        ###scherm sluiten###
        def Close():
            toplevel.deiconify()
            toplevel.destroy()

        ###Knop om terug te keren naar het beginscherm####
        stopbutton = Button(master=toplevel, font=('Frutiger', 10, 'bold'), foreground='white', background='red',
                        text='Back to the\n startscreen', command=Close)
        stopbutton.place(x=640, y=540)

    ###Geeft verwijzing naar een PNG###
    beginschermengels = PhotoImage(file='beginscherm_engels.png')

    ###Maakt het scherm groter en geeft als achtergrond de PNG###
    label = Label(master=engels, image=beginschermengels)
    label.pack(expand=YES, fill=BOTH)

    ###Creëer een nieuwe button met tekst, kleur en font###
    button1 = Button(master=engels,
                 text='Tripinformation of station Utrecht',
                 background='#01236a',
                 foreground='white',
                 font=('Helvetica', 12, 'bold'), command=tripinfoutrecht)
    button1.place(x=120, y=400)

    ###Creëer een nieuwe button met tekst, kleur en font###
    button2 = Button(master=engels,
                 text='Tripinformation of station Amsterdam',
                 background='#01236a',
                 foreground='white',
                 font=('Helvetica', 12, 'bold'), command=tripinfouamsterdam)
    button2.place(x=410, y=400)

    ###Creëer een nieuwe button met een afbeelding###
    photo = PhotoImage(file='Nederland flag.png')
    button3 = Button(master=engels, width=33, height=21)
    button3.config(image=photo)
    tmi = photo.subsample(6,6)
    button3.config(image=tmi)
    button3.place(x=13, y=560)

    ###Creëer een nieuwe button met een afbeelding###
    photo = PhotoImage(file='UK.png')
    button3 = Button(master=engels, width=33, height=21)
    button3.config(image=photo)
    tmi2 = photo.subsample(7,7)
    button3.config(image=tmi2)
    button3.place(x=55, y=560)

    engels.mainloop()


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

###Creëer een nieuwe button met een afbeelding###
photo = PhotoImage(file='Nederland flag.png')
button3 = Button(master=root, width=33, height=21)
button3.config(image=photo)
tmi = photo.subsample(6,6)
button3.config(image=tmi)
button3.place(x=13, y=560)

###Creëer een nieuwe button met een afbeelding###
photo = PhotoImage(file='UK.png')
button3 = Button(master=root, width=33, height=21, command=clicked3)
button3.config(image=photo)
tmi2 = photo.subsample(7,7)
button3.config(image=tmi2)
button3.place(x=55, y=560)

root.mainloop()
