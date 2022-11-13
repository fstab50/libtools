#!/usr/bin/env python3


import os
import sys
import subprocess
from shutil import which
from libtools import stdout_message

"""
Command-line Utility to generate colored syntax highlighting of any
filesystem code artifact provided as a parameter.

Use:
    $  colorize myprogram.sh
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
