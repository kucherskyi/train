#!/usr/bin/env python

"""
Write a non-recursive function calculating a factorial of a number using an
xrange function.
"""


def factorial(number):

    if number > 1:
        fact = 1
    for n in xrange(2, number + 1):
        fact *= n
    return fact

print factorial(5)
