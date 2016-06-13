#!/usr/bin/env python

"""
Print a number of all occurences of double characters in a file (e.g. ee).
"""

import re

with open('alice.txt', 'r') as alice:

    doubles = 0
    for line in alice:
        doubles += len(re.findall(r'(.)\1', line))

print '{}  doubles '.format(doubles)
