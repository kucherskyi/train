#!/usr/bin/env python

"""
Write a program that prints N last lines of a file in reverse order (just like
a tail -r FreeBSD command). Both file name and a number of lines to print shall
be passed as command-line arguments.
Think of a memory-efficient yet fast way to implement this task.
"""

#!/usr/bin/env python

"""
Write a program that prints N last lines of a file in reverse order (just like
a tail -r FreeBSD command). Both file name and a number of lines to print shall
be passed as command-line arguments.

Think of a memory-efficient yet fast way to implement this task.
"""
import os,
import itertools
import sys
import re


def reversed_line(filename):

    with open (filename, 'r') as file:
        file.seek(0, os.SEEK_END)
        size = file.tell()
        while size > 0:
            
            pass


print reversed_line('alice.txt')