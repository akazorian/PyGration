from Integral import *
from math import *
import sys

sys.setrecursionlimit(100000)


class Simpson_Rule:
    """ Application of Simpson's Rule in approximating integral and error bounds.
    """

    def __init__(self, integral, n):
        """
        >>> integral = Integral(lambda x: x ** 2, 4, -2)
        >>> Simpson = Simpson_Rule(integral, 3)
        Traceback (most recent call last):
                ...
        AssertionError: The Simpson's Rule requires that there be an even number of n sub-intervals as a parabola between three points requires two sub-intervals.
        """
        assert n % 2 == 0, "The Simpson's Rule requires that there be an even number of sub-intervals as a parabola between three points requires two sub-intervals."

        self.integral = integral
        self.n = n
        self.delta_x = (self.integral.b - self.integral.a) / self.n

    def Simpson_approx(self):
        """ Applies Simpson's Theory for the approximation of a 
                definite integral to a given integral.

        >>> integral = Integral(lambda x: 1 / x, 1, 2)
        >>> Simpson = Simpson_Rule(integral, 10) 
        >>> Simpson.Simpson_approx()
        0.6931502306889303
        >>> integral_2 = Integral(lambda x: 1 / (x ** 2), 20, 20)
        >>> Simpson_2 = Simpson_Rule(integral_2, 10)
        >>> Simpson_2.Simpson_approx()
        Traceback (most recent call last):
                ...
        AssertionError: The definite integral of any given integral on [a, b] when a = b, is always 0.
        """

        assert type(
            self.integral) is Integral, "Simpson's approximation must be given a proper definite integral to compute"
        assert self.integral.a != self.integral.b, "The definite integral of any given integral on [a, b] when a = b, is always 0."

        def __calc_series(count, x, mult_by_four):
            if count == 0:
                return self.integral.f(x) + __calc_series(count + 1, x + self.delta_x, True)
            elif count == self.n:
                return self.integral.f(x)
            elif mult_by_four:
                return (4 * self.integral.f(x)) + __calc_series(count + 1, x + self.delta_x, False)
            else:
                return (2 * self.integral.f(x)) + __calc_series(count + 1, x + self.delta_x, True)

        return (self.delta_x / 3) * __calc_series(0, self.integral.a, False)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
