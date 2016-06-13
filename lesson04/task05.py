#!/usr/bin/env python

"""
Write a program that prints some statistics about itself to standard output:
a path to executable, command line arguments, imported module names and
corresponding file paths, environment variables.
"""


import datetime
import os
import sys



print 'Path to executable: %s\n' % sys.executable
print 'Command line arguments: % s\n' % sys.argv

print 'Imported modules (%s):' % len(sys.modules.items())
for key, val in sys.modules.items():
    print key.ljust(50), val

print 'Environment variables (%s):' % len(os.environ.items())
for key, val in os.environ.items():
    print key.ljust(50), val

