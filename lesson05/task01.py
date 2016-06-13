#!/usr/bin/env python

"""
Remove all empty lines in a file and print a number of removed lines.
"""

import re


empty_lines = 0
for line in open('alice.txt', 'r'):
    if re.match(r'^\n$', line):
        empty_lines += 1
    else:
        pass

print ('Removed {} empty lines'.format(empty_lines))
