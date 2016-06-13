#!/usr/bin/env python

"""
Print a number of unique English words in alice.txt.
"""
import collections
import re


unique = collections.Counter()

with open('alice.txt', 'r') as alice:
    text = alice.read().lower()

for word in re.findall(r'\b([a-zA-Z]+)\b', text):
    unique[word] += 1
print len(unique)