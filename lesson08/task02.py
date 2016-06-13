#!/usr/bin/env python

"""
Write a simple parametrized decorator so that the below code snippet prints
Hello\nWorld to the standard output:
"""


def decorator(word):

    def decorator_inner(func):
        def wrapper(arg):
            func(arg)
            print word
        return wrapper
    return decorator_inner


@decorator('World!')
def hello(arg):
    print arg

hello('Hello')
