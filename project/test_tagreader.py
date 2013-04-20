"""
Test class for TagReader

"""

import tagreader

if __name__ == '__main__':
    treader = tagreader.TagReader()
    tag_dict = treader.readTags("../../music/")
    print(str(tag_dict))
