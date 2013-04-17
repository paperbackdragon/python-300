#! /usr/bin/bash -t
#
# Copyright 2013 Systems Deployment, LLC
# Author: Morris Bernstein (morris@systems-deployment.com)

import sys


def dump_node(node, depth=0):
    for _ in range(depth):
        sys.stderr.write("   +")
    sys.stderr.write(" %s\n" % node)
    if node.left:
        dump_node(node.left, depth + 1)
    if node.middle:
        dump_node(node.middle, depth + 1)
    if node.right:
        dump_node(node.right, depth + 1)


def dump_method(tree):
    if tree.root:
        tree.root.dump(0)
    else:
        print("Tree is empty.")


def dump(tree):
    if tree.root:
        dump_node(tree.root, 0)
    else:
        print("Tree is empty.")
