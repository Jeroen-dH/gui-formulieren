import tkinter
from tkinter import ttk


gui= tkinter.Tk()
gui.geometry("600x300")
gui.configure(bg="gray")
gui.title("Raad het word!")
TempWoord = ""
Woord = ""
frame = tkinter.Frame(gui)


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
    activebackground="lightgreen",
    command= lambda: [PlayerOneDestroy(),PlayerTwoLoad()]
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
def PlayerOneDestroy():
    global TempWoord , Woord
    Woord = TempWoord.get()
    print(Woord)
    label.destroy()
    TempWoord.destroy()
    confirmButton.destroy()
def PlayerTwoLoad():
    guesslabel.pack(pady=25)
    WoordGen()


gui.mainloop()