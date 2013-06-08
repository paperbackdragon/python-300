#Item grabbing function/closure generator
def takeitem(num):
    return lambda x: x[num]

#Word generator
def wordgen():
    with open("words") as wordlist:
        for line in wordlist:
            yield line

#Prints sorted list of words
print sorted(wordgen(), key=takeitem(1))

