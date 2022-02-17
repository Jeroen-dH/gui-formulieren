import re
import tkinter
from tkinter import ttk
from datetime import datetime
import datetime as dt
import calendar
from tkinter import messagebox
from tkinter.messagebox import *
from datetime import timedelta

gui = tkinter.Tk()
gui.title("DaysByDays")
gui.geometry("600x300")
gui.configure(bg="gray")

x = dt.date.today()
print(x)
var1 = tkinter.StringVar(value=x.strftime("%d"))
var2 = tkinter.StringVar(value=x.strftime("%B"))
var3 = tkinter.StringVar(value=x.year)
combobox1 = ttk.Combobox(gui, textvariable=var1,values=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"),state="readonly")   
combobox2 = ttk.Combobox(gui, textvariable=var2,values=("January", "February","March","April","May","June","July","August","September","Oktober","November","December"),state="readonly")
combobox3 = ttk.Combobox(gui, textvariable=var3,values=("2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030"),state="readonly")
combobox1.pack()
combobox2.pack()
combobox3.pack()
combobox1.place(rely=.5, relx=.100, anchor="w")
combobox2.place(rely=.5, relx=.50, anchor="center")
combobox3.place(rely=.5, relx=.9, anchor="e")

def calculate():
    day = int(var1.get())
    print(day)
    month = str(var2.get())
    print(month)
    year = int(var3.get())
    print(year)
    global number, textInfo
    dayPicked = int(day)
    monthPicked = month
    yearPicked = int(year)
    monthNumber = int(dt.datetime.strptime(monthPicked, "%B").month)
    print(dayPicked,monthNumber,yearPicked)
    today = x
    datePicked = dt.date(yearPicked, monthNumber, dayPicked)
    print(datePicked,today)
    difference = datePicked - today
    print(difference)
    number = difference.days
    if number > 0:
        if number == 1:
            textInfo = "This is " + str(number) + " day in the future"
        else:
            textInfo = "This is " + str(number) + " days in the future"
    elif number < 0:
        if -number == 1:
            textInfo = "This was " + str(-number) + " day ago"
        else:
            textInfo = "This was " + str(-number) + " days ago"
    else:
        textInfo = "This is today"

GoButton = tkinter.Button(
    gui,
    text="Go",
    bg="blue",
    fg="white",
    activebackground="lightgreen",
    command=lambda:[calculate(),showinfo(title="Je ma",message=textInfo)]
)
GoButton.pack()
GoButton.place(rely=.7 ,relx=.5 ,anchor="s")

gui.mainloop()