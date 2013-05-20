"""
Treader - A GUI-based MP3 Tag Reader
Author: Heather Hoaglund-Biron

"""
from multiprocessing import Process
import Tkinter as tk
import tagwidgets as mytk
import dbhelper
import tagreader

class Application(tk.Frame):
    def __init__(self, master=None):
        """
        Initializes required objects in the main application, including a 
        TagReader object and a DatabaseHelper object.

        """
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.treader = tagreader.TagReader()
        self.dbhelper = dbhelper.DatabaseHelper()

    def create_widgets(self):
        """
        Creates the widgets used in the application.

        """
        #Menu buttons
        mytk.MainButton(self, 0, 'Import', self.import_click)
        mytk.MainButton(self, 1, 'Clear', self.clear_click)
        mytk.MainButton(self, 2, 'Quit', self.quit)
        self.spacer = tk.Label(self, text='', width='40')
        self.spacer.grid(row=0, column=3)
        
        #Main frame
        self.mframe = tk.Frame(
            self,
            bg='white',
            height=400,
            width=600
        )
        self.mframe.grid(row=1, column=0, columnspan=4)
        self.mframe.grid_propagate(0)
        
        #Main list labels
        mytk.GridLabel(self.mframe, 0, 'Track')
        mytk.GridLabel(self.mframe, 1, 'Album')
        mytk.GridLabel(self.mframe, 2, 'Title')
        mytk.GridLabel(self.mframe, 3, 'Length')

    def import_click(self):
        print "Importing..."

    def clear_click(self):
        print "Clearing..."

    def import_tags(self):
        """
        Uses the treader to read tags from .mp3 files and the dbhelper to 
        insert them in the database. Runs in a separate process.

        """

    def get_tags(self):
        """
        Uses the dbhelper to query the database for tags and then returns them 
        in a way that the GUI can use them. Runs in a separate process.
        
        """

app = Application()
app.master.title('Treader')
app.mainloop()
