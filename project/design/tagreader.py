"""
MP3 Tag Reader
Author: Heather Hoaglund-Biron

"""
from mutagen.easyid3 import EasyID3

class TagReader:
    """
    A TagReader reads metadata from .mp3 files and returns it in a list 
    of dictionaries. The only method used outside this file will be readtags().
    
    """

    def readtags(self, topdir):
        """
        Searches through the given directory for .mp3 files, reads the
        files' metadata, and returns it in a list of dictionaries.

        """

    def _find(self, topdir):
        """
        Searches through the given music directory for .mp3 files and
        returns an array of filenames.

        """

    def _read(self, musicfiles):
        """
        Reads the metadata from the given files and returns a list of 
        dictionaries cotaining the metadata for each file.

        """
    
