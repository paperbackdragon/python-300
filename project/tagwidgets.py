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
    def __init__(self, master, col, labeltext):
        tk.Label.__init__(self, master=master, text=labeltext)

        self.config(relief='groove', bg='white', width=16, anchor=tk.W)
        self.grid(row=0, column=col)
