"""
MP3 Tag Reader
Author: Heather Hoaglund-Biron

"""
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from decimal import Decimal
import fnmatch
import os

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
        files = self._find(topdir)
        tags = self._read(files)
        return tags

    def _find(self, topdir):
        """
        Searches through the given music directory for .mp3 files and
        returns an array of filenames.

        """
        matches = []
        for root, dirnames, filenames in os.walk(topdir):
            for filename in fnmatch.filter(filenames, '*.mp3'):
                matches.append(os.path.join(root, filename))
        
        return matches
    
    def _formattime(self, time):
        """
        Given a floating point number in seconds, returns a string
        formatted as "MM:SS".

        """
        #Divide into minutes
        print time
        minutes = Decimal(time / 60).quantize(Decimal(".01"), rounding=ROUND_HALF_UP)
        return minutes


        #Split into minute string and second string


        #Concatenate

        #return

    def _read(self, musicfiles):
        """
        Reads the metadata from the given files and returns a list of 
        dictionaries cotaining the metadata for each file.

        """
        metadata = []
        for mp3 in musicfiles:
            filedict = {}
            musicfile = EasyID3(mp3)
            musicaudio = MP3(mp3)
            keys = ['title', 'artist', 'album', 'tracknumber']
            
            #Store each key, value pair in the file's dictionary
            for key in keys:
                try:
                    if key == 'tracknumber':
                        dictkey = 'track'
                    else:
                        dictkey = key
                    filedict[dictkey] = ', '.join(musicfile[key])
                except KeyError:
                    pass
            try:
                filedict['length'] = self._formattime(musicaudio.info.length)
            except KeyError:
                pass

            metadata.append(filedict)
        return metadata
    
