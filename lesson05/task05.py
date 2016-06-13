#!/usr/bin/env python

"""
Print a number of numbers in a file; each number shall count only once
(e.g. 1234 shall count only once, not 4 times).
"""

import re

with open('alice.txt', 'r') as alice:

    numbers = 0
    for line in alice:
        numbers += len(re.findall(r'\d+', line))

print '{} numbers'.format(numbers)
