# maze 2020 custom print library

import sys
import datetime
import builtins

orig_stdout = None
log = None

def start():
    global orig_stdout
    global log
    orig_stdout = sys.stdout  # safe standard out
    log = open('log.txt', 'w')  # open logfile
    sys.stdout = log  # set new standard out to logfile

    println = builtins.print  # safe old print

    def print(*args, **kwargs):  # define own print method with timestamps
        builtins.print(str(datetime.datetime.now()).split('.')[0], end=": ")  # set timestamp in front of every print
        builtins.print(*args, **kwargs)  # normal print afterwards

def stop():
    global orig_stdout
    global log
    sys.stdout = orig_stdout
    log.close()
