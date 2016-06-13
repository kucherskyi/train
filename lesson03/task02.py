#!/usr/bin/env python

"""
Write a function that takes arbitrary number of positional and named arguments
and returns a string in the following format (use only a str.join method
for this):

pos1_value, pos2_value, pos3_value
named1=named1_value, named2=named2_value
"""


def joining_arguments(*args, **kwargs):

    pos = ', '.join([str(x) for x in args])
    named = ', '.join(['{}={}'.format(k, v) for k, v in kwargs.items()])
    return ('\n'.join([pos, named]))


if __name__ == '__main__':
    print (joining_arguments('pos1_value',
                             'pos2_value',
                             'pos3_value',
                             n1='n1_val',
                             n2=1, n3='n3_val'))
