"""
Treader - A GUI-based MP3 Tag Reader
Author: Heather Hoaglund-Biron

"""
from multiprocessing import Process, Queue
import Tkinter as tk
import tagwidgets as mytk
import dbhelper
import tagreader
import os
import random
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        """
        Initializes required objects in the main application, including a 
        TagReader object and a DatabaseHelper object.

        """
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
        self.curRow = 0
        self.queue = Queue()
        self.gui_queue = Queue()

    def import_click(self):
        print "Importing..."
        self.start_time = time.time()
        self.start_processes()

    def clear_click(self):
        print "Clearing..."
        
        #Delete song database
        try:
            os.remove("tags.db")
        except OSError:
            print "Database already removed."

        #Remove text from screen
        children = [x for x in self.mframe.winfo_children() if isinstance(x, mytk.GridCell)]
        for child in children:
            child.destroy()
            self.curRow = 1

    def import_tags(self):
        """
        Uses the treader to read tags from .mp3 files and the dbhelper to 
        insert them in the database. Runs in a separate process.

        """
        #Read tags from music folder 
        treader = tagreader.TagReader()
        datalist = treader.readtags("../../../music/")
        print("Read %s tags." % len(datalist))

        #Write tags to database and alert other process after commit
        writer = dbhelper.DatabaseHelper()
        for entry in datalist:
            key = writer.write(entry)
            if key != {}:
                self.queue.put(key)
        writer.close()
        self.queue.put("done")
        print("Done writing tags to database.")

    def update_gui(self):
        while True:
            rows = self.gui_queue.get()
            if rows == "done":
                #We're done importing
                print time.time() - self.start_time
                break;
            else:
                #Display tags in GUI
                print "Displaying %s" % rows
                for row in rows:
                    self.curRow += 1
                    mytk.GridCell(self.mframe, self.curRow, 0, 3, row[3])
                    mytk.GridCell(self.mframe, self.curRow, 1, 30, row[0])
                    mytk.GridCell(self.mframe, self.curRow, 2, 20, row[1])
                    mytk.GridCell(self.mframe, self.curRow, 3, 30, row[2])
                    mytk.GridCell(self.mframe, self.curRow, 4, 7, row[4])     

    def get_tags(self):
        """
        Uses the dbhelper to query the database for tags and then returns them 
        in a way that the GUI can use them. Runs in a separate process.
        
        """
        reader = dbhelper.DatabaseHelper()

        #While still importing and new items haven't been displayed
        while True:
            key = self.queue.get()
            if key == "done":
                #We're done importing
                self.gui_queue.put(key)
                break;
            elif "title" in key and "album" in key:
                #Read tags from database
                rows = reader.read(key)
                self.gui_queue.put(rows)

        reader.close()
        print("Done reading tags from database.")

    def start_processes(self):
        """
        Initializes and starts the writing (import) and reading (getter) 
        processes.

        """
        #self.import_proc = Process(target=self.import_tags)
        #self.getter_proc = Process(target=self.get_tags)

        #self.import_proc.start()
        #self.getter_proc.start()

        self.import_tags()
        self.get_tags()

        self.update_gui()

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

app = Application()
app.master.title('Treader')
app.master.geometry('-200+40')
app.mainloop()
