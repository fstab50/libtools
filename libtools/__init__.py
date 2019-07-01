"""
Tools & Utilities Module
"""

import os
from libtools.userinput import bool_convert, bool_assignment, ascii_lowercase
from libtools.userinput import range_test, range_bind, userchoice_mapping
from libtools.time import *
from libtools.usermessage import stdout_message
from libtools.export import export_json_object
from libtools.concurrency import split_list
from libtools.progress import screen_dimensions, progress_meter

# color formatting
from libtools.stdout.colors import Colors
from libtools.stdout.colormap import ColorMap, ColorAttributes

# logging
from libtools import logd
from libtools._version import __version__ as version


__author__ = 'Blake Huber'
__version__ = version
__credits__ = []
__license__ = "GPL-3.0"
__maintainer__ = "Blake Huber"
__email__ = "blakeca00@gmail.com"
__status__ = "Development"


try:

    # Linux
    from libtools.oscodes_unix import exit_codes

except Exception:
    # windows
    from libtools.oscodes_win import exit_codes


## the following imports require __version__  ##

from libtools import logd

# shared, global logger object
logger = logd.getLogger(__version__)
