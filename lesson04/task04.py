#!/usr/bin/env pytkhon

"""
Write a program that lists all file names, their permissions, ownership,
last modified date in a specified directory (like an ls -l shell command).
If no directory is specified as the first (and only) command-line argument
than a current directory shall be listed. If more than one argument is passed
or the specified directory does not exist and application shall report to
standard error and return an error status code.
"""
import os
import stat
import datetime
import sys


def folder_parser(folder):

    for elem in os.listdir(folder):
        filee = folder + elem
        print """%s file permissions: \n\
                exists - %s,\n\
                readeble - %s,\n\
                writeble - %s,\n\
                executible - %s""" % \
            (elem, os.access(filee, os.R_OK), os.access(filee, os.W_OK),
             os.access(filee, os.F_OK), os.access(filee, os.X_OK))
        if os.stat(filee).st_uid == 0:
            print '%s owner - root' % elem
        print 'Last modified on %s'\
            % datetime.datetime.fromtimestamp(int(os.stat(filee).st_mtime))
        print '-' * 80

if len(sys.argv) == 2 and os.path.exists(sys.argv[1]) is True:
    folder_parser(str(sys.argv[1]))
elif len(sys.argv) == 0:
    folder_parser(os.path.dirname(os.path.realpath(__file__)))
elif os.path.exists(sys.argv[1]) is False:
    raise NameError('Directory doesn\'t exist')
elif len(sys.argv) > 2:
    raise NameError('More arguments than needed')
else:
    raise NameError('Some error')
