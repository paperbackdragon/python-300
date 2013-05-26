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
    #test getting tags
    treader = tagreader.TagReader()
    datalist = treader.readtags("../../music/")
    print("done reading tags")

    #test writing
    writer = dbhelper.DatabaseHelper()
    write_to_db(datalist, writer)
    writer.close()
    print("done writing to db")
    
    #test reading
    reader = dbhelper.DatabaseHelper()
    read_from_db(reader)
    reader.close()
    print("done reading to db")
