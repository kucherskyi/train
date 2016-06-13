#!/usr/bin/env python

"""
Write a function that restores function arguments off the output of the
previous function into a tuple of positional and a dictionary of named
arguments. For simplicity assume that argument values are all strings that
does not contain special characters. Use a str.split method for this task.
"""
from task03 import joining_arguments

str_value = joining_arguments('pos1_value',
                              'pos2_value',
                              'pos3_value',
                              n1='n1_val',
                              n2=1, n3='n3_val')


def restoration(value):

    named = {}
    pos = []
    edited = value.replace(' \n', ', ').split(', ')
    for elem in edited:
        if '=' in elem:
            sub = elem.split('=')
            named[sub[0]] = sub[1]
        else:
            pos.append(elem)
    print ('{}\n{}'.format(named, tuple(pos)))


restoration(str_value)
