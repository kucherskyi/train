#!/usr/bin/env python

"""
Write an application which spawns several children threads or processes (based
on a command line argument). A parent shall read from a file and put all lines
into a queue. Children shall take those lines and append them into another
file if and only if those lines start with a capital letter. An order of lines
in a resulting file is not important, however, all lines shall be put
intact.All threads (processes) shall exit gracefully after an input file
ends and all necessary lines are put to output an file.

Compare a performance difference between the two solutions for alice.txt.
"""


import argparse
import os
import multiprocessing
import time
import threading
import Queue


def worker(queue):

    output = os.open(output_path, os.O_APPEND | os.O_WRONLY)
    while True:
        line = queue.get()
        if line[0].isupper():
            os.write(output, line)
        queue.task_done()


input_path = 'alice.txt'
output_path = 'alice_edited.txt'

parser = argparse.ArgumentParser()
child_type = parser.add_mutually_exclusive_group(required=True)
child_type.add_argument('-t', action='store_true', help='Threads.')
child_type.add_argument('-p', action='store_true', help='Processes.')
args = parser.parse_args()

start = time.time()

if args.t:
    queue = Queue.Queue()

    for i in xrange(10):
        t = threading.Thread(target=worker, args=(queue,))
        t.daemon = True
        t.start()
elif args.p:
    queue = multiprocessing.JoinableQueue()

    for i in xrange(10):
        p = multiprocessing.Process(target=worker, args=(queue,))
        p.daemon = True
        p.start()

for line in open(input_path):
    queue.put(line)

queue.join()

print time.time() - start






