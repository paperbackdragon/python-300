#! /usr/bin/python -t
#
# Copyright 2013 Systems Deployment, LLC
# Author: Morris Bernstein (morris@systems-deployment.com)

import collections
import sys


class BTree(object):

    class Node(object):
        def __init__(self, data):
            self.data1 = data
            self.data2 = None
            self.left = None
            self.middle = None
            self.right = None
            self.hilite = False

        def __repr__(self):
            return "%s(%#08x)" % (self.__class__.__name__, id(self))

        # mainly for debugging
        def __str__(self):
            return ("<Node %s: <%s> %s <%s> %s <%s>>" %
                    (repr(self),
                     repr(self.left),
                     self.data1,
                     repr(self.middle),
                     self.data2,
                     repr(self.right)))

        def _isleaf(self):
            # Leaf nodes have no children so we just have to check for
            # a left child.
            return self.left is None

        def height(self, initial=0):
            if self._isleaf():
                return initial
            return self.left.height(initial + 1)

        def verify(self):
            if self._isleaf():
                return 1
            left_height = self.left.verify()
            middle_height = self.middle.verify()
            if middle_height != left_height:
                return False
            if self.right:
                right_height = self.right.verify()
                if right_height != left_height:
                    return False
            return left_height

        def _insert_leaf(self, data, maker=None):
            #sys.stderr.write("    _insert_leaf before: %s\n" % self)
            if self.data2 is None:
                # It fits, so figure out where to put it
                if data < self.data1:
                    self.data2 = self.data1
                    self.data1 = data
                elif self.data1 < data:
                    self.data2 = data
                else:
                    # Data compares equal: return original object.
                    data = self.data1
                new_parent = None
                self.hilite = True
                if maker:
                    maker.make_frame()
            else:
                # Split leaf node (unless it's a duplicate).
                #sys.stderr.write("    __insert_leaf: splitting node\n")
                if data < self.data1:
                    new_parent = BTree.Node(self.data1)
                    new_sibling = BTree.Node(self.data2)
                    self.data1 = data
                    self.data2 = None
                    new_parent.left = self
                    new_parent.middle = new_sibling
                    #sys.stderr.write("    _insert_leaf new_sibling: %s\n" % new_sibling)
                elif self.data1 < data and data < self.data2:
                    new_parent = BTree.Node(data)
                    new_sibling = BTree.Node(self.data2)
                    self.data2 = None
                    new_parent.left = self
                    new_parent.middle = new_sibling
                    #sys.stderr.write("    _insert_leaf new_sibling: %s\n" % new_sibling)
                elif self.data2 < data:
                    new_parent = BTree.Node(self.data2)
                    new_sibling = BTree.Node(data)
                    self.data2 = None
                    new_parent.left = self
                    new_parent.middle = new_sibling
                    #sys.stderr.write("    _insert_leaf new_sibling: %s\n" % new_sibling)
                elif data < self.data2:
                    new_parent = None
                    data = self.data1
                else:
                    new_parent = None
                    data = self.data2
                if new_parent:
                    new_parent.hilite = True
                    new_parent.left.hilite = True
                    new_parent.middle.hilite = True
                else:
                    self.hilite = True
                    if maker:
                        maker.make_frame()
            #sys.stderr.write("    _insert_leaf new_parent: %s\n" % new_parent)
            #sys.stderr.write("    _insert_leaf after: %s\n" % self)
            return (new_parent, data)

        def _insert_left(self, data, maker=None):
            #sys.stderr.write("    _insert_left before: %s \n" % self)
            (new_node, data) = self.left.insert(data, maker)
            #sys.stderr.write("        _insert_left new_node: %s\n" % new_node)
            if new_node is None:
                new_parent = None
            else:
                # Temporarily insert new_node for dumping.  It'll get
                # overwritten shortly.
                self.left = new_node
                if maker:
                    maker.make_frame()
                if self.data2 is None:
                    new_parent = None
                    self.data2 = self.data1
                    self.data1 = new_node.data1
                    self.right = self.middle
                    self.middle = new_node.middle
                    self.left = new_node.left
                    self.hilite = True
                    if maker:
                        maker.make_frame()
                else:
                    # Split node
                    new_parent = BTree.Node(self.data1)
                    self.data1 = self.data2
                    self.data2 = None
                    self.left = self.middle
                    self.middle = self.left
                    self.right = None
                    new_parent.left = new_node
                    new_parent.middle = self
                    new_parent.hilite = True
                    new_parent.left.hilite = True
                    new_parent.middle.hilite = True
                    #sys.stderr.write("        _insert_left new_parent: %s\n" % new_parent)
            #sys.stderr.write("    _insert_left after: %s \n" % self)
            return (new_parent, data)

        def _insert_middle(self, data, maker=None):
            #sys.stderr.write("    _insert_middle before: %s\n" % self)
            (new_node, data) = self.middle.insert(data, maker)
            #sys.stderr.write("        _insert_middle new_node: %s\n" % new_node)
            if new_node is None:
                new_parent = None
            else:
                # Temporarily insert new_node for dumping.  It'll get
                # overwritten shortly.
                self.middle = new_node
                if maker:
                    maker.make_frame()
                if self.data2 is None:
                    new_parent = None
                    self.data2 = new_node.data1
                    self.middle = new_node.left
                    self.right = new_node.middle
                    self.hilite = True
                    if maker:
                        maker.make_frame()
                else:
                    # Split node
                    new_parent = new_node
                    new_sibling = BTree.Node(self.data2)
                    self.data2 = None
                    new_sibling.middle = self.right
                    new_sibling.left = new_parent.middle
                    self.right = None
                    self.middle = new_parent.left
                    new_parent.left = self
                    new_parent.middle = new_sibling
                    new_parent.hilite = True
                    new_parent.left.hilite = True
                    new_parent.middle.hilite = True
                    #sys.stderr.write("        _insert_middle new_sibling %s\n" % new_sibling)
            #sys.stderr.write("        _insert_middle new_parent: %s\n" % new_parent)
            #sys.stderr.write("    _insert_middle after: %s\n" % self)
            return (new_parent, data)

        def _insert_right(self, data, maker=None):
            #sys.stderr.write("    _insert_right before: %s\n" % self)
            (new_node, data) = self.right.insert(data, maker)
            if new_node is None:
                new_parent = None
            else:
                # Temporarily insert new_node for dumping.  It'll get
                # overwritten shortly.
                self.right = new_node
                if maker:
                    maker.make_frame()
                # Split node
                new_parent = BTree.Node(self.data2)
                self.data2 = None
                self.right = None
                new_parent.left = self
                new_parent.middle = new_node
                new_parent.hilite = True
                new_parent.left.hilite = True
                new_parent.middle.hilite = True
                #sys.stderr.write("    _insert_right new_node: %s\n" % new_node)
                #sys.stderr.write("    _insert_right new_parent: %s\n" % new_parent)
            #sys.stderr.write("    _insert_right after: %s\n" % self)
            return (new_parent, data)

        def insert(self, data, maker=None):
            #sys.stderr.write("    insert: %s\n" % self)
            assert self.data1 is not None
            assert (((self.left is None) and (self.middle is None) and (self.right is None)) or
                    ((self.left is not None) and (self.middle is not None)))
            assert (((self.data2 is None) and (self.right is None)) or
                    ((self.data2 is not None) and ((self.right is None) == (self.left is None))))
            if self._isleaf():
                result = self._insert_leaf(data, maker)
            elif data < self.data1:
                result = self._insert_left(data, maker)
            elif self.data1 < data and (self.data2 is None or data < self.data2):
                result = self._insert_middle(data, maker)
            elif self.data2 and self.data2 < data:
                result = self._insert_right(data, maker)
            elif self.data1 < data:
                # data == data2
                self.hilite - True
                result = (None, self.data2)
            else:
                # data == data1
                self.hilite - True
                result = (None, self.data1)
            return result


        def walk(self, action):
            if self.left:
                self.left.walk(action)
            if self.data1:
                #sys.stdout.write("Node(0x%x) " % id(self))
                action(self.data1)
            if self.middle:
                self.middle.walk(action)
            if self.data2:
                #sys.stdout.write("Node(0x%x) " % id(self))
                action(self.data2)
            if self.right:
                self.right.walk(action)

        def name(self):
            label1 = "%s" % self.data1
            if self.data2:
                label2 = "| %s" % self.data2
            else:
                label2 = ""
            return "".join([label1, label2])

        def label(self):
            label1 = "%s" % self.data1
            if self.data2:
                label2 = "| %s" % self.data2
            else:
                label2 = ""
            return "".join([label1, label2])

        def dot_fmt_node(self):
            if self.hilite:
                hilite_code = ", style=filled, fillcolor=yellow"
                self.hilite = False
            else:
                hilite_code = ""
            format_list = ["\"%s\" " % (self.name(),),
                           "[",
                           "shape=Mrecord"
                           ", label=\"%s\"" % (self.label(),),
                           hilite_code,
                           "];"]
            return "".join(format_list)


    def __init__(self):
        self.root = None

    def depth(self):
        node = self.root
        n = -1
        while node:
            n += 1
            node = node.left
        return n

    def verify(self):
        if not self.root:
            return True
        return self.root.verify()

    def insert(self, data, maker=None):
        sys.stderr.write("**** Inserting %s\n" % data.word)
        if self.root is None:
            self.root = BTree.Node(data)
            self.root.hilite = True
            if maker:
                maker.make_frame()
        else:
            (new_root, data) = self.root.insert(data, maker)
            #sys.stderr.write("**** Data Inserted: (%s, %s)\n" % (new_root, data))
            if new_root is not None:
                self.root = new_root
                if maker:
                    maker.make_frame()
        return data

    def walk(self, action):
        if self.root is None:
            print "Empty tree"
        else:
            self.root.walk(action)

    def bylevel(self, fn):
        if not self.root:
            return
        worklist = collections.deque()
        worklist.append(self.root)
        while True:
            try:
                node = worklist.popleft()
            except IndexError:
                return
            fn(node)
            if node.left:
                worklist.append(node.left)
            if node.middle:
                worklist.append(node.middle)
            if node.right:
                worklist.append(node.right)



