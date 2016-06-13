#!/usr/bin/env python


class Third(object):
    """docstring for Third"""
    def __init__(self, value, val):
        self.val = val
        self.data = value
        self.ty = type(self)
    
    def __add__(self, other):
        return Third(self.data + other)
    def __str__(self):
        return '[Thiird: %s]' % self.ty

    def mul(self):
        print self.ty

a = Third(111, 222)

a.mul()
