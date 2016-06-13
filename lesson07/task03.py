#!/usr/bin/env python

"""
Write a generator which produces an infinite sequence of Fibonacci numbers.
Use it to print first 100 Fibonacci numbers followed by every tenth such number
between 100th and 1000th (e.g. 100th, 110th, 120th and so on).
Hint
Use enumerate to solve the second part of a task. Think of a way to form a
finite loop off an infinite generator (e.g. use some of itertools module
functions to achieve this).
"""


import itertools


def fibo():

    a = b = 1
    while True:
        yield a
        a, b = b, a + b

for key, value in enumerate(itertools.islice(fibo(), 99)):
    print '{}:{}'.format(key + 1, value)

for key, value in enumerate(itertools.islice(fibo(), 99, 1000, 10)):
    print '{}:{}' .format((100 + 10 * key), value)
