#! /usr/bin/python
#
# Copyright 2013 Systems Deployment, LLC
# Author: Morris Bernstein (morris@systems-deployment.com)

import sys
import mydecorators

class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.count = 1
        self.left = left
        self.right = right

    @mydecorators.depth_1
    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        else:
            self.count += 1

    @mydecorators.depth_1
    def inorder(self, fn):
        if self.left:
            self.left.inorder(fn)
        fn(self)
        if self.right:
            self.right.inorder(fn)


class Tree(object):

    def __init__(self, rebalance=True):
        self.root = None
        self.rebalance = rebalance

    def insert(self, data):
        if not self.root:
            self.root = Node(data, None, None)
        else:
            self.root.insert(data)

    def inorder(self, fn):
        if self.root:
            self.root.inorder(fn)


def print_data(node):
    print node.count, node.data


def run(input):
    tree = Tree()
    for word in input:
        if word.endswith("\n"):
            word = word[:-1]
        tree.insert(word)
    tree.inorder(print_data)


if __name__ == "__main__":
    run(sys.stdin)
