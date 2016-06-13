#!/usr/bin/env python

"""
Write an iterator which takes an arbitrary number of iterables and flattens
their output (i.e. iterates over their elements returning one element from each
iterable in a loop). For example, a return of these two iterables: A, B, C, D,
E, F - shall be A, D, B, E, C, F. An iterator shall end when all of iterables
are exhausted.
"""


from collections import Iterable


def flatten(*args):

    for elem in args:
        if isinstance(elem, Iterable):
            element = [iter(elem) for elem in args]
            while element:
                to_remove = []
                for item in element:
                    try:
                        yield item.next()
                    except StopIteration:
                        to_remove.append(item)
                for rem in to_remove:
                    element.remove(rem)


if __name__ == '__main__':
    for elem in flatten(('s', True, 'e'), (1, 2, 3, 4)):
        print elem
