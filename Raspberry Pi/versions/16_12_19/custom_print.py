# maze 2020 custom print library

import sys
import datetime
import builtins
import os

orig_stdout = None
log = None


def print(*args, **kwargs):  # define own print method with timestamps
    builtins.print(str(datetime.datetime.now()).split('.')[0] + ': ', *args, **kwargs)  # normal print afterwards


def update_print():
    return print


def start(name):
    global orig_stdout
    global log
    orig_stdout = sys.stdout  # safe standard out
    script_dir = os.path.dirname(__file__)
    file_path = 'logs/log' + name + '.txt'
    log = open(os.path.join(script_dir, file_path), 'w')  # open logfile
    sys.stdout = log  # set new standard out to logfile

    println = builtins.print  # safe old print


def stop():
    global orig_stdout
    global log
    sys.stdout = orig_stdout
    log.close()
