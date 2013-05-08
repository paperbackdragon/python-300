#!/usr/bin/env python

import urllib2

from decorators import exception_handler, logger, timer

@timer
@exception_handler
def wx_report():
    print "Collecting data"
    url = "hxxp://www.atmos.washington.edu/data/city_report.html"
    reader = urllib2.urlopen(url)
    data = reader.read()
    print data

@logger
@exception_handler
def add(x,y):
    print x + y

if __name__ == "__main__":
    wx_report()
    add(None,2)
