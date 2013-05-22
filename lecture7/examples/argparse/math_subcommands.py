import argparse

def add(x,y):
    return x+y

def double(x):
    return 2*x

def handle_sum(*args):
    return sum(args)

parser = argparse.ArgumentParser(description='add app')
parser.add_argument('--verbose', '-v', action='store_true', help='verbose')

subparsers = parser.add_subparsers(help='sub command')

add_parser = subparsers.add_parser('add', help='add')
add_parser.add_argument('x', type=float, nargs=2, help='values')
add_parser.set_defaults(func=add)

sum_parser = subparsers.add_parser('sum', help='sum')
sum_parser.add_argument('x', type=float, nargs='+', help='values')
sum_parser.set_defaults(func=handle_sum)

double_parser = subparsers.add_parser('double', help='double')
double_parser.add_argument('x', type=float, nargs=1, help='value')
double_parser.set_defaults(func=double)

args = parser.parse_args()
if args.verbose:
    print "executing command"

print args.func(*(args.x))
