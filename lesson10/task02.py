#!/usr/bin/env python

"""
Write a Mixin class that checks if a given class instance instance is
True or False based on a truth table. A truth table is a list of object hashes
that would evaluate to True (or False) specified as a class attribute.
For example, the following code snippet shall print True True:
class TrueTest(int, TruthTable):

    __true_values__ = (0, 1, 2, 3)

class FalseTest(str, TruthTable):

    __false_values__ = ('false', hash('no'))

print bool(TrueTest(0)), bool(FalseTest(''))
"""


class TruthTable(object):

    def __nonzero__(self):
        if hasattr(self, '__true_values__'):
            return self in self.__true_values__
        elif hasattr(self, '__false_values__'):
            return self not in self.__false_values__
        else:
            pass


class TrueTest(TruthTable, int):

    __true_values__ = (0, 1, 2, 3)


class FalseTest(TruthTable, str):

    __false_values__ = ('false', hash('no'))


print bool(TrueTest(0))
print bool(FalseTest(''))

