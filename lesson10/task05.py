#!/usr/bin/env python

"""
Write a universal transparent proxy that is able to provide read/write access
to attributes of any object instance being proxied. For example, the following
code snippet shall print Hello World!:
class A(object):

    phrase = 'Test'

    def test(self):
        print self.phrase

proxy = Proxy(A())
proxy.phrase = 'Hello World!'
proxy.test()
In addition, a proxy shall count how many times a proxied object methods were
called (separately for each method).
Note
A method can be accessed but not called, hence, you need to proxy method
objects as well to fulfill this task. At the same moment, any read/write
operation on method proxy shall be delegated to an original method as well.
"""


class Proxy(object):

    def __init__(self, object):
        self.__dict__['count'] = {}
        self.__dict__['proxied_object'] = object

    def __getattr__(self, attribute):
        value = getattr(self.__dict__['proxied_object'], attribute)
        return self.__wrapper(attribute, value) if callable(value) else value

    def __setattr__(self, name, value):
        setattr(self.__dict__['proxied_object'], name, value)

    def __wrapper(self, name, value):
        self.__dict__['count'].setdefault(name, 0)

        def result(*args, **kwargs):
            self.__dict__['count'][name] += 1
            return value(*args, **kwargs)

        return result

    def statistics(self):
        for func, times in self.__dict__['count'].items():
            print '%10s: %s' % (func, times)


class A(object):

    phrase = 'Test'

    def test(self):
        print self.phrase

    def param_test(self, param):
            print param


proxy = Proxy(A())

proxy.test()
proxy.test()
proxy.param_test('lhllhhjlhl')
other_proxy = Proxy(A())
other_proxy.test()
other_proxy.test()
other_proxy.param_test('ykykykykf')
proxy.test()
proxy.statistics()
other_proxy.statistics()