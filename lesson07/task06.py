#!/usr/bin/env python

"""
Write a generator that consumes lines of a text and prints them to standard
output. Use this generator and a flatten function from the previous task to
print contents of two different files to a screen pseudo-simultaneously.
"""


from task05 import flatten


def line_writer():
    yield
    while True:
        print (yield)

generate = line_writer()
generate.next()

for line in flatten(open('alice.txt'), open('alice01.txt')):
    generate.send(line)
