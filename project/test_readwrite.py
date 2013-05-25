"""
Test class for DatabaseHelper and TagReader together

"""

import dbhelper
import tagreader

def write_to_db(dictlist, helper):
    for entry in dictlist:
        helper.write(entry)

def read_from_db(helper):
    rows = helper.read()

    for row in rows:
        print row

if __name__ == '__main__':
    #test writing
    writer = dbhelper.DatabaseHelper()

    datalist = [{
        'title': "Song Title",
        'album': "This Is An Album",
        'artist': "Oc Topi",
        'track': "1",
        'length': "3:50"
        }]

    write_to_db(datalist, writer)
    writer.close()
    print("done writing")
    
    #test reading
    reader = dbhelper.DatabaseHelper()
    
    read_from_db(reader)

    reader.close()

    print("done reading")
