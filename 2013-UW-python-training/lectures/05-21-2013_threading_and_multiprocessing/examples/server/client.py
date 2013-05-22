#!/usr/bin/env python

import argparse
import os
import sys
import urllib2
import threading
import Queue

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from decorators.decorators import timer

@timer
def threading_client(number_of_requests=10):
    
    results = Queue.Queue()
    url = "http://localhost:8080"

    def worker(*args):
        conn = urllib2.urlopen(url)
        result = conn.read()
        conn.close()
        results.put(result)


    for i in xrange(number_of_requests):
        thread = threading.Thread(target=worker, args=())
        thread.start()
        print "Thread %s started" % thread.name

    for i in xrange(number_of_requests):
        print results.get()

if __name__ == "__main__":

    number_of_requests = 800
    threading_client(number_of_requests=number_of_requests)
