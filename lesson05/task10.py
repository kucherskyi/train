#!/usr/bin/env python

"""
Replace each occurence of Alice was to Alice is and print a number of modified
phrases; sentences breaking though lines shall be modified correctly as well.
"""

import re

with open('alice.txt', 'r') as alice:

    print '{} modified' .format(re.subn(r'Alice was',
                                        r'Alice is',
                                        alice.read())[1])
