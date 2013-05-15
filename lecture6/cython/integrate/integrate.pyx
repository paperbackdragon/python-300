def f(double x):
    return x**2-x

def integrate_f(double a, double b, int N):
    cdef int s = 0
    cdef double dx = (b-a)/N
    for i in range(N):
        s += f(a+i*dx)
    return s * dx


