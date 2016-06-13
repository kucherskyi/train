#!/usr/bin/env python

"""
Create a module containing a class MyNumberPrinter which accepts a number in a
constructor and contains the following instance methods:

- me: prints a number itself;
- factorial: prints a factorial of a number;
- string: prints a string concatenated with itself number times;
- update: modifies a number value and prints a new value;
- time_in_past: accepts a one letter string that is either of s, m, h, d and
print a time that is a number of seconds, minutes, hours, or days in the past
since now;

A module shall create several MyNumberPrinter instances showing its
functionality.
"""

import datetime


class MyNumberPrinter(object):

    def __init__(self, number):
        self.number = number

    def me(self):
        print 'Original value is %s' % (self.number)

    def factorial(self):

        def fac_loop(val):
            if val == 0:
                return 1
            return fac_loop(val - 1) * val

        print 'Factorial of {0} is {1}' .format(self.number,
                                                fac_loop(self.number))

    def string(self, text):

        print '%s value %s times is: %s' % (text,
                                            self.number,
                                            text * self.number)

    def update(self, new_value):

        self.number = new_value
        print 'New value is %s' % (self.number)

    def time_in_past(self, val):

        values_range = {'s': 'seconds',
                        'm': 'minutes',
                        'h': 'hours',
                        'd': 'days'}
        if val in values_range.keys():
            delta = datetime.timedelta(**{values_range[val]: self.number})
            vas_ago = datetime.datetime.now().replace(microsecond=0) - delta
            print '%s %s ago vas : %s' % (self.number,
                                          values_range[val],
                                          vas_ago)
        else:
            print 'Defined interval value is not valid'


if __name__ == '__main__':
    my = MyNumberPrinter(5)
    my.me()
    my.factorial()
    my.string('abc')
    my.update(11)
    my.time_in_past('g')

    second_class = MyNumberPrinter(55)
    second_class.time_in_past('d')
