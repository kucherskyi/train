#!/usr/bin/env python

"""
Write a context manager class that takes an object, its attribute name and
value and sets that attribute, but later restores an original attribute value
in a way suitable for a with statement. For example, the following code snippet
shall print Did you want to exit?:

with memento(sys, 'exit', lambda x: 'Did you want to exit?'):
    print sys.exit(1)
Compare a performance and readability with the same solution using a
contextlib library.
"""


import contextlib
import time
import timeit
import sys


class Memento(object):

    def __init__(self, object, attribute, value):
        self.object = object
        self.attribute = attribute
        self.value = value

    def __enter__(self):
        self.origin_value = getattr(self.object, self.attribute)
        setattr(self.object, self.attribute, self.value)
        return self.object

    def __exit__(self, exc_type, exc_val, exc_tb):
        setattr(self.object, self.attribute, self.origin_value)


@contextlib.contextmanager
def memento(object, attribute, value):

    original = getattr(object, attribute)
    setattr(object, attribute, value)
    yield
    setattr(object, attribute, original)


if __name__ == '__main__':
    cla = """
    import task03 as t
    with t.Memento(sys, 'exit', lambda x: 'Did you want to exit?'):
        sys.exit(1)
    """
    print 'Class: {}'.format(timeit.timeit(stmt=cla, number=10000))

    lib = """
    import task03 as t
    with t.memento(sys, 'exit', lambda x: 'Did you want to exit?'):
        sys.exit(1)
    """
    print 'Contextlib: {}'.format(timeit.timeit(stmt=lib, number=10000))
