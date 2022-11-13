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

Note:  This module requires that the python pygments module be
       installed as it provides the 'pygmentize' executable
"""


def colorize():
    def execute(file):
        cmd = which('pygmentize') + ' ' + str(file)
        print(subprocess.getoutput(cmd))
        return True

    def help_menu():
        menu = """
        colorize: command-line utility to generate colored syntax highlighting of any
        filesystem code artifact provided as a parameter.

            Use:
                $  colorize myprogram.sh
        """
        print(menu)

    try:
        target = sys.argv[1]

        if target.endswith('.html'):
            print(execute(target))
        else:
            execute(target)

    except IndexError:
        stdout_message('You must provide filename of a code artifact when calling colorize', 'WARN', indent=12)
        help_menu()
        pass
    return
