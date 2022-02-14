import tkinter
gui = tkinter.Tk()
gui.geometry("900x900")
gui.title("Dambord")
gui.configure(bg="gray")
frame = tkinter.Frame(gui)
temp = ""
a = 0

for x in range(10):
    if a == 0:
        a = 1
    else:
        a = 0
    for y in range(10):
        if a == 1:
            temp = "white"
            a = 0
        elif a == 0:
            temp = "black"
            a = 1 
        blokje = tkinter.Label(
            frame,
            bg= temp,
            padx=30,
            pady=20
        ).grid(row=y, column=x)

frame.pack(expand=True)
gui.mainloop()