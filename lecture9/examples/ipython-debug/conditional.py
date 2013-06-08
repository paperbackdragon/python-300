import random

def worker(x):
    print "entered worker"
    return x

def main(x):
    print "entered main"
    y = random.random()
    return worker(x+y)

if __name__ == "__main__":
    while True:
        main(random.random())
