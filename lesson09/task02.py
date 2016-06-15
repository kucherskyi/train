#!/usr/bin/env python

"""
A task is the same as above, but a keyboard interruption shall be handled
gracefully printing a message Operation terminated by user. In order to better
visualize user interaction, file content shall be read/written line by line
with a time.sleep for one second between each line and printing a diagnostic
information like below (each dot means one line):
Copying a file "aaa.txt" into "bbb.txt"
.............................
Operation complete
In case of user initiated termination all data that was written into a file up
to data shall be preserved.
"""

import os
import sys
import time


input_path = 'alice.txt'
output_path = 'test1.txt'

try:
    sys.stdout.write('Copy from {} to {}.\n' .format(input_path, output_path))
    input_file = open(input_path, 'r')
    output_file = os.open(output_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    for line in input_file:
        os.write(output_file, line)
        sys.stdout.write('.')
        time.sleep(1)

    sys.stdout.write('\nCompleted.\n')
except IOError, error:
    sys.stderr.write('{} error: {}.\n' .format(error.filename, error.strerror))
    sys.exit(1)
except OSError, error:
    sys.stderr.write('%s file error: %s.\n' .format(
        error.filename, error.strerror))
    sys.exit(1)
except KeyboardInterrupt:
    sys.stdout.write('Terminated by user.\n')
    sys.exit(0)
