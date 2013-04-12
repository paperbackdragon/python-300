def depth(f):
    def wrapped(data):
        print("entering function")
        f(data)
        print("leaving function")
    return wrapped
    