#!/usr/bin/env python

"""
Print a number of sentences in a file (a sentence shall and in either a dot .
or a tripple-dot ....
"""

import re


with open('alice.txt', 'r') as alice:

    print 'Text has {} sentences' .format(len(re.split(r'\b\.?\.\.?(?=\s)',
                                                       alice.read())))
