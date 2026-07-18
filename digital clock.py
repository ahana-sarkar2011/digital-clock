from tkinter import *
from time import strftime

type = "24h"

def change_type():
    global type
    if type == "24h":
        type = "12h"
    else:
        type = "24h"
    print (type)

def new_time():
    global type
    if type == "24h":
        t = strftime("%H:%M:%S")
        time.config(text=t)
        time.after(1000,new_time)
        d = strftime("%d/%m/%y")
        date.config(text=d)
    else:
        t = strftime("%I:%M:%S %p")
    time.config(text=t)
    time.after(1000,new_time)
    d = strftime("%d/%m/%y")
    date.config(text=d)
    

root = Tk()
root.geometry("500x300")
root.config(background="pink")
root.title("Digital clock")

time = Label(root,font=("Arial",50))
time.grid(row=0,column=0)

date = Label(root,font=("Arial",30))
date.grid(row=1,column=0)

time_type = Button(root,text="change time type",font=("Arial",20),command=change_type)
time_type.grid(row=0,column=1)

new_time()

root.mainloop()