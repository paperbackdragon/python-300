#!/usr/bin/env python

from ctypes import *

libc = CDLL("/usr/lib/libc.dylib")
# for Linux:
# libc = CDLL("libc.so")
libc.printf("printed via libc printf()\n")

# libc.printf("An int %d, a double %f\n", 1234, 3.14)
libc.printf("An int %d, a double %f\n", 1234, c_double(3.14))

# load the math library
libm = CDLL("/usr/lib/libm.dylib")
print libm.pow(3,4)


# now load our own shared library
add = cdll.LoadLibrary("add.so")
print add.add(3,4)
