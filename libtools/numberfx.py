"""
Summary:
    - Number manipulation functionality (float, int)
    - Python3

Module Functions:
    - range_bind:  Returns an intger value between a floor and ceiling

Classes:
    - None

"""
import inspect
from libtools import logger


def range_bind(x, minx, maxx):
    """
        Bind an integer or floating point number (x) to min, max range

    Args:
        :x (int or float): Value to bind to a min, max range
        :minx (int): Minimum range (floor) value
        :maxx (int): Maximum range (ceiling) value

    Returns:
        value in range(minx, maxx), TYPE: int

    """
    bind = lambda x, minx, maxx: max(min(maxx, round(x)), minx)
    return bind(x, minx, maxx)
