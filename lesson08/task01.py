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

    func.counter = 0

    def wrapper(*args):
        func.counter += 1
        print 'Transaction {} for {} started.' .format(func.counter,
                                                       func.__name__)
        try:
            result = func(*args)
            print 'Transaction {} for {} completed' .format(func.counter,
                                                            func.__name__)
            return result
        except:
            print 'Transaction {} for {} cancelled', format(func.counter,
                                                            func.__name__)

    return wrapper


@decorator
def mult(a, b):
    return a * b

print mult('sss', 3)
