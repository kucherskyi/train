#!/usr/bin/env python

"""
Replace all blank lines (lines consisting of just a white space) with an empty
line and print a number of modified lines. Initially empty lines (lines that
were empty before a replacement) shall not count.
"""

import re


file_without_empty = open('alice_empty.txt', 'w')

empty_lines = 0
for line in open('alice.txt', 'r'):
    if re.match(r'^\s+\n', line):
        empty_lines += 1
        file_without_empty.write('\n')
    else:
        file_without_empty.write(line)

file_without_empty.close()
print ('Removed {} empty lines'.format(empty_lines))
