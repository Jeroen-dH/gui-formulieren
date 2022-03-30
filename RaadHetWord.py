import tkinter
from tkinter import StringVar, ttk
from tkinter.messagebox import *
import sys
import os

gui= tkinter.Tk()
gui.geometry("600x300")
gui.configure(bg="gray")
gui.title("Raad het word!")
TempWoord = ""
Woord = []
score = 0
fout = 0
frame = tkinter.Frame(gui)
points = 0

errorlabel = tkinter.Label()
label = tkinter.Label(
    gui,
    text="Type hier een woord die de ander moet raden\n(mag maar 4-7 letters):",
    bg="#91A3B0",
    relief="solid"
)
label.pack(pady=30)
TempWoord = tkinter.Entry(gui,relief="solid",width=30)
TempWoord.pack(pady=.5,ipady=2)
confirmButton = tkinter.Button(
    gui,
    text="Confirm",
    bg="White",
    command=lambda: [PlayerOneDestroy()],
    activebackground="lightgreen"
)
confirmButton.pack(pady=10)

guesslabel = tkinter.Label(
    gui,
    text="Raad het woord!",
    bg="#91A3B0"
)
RaadButton = tkinter.Button(
    gui,
    text="Raad",
    bg="White",
    activebackground="lightgreen",
    command=lambda:[guessing()]
)

var1 = tkinter.StringVar(value="A")
list1 = []
for x in range(7):
    list1.append(StringVar) 
    
spinbox0 = tkinter.Spinbox(frame,textvariable=list1[x],wrap=True,width=2,justify ="center",state="readonly",values=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],bd=5)
spinbox1 = tkinter.Spinbox(frame,textvariable=list1[x],wrap=True,width=2,justify ="center",state="readonly",values=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],bd=5)
spinbox2 = tkinter.Spinbox(frame,textvariable=list1[x],wrap=True,width=2,justify ="center",state="readonly",values=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],bd=5)
spinbox3 = tkinter.Spinbox(frame,textvariable=list1[x],wrap=True,width=2,justify ="center",state="readonly",values=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],bd=5)
spinbox4 = tkinter.Spinbox(frame,textvariable=list1[x],wrap=True,width=2,justify ="center",state="readonly",values=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],bd=5)
spinbox5 = tkinter.Spinbox(frame,textvariable=list1[x],wrap=True,width=2,justify ="center",state="readonly",values=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],bd=5)
spinbox6 = tkinter.Spinbox(frame,textvariable=list1[x],wrap=True,width=2,justify ="center",state="readonly",values=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],bd=5)

def WoordGen():
    global Woord
    frame.pack(pady=50)
    if len(Woord) == 4:
        spinbox0.grid(row=1, column=0)
        spinbox1.grid(row=1, column=1)
        spinbox2.grid(row=1, column=2)
        spinbox3.grid(row=1, column=3)
    if len(Woord) == 5:
        spinbox0.grid(row=1, column=0)
        spinbox1.grid(row=1, column=1)
        spinbox2.grid(row=1, column=2)
        spinbox3.grid(row=1, column=3)
        spinbox4.grid(row=1, column=4)
    if len(Woord) == 6:
        spinbox0.grid(row=1, column=0)
        spinbox1.grid(row=1, column=1)
        spinbox2.grid(row=1, column=2)
        spinbox3.grid(row=1, column=3)
        spinbox4.grid(row=1, column=4)
        spinbox5.grid(row=1, column=5)
    if len(Woord) == 7:
        spinbox0.grid(row=1, column=0)
        spinbox1.grid(row=1, column=1)
        spinbox2.grid(row=1, column=2)
        spinbox3.grid(row=1, column=3)
        spinbox4.grid(row=1, column=4)
        spinbox5.grid(row=1, column=5)
        spinbox6.grid(row=1, column=6)
    return len(Woord)

def check():
    global TempWoord , Woord
    Woord = TempWoord.get()
    print(Woord)
    if len(Woord)<4 or len(Woord)>7:
        errorlabel.configure(text="4 tot 7 letters\n niet "+str(len(Woord))+" letters")
        errorlabel.pack()
        return False
    else:
        return True
    
def PlayerOneDestroy():
    global points
    confirm = check()
    if confirm == True:
        label.destroy()
        TempWoord.destroy()
        confirmButton.destroy()
        errorlabel.destroy()
        points = len(Woord)*6
        PlayerTwoLoad()
    elif confirm == False:
        print("try again.")
    
def PlayerTwoLoad():
    guesslabel.pack(pady=25)
    RaadButton.place(x= 285,y=180)
    WoordGen()    
letter1 = False
letter2 = False
letter3 = False
letter4 = False
letter5 = False
letter6 = False
letter7 = False
letters = [letter1,letter2,letter3,letter4,letter5,letter6,letter7]

def wrongs(fout):
    for x in range(len(Woord)):
        if letters[x] == False:
            fout += 1
    return fout

def pointsCheck():
    if points <= 0:
        popup = askyesno(title="Geen pogingen meer!",message="je hebt geen punten meer, Game over!\n Wil je nog een keer spelen?")
        if popup:
            print("check")
            gui.destroy()
            restart()
        else:
            gui.destroy

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def guessing():
    global points    
    tempspinboxen = [spinbox0.get(),spinbox1.get(),spinbox2.get(),spinbox3.get(),spinbox4.get(),spinbox5.get(),spinbox6.get()]
    for x in range(len(Woord)):
        if tempspinboxen[x] == Woord[x]:
            letters[x] = True
            print(letters[x])
        elif tempspinboxen[x] != Woord[x]:
            points-=2
            print(points)
        print(tempspinboxen[x])
        fouten = wrongs(0)
    if points <= 0:
        pointsCheck() 
        print("game over")
    else:
        if fouten == 0:
            popup = askyesno(title="Geraden!",message="Gefeliciteerd! je hebt het woord geraden!\nwil je nog een keer?")
            if popup:
                gui.destroy()
                restart()
            else:
                gui.destroy()
        elif fouten > 0:
            popup = showinfo(title="Guess", message="er zijn er "+str(fouten)+" fout\nJe hebt nu nog "+str(points)+" punten")
gui.mainloop()