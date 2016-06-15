#!/usr/bin/env python

"""
Write a simple decorator which implements a transaction handler. There shall
be no real transaction performed, instead, a decorator shall print messages
like Transaction 1 for my_func started, Transaction 2 for my_func complete,
or Transaction 3 for my_func cancelled at transaction start, completion, or
cancellation (in case of an error in a decorated function) accordingly.
Declare several functions doing different stuff that are decorated with
this decorator.
Hint
For simplicity it is allowed to use a global variable to auto-increment
transaction numbers. Use a __name__ function attribute to distinguish
transactions for different functions.
"""


def decorator(func):

    func.number = 0

    def wrapper(*args):
        func.number += 1
        name = func.__name__
        print 'Transaction {} for {} started.' .format(func.number, name)
        try:
            result = func(*args)
            print 'Transaction {} for {} completed' .format(func.number, name)
            return result
        except Exception, error:
            print 'Transaction {} for {} cancelled at transaction start. \nError : {}' .format(func.number, name, error)

    return wrapper


@decorator
def multiplication(a, b):
    return a * b

@decorator
def division(a, b):
    return a / b

print multiplication(2, 4)
print division(2, 0)
print multiplication(2, 4)
