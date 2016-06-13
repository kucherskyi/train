#!/usr/bin/env python

"""
Using a timeit module compare a speed of 1 000 000 operations of creating a
tuple, a list, and a set of all integer digits (numbers 0-9).
"""

import timeit


def performance(value):

    return '{} - {}' .format(type(value), timeit.timeit(stmt=str(value),
                                                        number=1000000))

print performance(tuple(xrange(0, 10)))
print performance(list(xrange(0, 10)))
print performance(set(xrange(0, 10)))
