#!/usr/bin/env python

"""
Write a function which returns a tuple of first 10 and last 10 characters of an
input string. Use an output of that function to print the first 10, the last 10
characters of some string and their concatenation.
"""


def return_tuple(string):

    return string[:10], string[-10:]

string_to_input = """Write a function which returns a tuple of first 10 and"""
beg, end = return_tuple(string_to_input)

print 'First 10: {0} \nLast 10: {1} \nConcatinated: {2}'.format(beg,
                                                                end,
                                                                beg + end)
