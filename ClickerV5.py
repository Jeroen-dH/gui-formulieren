import argparse
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import *


clickcounter = 0
update = ""
gui = tkinter.Tk()
gui. geometry("400x500")
gui.title("Clicker V4")
gui.configure(
    bg="gray"
)
def hover(event):
    gui.configure(bg="yellow")

def hoverLeave(e):
    colorchanger()

def colorchanger():
    if clickcounter < 0:
        gui.configure(bg="red")
    elif clickcounter > 0:
        gui.configure(bg="#00DC00")
    else:
        gui.configure(bg="gray")

def counterchanger(e):
    global update, clickcounter
    if update == 'up':
        clickcounter *= 3
    elif update == 'down':
        clickcounter /=3
    counter.config(text= clickcounter)
    


def UpEnDownCounter(amount):
    global clickcounter
    clickcounter += amount
    counter.config(text=clickcounter)
    counter.pack()
    gui.after(10, colorchanger)
        
# de up button

def up():
    global update
    update='up'
    UpEnDownCounter(1)

def up2(e):
    global update
    update='up'
    UpEnDownCounter(1)
    
button1 = tkinter.Button(gui, font=("arial", 20, "bold"), command= up, activebackground="#00DC00")
button1.configure(
    text="Up",
    bg=("#00DC00"),
    padx= 30
)
button1.pack(
    pady= 30
)

# de counter in het midden     

counter = tkinter.Label(
    gui,
    text=clickcounter,
    padx=80,
    pady=30,
    font=("arial", 30, "bold"),
    borderwidth=2,
    relief="solid"
)
counter.pack()

# Checkbox
var1 = tkinter.IntVar()
def autoclicker():
    global update,clickcounter
    while (var1.get()) == 1:
        if update == "up":
            clickcounter += 1
            counter.config(text=clickcounter)
            colorchanger()
        elif update == "down":
            clickcounter -= 1
            counter.config(text=clickcounter)
            colorchanger()


checkbox = ttk.Checkbutton(
    gui,
    text="Autoclicker",
    variable= var1,
    command=autoclicker,
    onvalue=1,
    offvalue=0
)
checkbox.pack()
# de Down button
def down():
    global update
    update='down'
    UpEnDownCounter(-1)

def down2(e):
    global update
    update='down'
    UpEnDownCounter(-1)
    
button2 = tkinter.Button(
    gui,
    text="down",
    font=("arial", 30, "bold"),
    command= down,
    bg="red",
    activebackground="red",
)
button2.pack(
    pady=30
)
button2.bind("<Enter>",hover)
button2.bind("<Leave>",hoverLeave)
button1.bind("<Enter>",hover)
button1.bind("<Leave>",hoverLeave)
counter.bind('<Double-Button>', counterchanger)
gui.bind('<Up>', up2)
gui.bind('<Down>', down2)
gui.bind('<space>', counterchanger)
gui.bind('<+>', up2)
gui.bind('-', down2)

gui.mainloop()