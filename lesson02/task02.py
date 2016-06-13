#!/usr/bin/env python

"""
Create a module containing the following functions:

- factorial: accepts one integer and prints its factorial (recursive);
- my_args: accepts an arbitrary number of arguments and prints them all;
- harmony: takes an arbitrary number of floats and prints their harmonic
medium value;
A module shall call its functions with different argumets;
"""

import sys


def factorial(val):

    if val == 0:
        return 1
    return factorial(val - 1) * val

my_args = lambda *args: [x for x in args]

harmony = lambda *args: float(sum(args) / len(args))

print factorial(5)
print my_args(12, 'sad', 11)
print harmony(12.12, 32, 222.32)