class WordCounter(object):

    def __init__(self, word):
        self.word = word
        self.count = 0

    def __lt__(self, counter):
        return self.word < counter.word

    def increment(self):
        self.count += 1
        return self

    def __str__(self):
        return str("%s (%s)" % (self.word, self.count))


def print_counter(counter):
    print  "%7d %s" % (counter.count, counter.word)


class Dot(object):

    def __init__(self, tree, out=None):
        if not out:
            out = sys.stdout
        self.tree = tree
        self.out = out

    def generate(self):
        def emit_node(node):
            self.out.write("   %s\n" % node.dot_fmt_node())

        def emit_links(node):
            if node.left:
                self.out.write("   \"%s\" -> \"%s\" [label=\"l\"];\n" % (node.name(), node.left.name()))
            if node.middle:
                self.out.write("   \"%s\" -> \"%s\" [label=\"m\"];\n" % (node.name(), node.middle.name()))
            if node.right:
                self.out.write("   \"%s\" -> \"%s\" [label=\"r\"];\n" % (node.name(), node.right.name()))

        self.out.write("digraph {\n")
        self.tree.bylevel(emit_node)
        self.tree.bylevel(emit_links)
        self.out.write("}\n");


class DotMaker(object):

    def __init__(self, tree, basename="frame-"):
        self.basename = basename
        self.count = 0
        self.tree = tree

    def make_frame(self):
        self.count += 1
        out = open("%s%03d.dot" % (self.basename, self.count), "w")
        Dot(self.tree, out).generate()
