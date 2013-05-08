#!/usr/bin/env python

class A(object):
    name = "A"
    def hello(self):
        return "%s says hello, A-style" % self.name

class B():
    name = "B"

class C():
    name = "C"
    def hello(self):
        return "%s says hello, C-style" % self.name

class D(C,B):
    name = "D"
    
if __name__ == "__main__":
    d = D()
    d2 = D()
    print d.hello()
    D.name = "Dee"
    print d.hello()
    print d2.hello()
