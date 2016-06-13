#!/usr/bin/env python
"""
Write a function which takes a string and replaces all vocal letters in it to
an uppercase using a str.replace method.
"""

VOCALS = 'aeiouy'


def vocal_upper(string):

    for letter in VOCALS:
        string = string.replace(letter, letter.upper())
    return string

print vocal_upper('These five or six letters')
