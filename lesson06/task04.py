#!/usr/bin/env python

"""
Print a statistics about alice.txt like a wc Unix command (number of lines,
words, and characters).
Hint
For this task and below assume that an English word cannot be split over
multiple lines using a hyphen; and that a hyphen is a normal separator between
words (e.g. a phrase in-line consists on two words).
"""

import collections
import re

stats = collections.Counter()

with open('alice.txt', 'r') as alice:

    for lines in alice:
        stats['Lines'] += 1
        stats['Words'] += len(re.findall(r'\b([a-zA-Z]+)\b', lines))
        for char in lines:
            if char.isalpha():
                stats['Characters'] += 1

print dict(stats)
