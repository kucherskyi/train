#!/usr/bin/env python

"""
Print a number of words in a file (words can be separated by either white
space or any separator (e.g. , or -). Pure integers shall not count but
identifiers consisting of a mix of characters and integers shall count).
"""

with open('alice.txt', 'r') as alice:
    