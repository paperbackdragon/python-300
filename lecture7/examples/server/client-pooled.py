#!/usr/bin/env python

import argparse
from multiprocessing.pool import ThreadPool
import os
import sys
import urllib2
import threading
import Queue

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from decorators.decorators import timer

@timer
def threading_client(number_of_requests=10, thread_count=2):
    
    results = Queue.Queue()
    url = "http://localhost:8080"

    def worker(*args):
        print "Thread %s started" % threading.current_thread().name
        conn = urllib2.urlopen(url)
        result = conn.read()
        conn.close()
        results.put(result)

    pool = ThreadPool(processes=thread_count)
    pool.map(worker, range(number_of_requests))

    for i in xrange(number_of_requests):
        print results.get(timeout=3)

if __name__ == "__main__":
    # TODO: get number_of_requests and thread_count from
    # argparse

    number_of_requests = 200
    thread_count = 5
    threading_client(number_of_requests=number_of_requests, thread_count = thread_count)
