#!/usr/bin/env python

"""
Write a program that waits for a user input and prints a dot every second until
a user either hit Enter or is killed with a signal. In case of a Ctrl-C
a message User input cancelled shall be printed on a new line. If a user input
was received an application shall print it back on a new line.
Hint
Use a system timer to implement this task without threads.
"""


import sys
import signal


def out(signum, frame):

    sys.stdout.write('\nUser input cancelled.\n')
    sys.exit()


def dot(signum, frame):

    sys.stdout.write('.')


signal.signal(signal.SIGINT, out)
signal.signal(signal.SIGALRM, dot)

signal.setitimer(signal.ITIMER_REAL, 1, 1)

print raw_input()
