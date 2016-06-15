#!/usr/bin/env python

"""
Write a decorator which generates a set of methods in a class given a template
function and a dictionary of function names and their parameters.
E.g. the following two code snippets shall be equivalent:
        def template(self, a, b, c):
            print self.x, a, b, c

        method_table = {
            'test': dict(a=10, c=20),
            'other_test': dict(b=30),
        }

        @template_methods(template, method_table):
        class A(object):
            x = 10
            pass

        class A(object):
            x = 10

            def test(self, b):
                print self.x, 10, b, 30

            def other_test(self, a, c):
                print self.x, a, 20, c

Hint
You might use a funcutils.partial to make this task easier.
"""


from functools import partial


def template_methods():

    def template(self, a, b, c):
        print self.value, a, b, c

    method_table = {
        'test': dict(a=10, c=20, b=11),
        'other_test': dict(b=30),
    }

    def wrapper(obj):

        for method, params in method_table.items():
            setattr(obj, method, partial(template, obj, **params))
        return obj
    return wrapper


@template_methods()
class SampleClass(object):

    value = 10
    pass

sample = SampleClass()
SampleClass.test(b=13)
SampleClass.other_test(a=121, c=3)
