import tkinter
from tkinter import ttk


gui= tkinter.Tk()
gui.geometry("600x300")
gui.configure(bg="gray")
gui.title("Raad het word!")
TempWoord = ""
Woord = []
frame = tkinter.Frame(gui)


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

var1 = tkinter.StringVar(value="A")

def WoordGen():
    frame.pack(pady=50)
    for x in range(len(Woord)):
        spinbox = ttk.Spinbox(frame,
            textvariable=var1,
            wrap=True,
            width=2,
            justify ="center",
            state="readonly",
            values=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
        spinbox.grid(row=1, column=x)

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
    confirm = check()
    if confirm == True:
        label.destroy()
        TempWoord.destroy()
        confirmButton.destroy()
        errorlabel.destroy()
        PlayerTwoLoad()
    elif confirm == False:
        print("hoi")
    
def PlayerTwoLoad():
    guesslabel.pack(pady=25)
    WoordGen()    

gui.mainloop()