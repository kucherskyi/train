#!/usr/bin/env python

"""
Print a number of vocal letters in first 100 lines of a file.
"""

import re

with open('alice.txt', 'r') as alice:

    vocals = 0
    for x in xrange(100):
        vocals += len(re.findall(r'[aeiouy]', alice.readline()))

print '{} vocals in first 100 lines'.format(vocals)
