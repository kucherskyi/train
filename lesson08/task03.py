#!/usr/bin/env python

"""
Redo a transaction handler task in such a way that there is no necessity to
wrap each action requiring a transaction into a separate function.
E.g. in the following code snippet there are 3 actions wrapped into a
transaction, including nested transactions:
    def my_func(a, b, c):
        with transaction('root'):
            print a
            with transaction('nested successful'):
                print b
            with transaction('nested with error'):
                print c
                raise Exception
Hint
Use a contextlib.context_manager decorator to implement this task.
"""

from contextlib import contextmanager


@contextmanager
def transaction(level):

    print 'Start transaction: {}'.format(level)
    try:
        yield
        print 'Success transaction: {}' .format(level)
    except:
        print 'Cancel transaction: {}' .format(level)


def my_func(a, b, c):

    with transaction('root'):
        print a
        with transaction('nested successful'):
            print b
        with transaction('nested with error'):
            print c
            raise Exception

my_func(10, 5, 4)
