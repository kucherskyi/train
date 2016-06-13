#!/usr/bin/env python

"""
Write a program that redirects its standard input into a standard output line
by line (like a shell pipe operator).
"""

import sys

while sys.stdin.readline != 'exit!':
    sys.stdout.write(inp)
