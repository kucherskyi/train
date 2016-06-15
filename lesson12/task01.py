#!/usr/bin/env python

"""
Spawn several counter threads each counting from 1 to a specified number and
printing those numbers to the standard output. Each counter thread shall sleep
for a specified number of seconds (float) between prints. There shall be a
status thread which prints how many threads are still alive in a specified time
interval. An application shall exit when all counter threads finish their work.
"""
import time
import threading


def count(to_stop, sleep):

    for el in xrange(1, to_stop + 1):
        print 'Count: {}'.format(el)
        time.sleep(float(sleep))


def status(refresh):

    while True:

        counts = 0
        for thread in threading.enumerate():
            if thread.name == 'count':
                counts += 1

        print 'Threats alive - {}'.format(threading.activeCount())

        if counts:
            time.sleep(refresh)
        else:
            print 'Completed!'
            break


if __name__ == '__main__':
    treat = threading.Thread(target=count, args=(5, 1), name='count')
    treat.start()

    treat = threading.Thread(target=count, args=(8, 2), name='count')
    treat.start()

    treat = threading.Thread(target=status, args=(1,), name='status')
    treat.start()
