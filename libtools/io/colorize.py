#!/usr/bin/env python3


import os
import sys
import subprocess
from shutil import which
from libtools import stdout_message

"""
def colorize(file):
    cmd = which('pygmentize') + ' ' + str(file)
    print(subprocess.getoutput(cmd))
    return


target = sys.argv[1]

if target.endswith('.html'):
    print(colorize(target))
else:
    colorize(target)

sys.exit(0)

"""


def colorize():
    def execute(file):
        cmd = which('pygmentize') + ' ' + str(file)
        print(subprocess.getoutput(cmd))
        return True

    try:
        target = sys.argv[1]

        if target.endswith('.html'):
            print(execute(target))
        else:
            execute(target)

    except IndexError:
        stdout_message('You must provide filename of a code artifact when calling colorize', 'WARN')
        pass
    return
