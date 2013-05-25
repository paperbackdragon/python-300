"""
Test class for TagReader

"""

import tagreader

def prettydict(dictlist):
    for entry in dictlist:
        for key, value in entry.items():
            print(key + ": " + value)
        print('\n')

if __name__ == '__main__':
    treader = tagreader.TagReader()
    datalist = treader.readtags("../../music/")
    prettydict(datalist)
