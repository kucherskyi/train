#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write a function which takes a unicode string and encodes it into a printable
US-ASCII character set. Use some real UTF-8 characters to test this function.
"""

encoded = lambda string: string.encode('utf-8')

test_string = u'\U00000394 \u0394 asd фысфыс'

print encoded(test_string)
print test_string.__repr__()
