import tkinter
import time
import random
from tkinter import messagebox
from tkinter.messagebox import *
import os
import sys
temptimer = 0
timer=20
points = 0
a =False
list1 = ["druk op de w","druk op de a","druk op de s","druk op de d","druk op de spatiebalk","enkele klik","dubbele klik","driedubbele klik."]
list2 = ["<w>","<a>","<s>","<d>","<space>","<Button>","<Double-Button>","<Triple-Button>"]
var1 = random.randint(0,7)

gui = tkinter.Tk()
gui.geometry("550x600")
gui.title("FPSTrainer")
gui.configure(bg="gray")

def countdown():
    global timer, a
    if a == False:
        a = True
        destroyStartButton()
    elif timer == -1:
        Clickbutton.destroy()
        popup()      
    elif timer > -1:
        timer = timer
        timerlabel.config(text=int(timer))
        timer = timer - 1
        gui.after(1000, countdown)
      
def destroyStartButton():
    startButton.destroy()
    countdown()
def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def popup():
    info = askyesno(title= "Time's up", message="Je tijd is om en je hebt "+str(points)+ " punten gehaald\nWil je nog een keer spelen?")
    if info:
        restart()
    else:
        gui.destroy()

def addpoints(e):
    global points,var1
    gui.unbind(list2[var1],funcid=None)
    var1 = random.randint(0,7)
    points += 1
    pointslabel.config(text="Points: "+str(points))
    gui.bind(list2[var1],addpoints)
    Clickbutton.configure(
        text=(list1[var1])
    )       
    Clickbutton.pack()
    randompos()

def bindfunction():
    gui.bind(list2[var1],addpoints)
def unbind():
    gui.unbind(list2[var1],addpoints)
def randompos():
    Clickbutton.pack(
        padx=random.randint(0,250),
        pady=random.randint(25,300)
    )

def Destroyconfirm():
    global timer, temptimer
    timer = (temptimer.get())
    if timer == "":
        timer = 20
    elif timer > "0":
        timer = int(temptimer.get())
    confirmbutton.destroy()
    timerquestion.destroy()
    temptimer.destroy()
    
Clickbutton = tkinter.Label(
    gui,
    text=(list1[var1]),
    padx= 20,
    pady= 20    
)

def randombutton():
    Clickbutton.configure(
        text=(list1[var1])
    )       
    Clickbutton.pack()    
    
    
timerquestion = tkinter.Label(
    gui,
    text="Hoelang wil je over de fpstrainer doen?\n(als je niks intyped is het automatisch 20)",
    padx=15,
    pady=15
)
temptimer = tkinter.Entry(gui)
timerquestion.pack(pady=50)
temptimer.pack(pady=10)

timerlabel = tkinter.Label(
    gui,
    text="(Timer)",
    relief="solid",
    padx="125",
    bg="black",
    fg="White"
)
timerlabel.place(anchor="nw")

pointslabel = tkinter.Label(
    gui,
    text="Points: "+ str(points),
    relief="solid",
    padx="125",
    bg="black",
    fg="white",
)
pointslabel.place(x=260)
    
startButton = tkinter.Button(
    gui,
    text="Click to start",
    command=lambda:[randombutton(), countdown(),bindfunction()]
)
def placestartbutton():
    startButton.place(relx=.5, rely=.5, anchor="center")

confirmbutton = tkinter.Button(
    gui,
    text="Confirm time",
    command=lambda: [placestartbutton(),Destroyconfirm()]
)
confirmbutton.pack()

gui.mainloop()