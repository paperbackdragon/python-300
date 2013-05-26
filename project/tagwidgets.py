"""
Tkinter widgets for use in the Treader application
Author: Heather Hoaglund-Biron

"""
import Tkinter as tk

class MainButton(tk.Button):
    def __init__(self, master, col, btext, bcommand):
        tk.Button.__init__(self, master=master, text=btext, command=bcommand)
        
        self.config(width=6) 
        self.grid(row=0, column=col, sticky=tk.N+tk.E+tk.S+tk.W)

class GridLabel(tk.Label):
    def __init__(self, master, col, size, labeltext):
        tk.Label.__init__(self, master=master, text=labeltext)

        self.config(
            relief='flat',
            bg='white',
            width=size,
            anchor=tk.W,
            font=('Helvetica', '10')
        )
        self.grid(row=0, column=col, sticky=tk.W)

class GridCell(tk.Label):
    def __init__(self, master, row, col, size, labeltext):
        tk.Label.__init__(self, master=master, text=labeltext)

        self.config(
            relief='flat',
            bg='white',
            width=size,
            anchor=tk.W,
            font=('Helvetica', '6')
        )
        self.grid(row=row, column=col, sticky=tk.W+tk.E)

