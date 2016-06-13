#!/usr/bin/env python

"""
Write a simple application that writes a string Hello world into a file
specified as a command-line argument.
"""

import sys


file = open(sys.argv[1], 'w')
file.write('Hello World')
file.close()