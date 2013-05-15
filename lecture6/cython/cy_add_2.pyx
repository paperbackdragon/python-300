"""
Cython implementation of the add.c example

This one re-writes the function as a cdef function, then
calls that from a def function

"""

cdef int c_add(int x, int y):
    """
    writing the function as a cdef -- only callable from Cython
    
    use this if the function will be called from multiple places --
      removes python function call overhead.
    """
    cdef int result
    
    result = x + y
    
    return result


def add(x, y):
    return c_add(x, y)








