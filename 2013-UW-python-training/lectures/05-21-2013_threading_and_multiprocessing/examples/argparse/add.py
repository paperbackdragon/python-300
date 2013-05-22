#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="add app")
parser.add_argument('x', type=int, help="x value")
parser.add_argument('y', type=int, help="x value")

args = parser.parse_args()

print args.x + args.y
