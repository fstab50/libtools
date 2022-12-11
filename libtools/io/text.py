"""
Summary.

    Text file object detection using Linux binary dependency

Use:

    Not working
"""
from shutil import which
from libtools import logger

"""
THIS SHIT WORKS IN REPL, BUT NOT WHEN INCLU WITH LIBTOOLS.  WTF
"""

def is_text(path):
    """
        Checks filesystem object using *nix file application provided
        with most modern Unix and Linux systems.  Returns False if
        file object cannot be read

    Args:
        :path (str): filesystem path ending in a file object
            Example:  '/usr/bin/python3.6' or '/home/joeuser/image.png'

    Returns:
        - True || False, TYPE: bool
        - Returns None if os binary dependency ('file' program) not found

    """
    if not which('file'):
        logger.warning('required dependency missing: Unix application "file". Exit')
        return None

    try:
        abspath = path if path.startswith('/') else os.path.join(os.getcwd(), path)
        print(f'\nabspath is: {abspath}\n')

        f = os.popen('file -bi ' + abspath, 'r')
        contents = f.read().strip()

    except Exception:
        return False
    return contents.startswith('text')
