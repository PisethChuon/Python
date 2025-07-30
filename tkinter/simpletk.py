from tkinter import *
from tkinter import ttk
root = Tk()

root.geometry('500x300')
frm = ttk.Frame(root)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.quit).grid(column=1, row=0)
root.mainloop()