#!/usr/bin/env python

"""
Write a function that takes a comma-separated string and returns a last element
(separated by a last comma) or the entire string if there is no comma in it.
"""
csv_func = lambda arg: arg.split(',')[-1]

print csv_func('firstsecond third last')