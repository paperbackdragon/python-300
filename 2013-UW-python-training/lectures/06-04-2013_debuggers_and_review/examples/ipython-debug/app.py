import random

def worker(x):
    print "entered worker"
    1/0
    return x

def main(x):
    print "entered main"
    y = random.random()
    return worker(x+y)

if __name__ == "__main__":
    print main(random.random())
