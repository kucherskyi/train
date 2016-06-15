#!/usr/bin/env python

"""
Write a function which returns a custom dictionary class which allows to set
a predefined set of custom attributes (but not an arbitrary attribute).
E.g. the following code snippet shall work just fine:

Test = dict_with_attrs('test', 'other')
d = Test({'a': 1}, test='test')
d.other = 'Hey!'
d[10] = 11

# This shall fails:
d.unknown = 42
"""


def dict_with_attrs(*attributes):

    class Dictionary(dict):

        __slots__ = attributes

        def __init__(self, *args, **kwargs):
            for k, v in kwargs.iteritems():
                setattr(self, k, v)
    return Dictionary


Test = dict_with_attrs('test', 'second')
d = Test({'a': 1}, test='test')
d.second = 11
d[2] = 3


print d.test
print d.second
