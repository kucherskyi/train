#!/usr/bin/env python

"""
Remove all leading and trailing white-space from a file and print a number of
modified lines.
"""

import re

whitespace = 0
for line in open('alice.txt', 'r'):
    if len(line) > len(line.strip()):
        whitespace += 1

print ('{} lines with leading and/or trailing white-spaces'.format(whitespace))
