from tkinter import *
import math


def calculate_squared():
    grondtal = int(entry.get())
    kwadraat = grondtal ** 2
    label['text'] = 'Kwadraat: van {} = {}'.format(grondtal, kwadraat)


def calculate_root():
    grondtal = int(entry.get())
    wortel = math.sqrt(grondtal)
    label['text'] = 'Wortel: van {} = {}'.format(grondtal, wortel)


root = Tk()

label = Label(master=root, text='Voer een getal in', height=2)
label.pack()

button_squared = Button(master=root, text='Naar kwadraat', command=calculate_squared)
button_squared.pack(pady=10)

button_root = Button(master=root, text='Naar wortel', command=calculate_root)
button_root.pack(pady=10)

entry = Entry(master=root)
entry.pack(padx=10, pady=10)

root.mainloop()
