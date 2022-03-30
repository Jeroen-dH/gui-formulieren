import tkinter as tk
from tkcalendar import Calendar
from tkinter import Button, Frame,StringVar
from datetime import datetime
from datetime import *

datum = ""
check = False
agecheck = 18
number = 0
GoOrNoGO = False

gui = tk.Tk()
gui.geometry("500x600")
gui.title("registratie formulier")
gui.configure(bg="white")
frame = Frame(gui, bg="gray",padx=5,pady=5,relief="solid",bd=.5)
frame.place(x=75,y=50)
x = datetime.today().date()


headLabel = tk.Label(
    gui,
    text="Registatieformulier",
    bg="#B2BEB5",
)


def checkpoint():
    naam = naamEntry.get()
    anaam = ANaamEntry.get()
    caldatum = cal.get_date()
    telefoon = telefoonNMREntry.get()
    emailresult = EmailEntry.get()
    datum2 = cal.get_date()
    if naam == "":
        wrong("\nnaam is niet ingevuld")
    if anaam == "":
        wrong("Achternaam is niet ingevuld")
    if number > -6574:
        wrong("Helaas je bent niet achtien")
    if len(telefoon) <= 9:
        wrong("telefoon nummer is niet ingevuld")
    if emailresult == "":
        wrong("Email is niet ingevoerd")
    else:
        frame.destroy()
        resultaat(naam,anaam,caldatum,telefoon,emailresult)
    
def resultaat(naam,anaam,caldatum,telefoon,emailresult):
    opslaanbtn.destroy()
    verstuurButton.place(y=500, x=220)
    resultaatlabel = tk.Label(gui,text="voornaam: "+naam+"\nAchternaam: "+anaam+"\nGeboorte datum: "+caldatum+"\nTelefoon nummer: "+ telefoon+"\nEmail: "+emailresult)
    resultaatlabel.place(x=170, y=75)


def wrong(printer) -> str:
    global GoOrNoGO
    print(printer)
    opslaanbtn.config(bg="red")
    gui.after(150,defaultcolor)
    GoOrNoGO = False

def right():
    global GoOrNoGO
    GoOrNoGO = True

        
        
def defaultcolor():
    opslaanbtn.config(bg="white")


cal = Calendar(gui,selectmode = 'day',year = x.year, month = x.month, day = x.day)
def GetCalander():
    global check, cal, datum, number
    if check == False:
        cal = Calendar(gui,selectmode = 'day',year = x.year, month = x.month, day = x.day)
        cal.place(x=.5,y=.5)
        check = True
    elif check:
        datelabel.config(text="Datum: "+cal.get_date(),padx=20)
        cal.destroy()
        check = False
        datum = datetime.strptime(cal.get_date(), '%m/%d/%y').date()
        difference = datum - x
        number = difference.days

#naam labels en entry's
naamLabel = tk.Label(
    frame,
    text="          Uw naam:         ", 
    padx=16,
    bd=.5,
    relief="solid"
).grid(row=0, column=0)
headLabel.pack(pady=29)

var1 = StringVar()
naamEntry = tk.Entry(
    frame,
    textvariable=StringVar,
)
naamEntry.grid(row=0,column=1)
ANaamLabel = tk.Label(
    frame,
    text="         Uw achternaam:         ",
    bd=.5,
    relief="solid"
).grid(row=1,column=0)
ANaamEntry = tk.Entry(
    frame,
    textvariable=var1
)
ANaamEntry.grid(column=1,row=1)

#geboorte datum vragen
GeboorteDate = tk.Label(
    frame,
    text="Wat is uw geboorte datum",
    bd=.5,
    relief="solid"
).grid(row=3, column=0)
datelabel = tk.Label(
    frame,
    text="Datum: ",
    padx=40

)

#telefoon nummer vragen
telefoonNMR = tk.Label(
    frame,
    text="   Uw telefoon nummer:     ",
    bd=.5,
    relief="solid"
)
telefoonNMR.grid(row=4,column=0)
telefoonNMREntry = tk.Entry(
    frame,
    textvariable=StringVar
)
telefoonNMREntry.grid(column=1,row=4)
#email adres
Email = tk.Label(
    frame,
    text="         Wat is uw email:         ",
    bd=.5,
    relief="solid"
)
Email.grid(row=5,column=0)

EmailEntry = tk.Entry(
    frame,
    textvariable=StringVar
)
EmailEntry.grid(row=5,column=1)


datelabel.grid(row=3,column=1)
calbutton = tk.Button(frame,text="cal",command=GetCalander)
calbutton.grid(row=3,column=2)

opslaanbtn = tk.Button(
    gui,
    text="Resultaat",
    command=lambda: [checkpoint()]
)
opslaanbtn.place(y=500,x=220)
verstuurButton = tk.Button(
    gui,
    text="versturen",
    command=lambda: [closewindow()]
)

def closewindow():
    gui.destroy()

gui.mainloop()