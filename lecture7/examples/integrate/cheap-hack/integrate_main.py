#!/usr/bin/env python

import sys
sys.path.append("..")


from integrate import integrate, f # integrate_f_with_functional_tools as integrate_f
# from integrate import integrate_f

import argparse

parser = argparse.ArgumentParser(description='integrator')
parser.add_argument('a', nargs='?', type=float, default=0.0)
parser.add_argument('b', nargs='?', type=float, default=10.0)
parser.add_argument('N', nargs='?', type=int, default=10**7)

args = parser.parse_args()
a = args.a
b = args.b
N = args.N

# print "Numerical solution from (%(a)f to %(b)f with N=%(N)d : \n%(x)f" % \
    # {'a': a, 'b': b, 'N': N, 'x': integrate_f(a, b, N)}
print "%(x)f" % {'x': integrate(f, a, b, N)}
