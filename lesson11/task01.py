#!/usr/bin/env python

"""
Implement a parametrized file copy operation accepting the following arguments:

input file path: specified as either first argument, or through one of -i,
--input options, required;
output file path: specified as either second argument, or through one of -o,
--output options, required;
buffer size in bytes: specified as one of -s, --buffer-size options,
optional, defaults to 8192;
program help: specified as one of -h, --help option; an application shall
print a program help and exit if this option is specified;
verbose mode: specified as one of -v, --verbose options, optional, defaults
to False;
an application shall print a dot per each file chunk copy in this mode;

In case of any argument error an application shall print an appropriate error
and a short usage information (not help). Any other error shall be handled
gracefully.
An application shall return an appropriate exit code.
"""


import argparse
import sys


parser = argparse.ArgumentParser()

parser.add_argument('path', nargs='*', help='> in/out files path')
parser.add_argument('-i', '--input', help=' > input file')
parser.add_argument('-o', '--output', help='> output file.')
parser.add_argument('-v', '--verbose', help='> increase verbosity',
                    default=False,
                    action='store_true')
parser.add_argument('-s', '--buffer-size', default=8196, type=int,
                    help='Buffer size.')

args = parser.parse_args()

try:
    index_arg = 0
    input_path = args.input
    output_path = args.output

    if not input_path:
        input_path = args.path[index_arg]
        index_arg += 1

    if not output_path:
        output_path = args.path[index_arg]
        index_arg += 1

    if len(args.path) > index_arg:
        parser.error('Need less path params.')

    file_in = open(input_path)
    file_out = open(output_path, 'w')
    while True:
        chunk_copy = file_in.read(args.buffer_size)
        if chunk_copy:
            file_out.write(chunk_copy)
            if args.verbose:
                sys.stdout.write('.')
        else:
            sys.stdout.write('\n')
            break
except IndexError:
    parser.error('Need more path params.')
except IOError, e:
    print e
    sys.exit(1)
except OSError, e:
    print e
    sys.exit(1)
