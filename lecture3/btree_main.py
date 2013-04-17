#! /usr/bin/python -t
#
# Copyright 2013 Systems Deployment, LLC
# Author: Morris Bernstein (morris@systems-deployment.com)

import sys

import btree
import btree_dump


def run(input=sys.stdin):
    tree = btree.BTree()
    maker = None
    #maker = btree.DotMaker(tree, "out/frame-")

    for line in input:
        #sys.stderr.write("#### inserting %s\n" % line[:-1])
        tree.insert(btree.WordCounter(line[:-1]), maker).increment()
        if tree.verify() == False:
            sys.stderr.write("**** tree is no longer BTree\n")
        #maker.make_frame();
        btree_dump.dump(tree)
    #sys.stdout.write("#### final output\n")
    tree.walk(btree.print_counter)


def main():
    input = sys.stdin
    try:
        input_name = sys.argv[1]
        input = open(input_name)
    except IndexError:
        pass
    run(input)


if __name__ == "__main__":
    main()
