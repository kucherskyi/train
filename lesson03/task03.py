#!/usr/bin/env python

"""
Implement the task02 using a str.join and a str.format methods.
"""


def joining_arguments(*args, **kwargs):

    pos = ', '.join([str(x) for x in args])
    named = ', '.join(['{}={}'.format(k, v) for k, v in kwargs.items()])
    return ('{} \n{}'.format(pos, named))

if __name__ == '__main__':
    print (joining_arguments('pos1_value',
                             'pos2_value',
                             'pos3_value',
                             n1='n1_val',
                             n2=1, n3='n3_val'))
