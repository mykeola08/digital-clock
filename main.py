from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Mykeola's Clock")


def time():
    string = strftime('%H:%M:%S %p')
    #For printing the date in human readable format
    #('%A, %B %d, %Y)
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=('ds-digital', 80), background='black', foreground='cyan')
label.pack(anchor='center')
time()

mainloop()