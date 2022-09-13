"""
Summary.

    Local Filesytem Operations

Module Functions:
    - clear_directory:  Cleans all file objects from a directory on local
                        filesystem given as a parameter.

"""
import os
from shutil import rmtree
from libtools import logger

logger.info('filesystem_ops.py:  logger working')


def clear_directory(directory):
    """
        Clear contents of fs directory provided as parameter.
        Will not alter directory name or objects external to
        directory given as a parameter.

    Returns:
        TYPE:  Boolean, Success || Failure
    """
    try:
        for x in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, x)):
                print('Removing directory %s' % x)
                rmtree(os.path.join(directory, x))
            elif os.path.isfile(os.path.join(directory, x)):
                print('Removing file %s' % x)
                os.remove(os.path.join(directory, x))
    except Exception:
        #logger.warning('%s Directory not found.  Error code %s' % x, sys.exit(exit_codes['E_MISC']['Code']))
        logger.warning('Directory object not found.')
        return False
    return True
