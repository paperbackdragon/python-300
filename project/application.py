"""
Treader - A GUI-based MP3 Tag Reader
Author: Heather Hoaglund-Biron

"""
from multiprocessing import Process
import Tkinter
import dbhelper
import tagreader

class Application(Frame):
    def __init__(self, master=None):
        """
        Initializes required objects in the main application, including a 
        TagReader object and a DatabaseHelper object.

        """
        Frame.__init__(self, master)
        self.treader = TagReader()
        self.dbhelper = DatabaseHelper()

    def createWidgets(self):
        """
        Creates the widgets used in the application.

        """

    def importTags(self):
        """
        Uses the treader to read tags from .mp3 files and the dbhelper to 
        insert them in the database. Runs in a separate process.

        """

    def getTags(self):
        """
        Uses the dbhelper to query the database for tags and then returns them 
        in a way that the GUI can use them. Runs in a separate process.
        
        """

