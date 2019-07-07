"""
Summary:
    - Timer class for measuring duration
    - Python3

Module Functions:
    - None

Classes:
    - TimeDuration

"""
import time
import inspect
from libtools import logger


class TimeDuration():
    """Timer class; accuracy to 100th of a second"""
    def __init__(self, accuracy=2):
        self.start_time = None
        self.end_time = None
        self.precision = accuracy

    def start(self):
        self.start_time = time.time()
        return self.start_time

    def __repr__(self):
        return time.strftime('%H:%M:%S', time.localtime(self.start_time))

    def end(self):
        try:
            duration = time.time() - self.start_time
        except Exception as e:
            logger.exception(
                '%s: Unknown error when calculating end time (Code: %s)' %
                (inspect.stack()[0][3], str(e)))
            return 0.00
        return round(duration, self.precision)
