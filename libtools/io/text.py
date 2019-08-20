"""
Summary.

    Binary file object detection

Use:

    After instantiation, class object can be called repeatly without
    re-initialization of static primitives used for detection

    >>> b = BinaryFile()
    >>> b.detect('/home/stacie/result.png')
    >>> True

"""
from libtools import logger


def is_text(path):
    """
        Checks filesystem object using *nix file application provided
        with most modern Unix and Linux systems.  Returns False if
        file object cannot be read

    Returns:
        - True || False, TYPE: bool
        - Returns None if os binary dependency ('file' program) not found

    """
    if not which('file'):
        logger.warning('required dependency missing: Unix application "file". Exit')
        return None

    try:
        # correct for multple file objects in path
        path = ' '.join(path.split()[:3])

        f = os.popen('file -bi ' + path, 'r')
        contents = f.read()
    except Exception:
        return False
    return contents.startswith('text')
