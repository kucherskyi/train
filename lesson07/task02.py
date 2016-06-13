#!/usr/bin/env python

"""
Create a function returning a list of all numbers N smaller than input integer
M such that N is a multiplier of 3 while N + 1 is a multiplier of 5. Use it to
print all such numbers smaller than 100.
Hint
Use an xrange function and a list comprehension to solve this task.
"""


def multiplier(max):

    return [number for number in xrange(0, max, 3) if (number + 1) % 5 == 0]

print multiplier(100)
