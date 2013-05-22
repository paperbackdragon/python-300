#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser(description='killer app')
parser.add_argument('--verbose', '-v', action='store_true', help="verbose")
subparsers = parser.add_subparsers(help='sub command')

null_parser = subparsers.add_parser('null', help='null')

echo_parser = subparsers.add_parser('echo', help='echo')
echo_parser.add_argument('message', nargs='*', help='values')

args = parser.parse_args()
print vars(args).get('message', "null")


