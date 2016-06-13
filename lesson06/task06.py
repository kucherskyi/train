#!/usr/bin/env python

"""
Print the first N most used English words in alice.txt; N shall be a positive
number taken from a command line.
"""
import collections
import re
import sys

unique = collections.Counter()

with open('alice.txt', 'r') as alice:
    text = alice.read().lower()

for word in re.findall(r'\b([a-zA-Z]+)\b', text):
    unique[word] += 1

print unique.most_common(int(sys.argv[1]))
