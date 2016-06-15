#!/usr/bin/env pytkhon

"""
Write a simple program that reads content from one file an writes it to yet
another file. All possible I/O and OS errors shall be handled gracefully
(e.g. nonexisting input file, insufficient permissions etc) and an appropriate
diagnostic information shall be printed to standard error. If a read of an
input file fails - not subsequent write shall be done. An output file shall be
written only if it does not exist, otherwise an error shall occur (think of
concurrency problems associated with this part of a task).
An application shall return an appropriate exit code identifying success or
failure do fulfill a requested operation.
"""


import os
import sys

input_path = 'alice.txt'
output_path = 'test.txt'

try:
    input_file = open(input_path, 'r')
    otuput_file = os.open(output_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    for line in input_file:
        os.write(otuput_file, line)

    sys.stdout.write('Done!')
except IOError, e:
    print >> sys.stderr, e
    sys.exit(1)
except OSError, e:
    print >> sys.stderr, e
    sys.exit(1)
