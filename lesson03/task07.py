#!/usr/bin/env python

"""
Write a function which takes a string and returns the first 10 characters off
it concatenated with the last 10 characters.
"""

concat = lambda string: '{0}{1}'.format(string[:10], string[-10:])

print concat("""Write a function which takes a string and returns the first 10
    characters off it concatenated with the last 10 characters.""")
