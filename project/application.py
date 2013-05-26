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

    def import_click(self):
        print "Importing..."
        self.start_processes()

    def clear_click(self):
        print "Clearing..."

    def start_processes(self):
        """
        """
        self.import_tags()
        self.get_tags()

    def import_tags(self):
        """
        Uses the treader to read tags from .mp3 files and the dbhelper to 
        insert them in the database. Runs in a separate process.

        """
        #Read tags from music folder 
        treader = tagreader.TagReader()
        datalist = treader.readtags("../../music/")
        print("Read %s tags." % len(datalist))

        #Write tags to database
        writer = dbhelper.DatabaseHelper()
        for entry in datalist:
            writer.write(entry)
        writer.close()
        print("Done writing tags to database.")

    def get_tags(self):
        """
        Uses the dbhelper to query the database for tags and then returns them 
        in a way that the GUI can use them. Runs in a separate process.
        
        """
        #Read tags from database
        reader = dbhelper.DatabaseHelper()
        rows = reader.read()
        
        #Display tags in GUI
        for row in rows:
            self.curRow += 1
            mytk.GridCell(self.mframe, self.curRow, 0, 3, row[3])
            mytk.GridCell(self.mframe, self.curRow, 1, 30, row[0])
            mytk.GridCell(self.mframe, self.curRow, 2, 20, row[1])
            mytk.GridCell(self.mframe, self.curRow, 3, 30, row[2])
            mytk.GridCell(self.mframe, self.curRow, 4, 7, row[4])     
        reader.close()
        print("Done reading tags from database.")

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
            height=600,
            width=1000
        )
        self.mframe.grid(row=1, column=0, columnspan=4)
        self.mframe.grid_propagate(0)
        
        #Main list labels
        mytk.GridLabel(self.mframe, 0, 3, '#')
        mytk.GridLabel(self.mframe, 1, 30, 'Title')
        mytk.GridLabel(self.mframe, 2, 20, 'Album')
        mytk.GridLabel(self.mframe, 3, 30, 'Artist')
        mytk.GridLabel(self.mframe, 4, 7, 'Length')
        self.curRow = 0

app = Application()
app.master.title('Treader')
app.mainloop()
