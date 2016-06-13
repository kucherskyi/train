#!/usr/bin/env python


"""
The same task as above but tripples shall not count (e.g. eee shall not count).
"""

import re

with open('alice.txt', 'r') as alice:

    triples = re.compile(r'(.)\1')
    doubles = 0
    for line in alice:
        if len(triples.findall(line)) == 2:
            pass
        else:
            doubles += len(triples.findall(line))

print '{}  doubles '.format(doubles)
