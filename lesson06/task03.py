#!/usr/bin/env python

"""
Print a number of times that each English character is used in alice.txt.
Hint
For this task and below a character case shall be ignored.
"""

import collections


def letters_count(to_parce):

    letters_hash = collections.Counter()
    for letter in to_parce.lower():
        if letter.isalpha():
            letters_hash[letter] += 1

    return letters_hash

with open('alice.txt', 'r') as alice:
    to_parce = alice.read()

for letter, count in letters_count(to_parce).items():
    print 'Letter {} => {} times'.format(letter, count)
