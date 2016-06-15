#!/usr/bin/env python

"""
Write an application which recursively forks itself until a recursion depth
reaches a specified value (passed as a command-line argument). Each child
application shall print its process ID on start and exit; each parent
application shall print a child process ID it has forked and wait for its
completion. Below is an example log of an application stack:
"""

import os
import sys
import threading


def fork(times):
    print 'Started processId {}' .format(os.getpid())

    if times > 1:
        child = os.fork()
        if child:
            print 'processId {0} fork {1}' .format(os.getpid(), child)
            os.waitpid(child, 0)
            print 'processId {0} finished' .format(os.getpid())
        else:
            fork(times - 1)
    else:
        print 'processId {0} finished' .format(os.getpid())


divider = int(sys.argv[1]) / 2
pro = int(sys.argv[1]) - divider
treat = threading.Thread(target=fork, args=(divider,))
treat.start()

treat = threading.Thread(target=fork, args=(pro,))
treat.start()
