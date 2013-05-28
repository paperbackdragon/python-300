"""
Database Helper
Author: Heather Hoaglund-Biron

"""
import sqlite3

class DatabaseHelper:
    """
    A DatabaseHelper reads and writes MP3 metadata to an SQLite database. It is
    necessary to close the connection to the database when finished with the
    close() method.

    """

    def __init__(self):
        """
        Initializes the MP3 metadata database.

        """
        self.conn = sqlite3.connect('tags.db')
        self.c = self.conn.cursor()
        
        #Create table
        self.c.execute("""CREATE TABLE IF NOT EXISTS songs
                          (title TEXT NOT NULL,
                           album TEXT NOT NULL,
                           artist TEXT,
                           track INTEGER,
                           length TEXT,
                           PRIMARY KEY (title, album))""")
        
        #Commit changes
        self.conn.commit()

    def write(self, data):
        """
        Takes the given song and writes it to the database, returning the
        primary key. Song title and album name are required.

        """
        insert_text = "INSERT into songs (title, album"
        columns = ['title', 'album', 'artist', 'track', 'length']
        used = ['title', 'album']
        primary_key = {}
        
        #See which tags are in the dictionary (title and album aren't optional)
        for column in columns[2:]:
            if column in data:
                insert_text += ", " + column
                used.append(column)
        insert_text += ") values ("

        #Prepare values
        values = []
        for column in used:
            if column == "track":
                values.append(data[column])
            else:
                values.append("\"" + data[column] + "\"")
            if column == "title" or column == "album":
                primary_key[column] = data[column]
        insert_text += ", ".join(values)
        insert_text += ")"

        #Execute command(s) and commit
        try:
            self.c.execute(insert_text)
            self.conn.commit()
            print "Writing tag: %s" % data
        except sqlite3.IntegrityError:
            primary_key = {}
            print "Item already exists in database."

        return primary_key

    def read(self, key):
        """
        Reads the information given in the query, grabs the specified data from 
        the database, and returns it.

        """
        select_text = "SELECT * from songs WHERE title is \"%s\" AND album is "\
            "\"%s\" ORDER BY artist, album, track" % (key["title"], key["album"])
        
        self.c.execute(select_text)

        rows = []
        for row in self.c.fetchall():
            rows.append(row)

        print "Reading tag: %s" % rows
        return rows

    def close(self):
        self.conn.close()

