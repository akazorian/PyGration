from types import *
from math import *

class Integral:
    """Base class to represent the integral

    >>> integral = Integral(lambda x: 1/(2 * x), 0, 4)
    >>> integral.f(2)
    0.25
    >>> integral.a
    0
    >>> integral.b
    4
    >>> integral_2 = Integral(lambda x: x ** 2, 7, -2)
    >>> integral_2.f(4)
    16
    >>> integral_2.a
    -2
    >>> integral_2.b
    7
    """

    def __init__(self, f, a, b):
        self.f = f
        if a > b:
            self.a, self.b = b, a
        else:
            self.a, self.b = a, b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
