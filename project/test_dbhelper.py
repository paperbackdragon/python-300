"""
Test class for DatabaseHelper

"""

import dbhelper

def write_to_db(dictlist, helper):
    for entry in dictlist:
        helper.write(entry)

if __name__ == '__main__':
    helper = dbhelper.DatabaseHelper()

    datalist = [{
        'title': "Song Title",
        'album': "This Is An Album",
        'artist': "Oc Topi",
        'track': "1",
        'length': "3:50"
        }]

    write_to_db(datalist, helper)
    helper.close()
    print("done")
