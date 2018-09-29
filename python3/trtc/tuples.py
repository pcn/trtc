import logging

from collections import namedtuple
import util

_p = namedtuple('Point', ['x', 'y', 'z', 'w'])
_v = namedtuple('Vector', ['x', 'y', 'z', 'w'])

def Point(x, y, z):
    return _p(x, y, z, 1.0)


def Vector(x, y, z):
    return _v(x, y, z, 0.0)


def t_add(t1, t2):
    """This function can raise an IndexError or a TypeError Both arguments
    should be tuples that conform to being either a vector or a point.
    If both are points, a TypeError is raised.  
    """
    if t1[3] + t2[3] > 1 or t1[3] + t2[3] < 0:
        raise TypeError(f"Can't add two points, or arbitrary tuples: ({t1}, {t2})")
    if t1[3] + t2[3] == 1:
        return Point(t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])
    elif t1[3] + t2[3] == 0:
        return Vector(t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])
    else:
        raise TypeError(f"Something with an incorrect value made it here: {t1} {t2}")
    
def t_sub(t1, t2):
    """This function can raise an IndexError or a TypeError Both arguments
    should be tuples that conform to being either a vector or a point.
    If both are points, a TypeError is raised.  
    """
    return (t1[0] - t2[0], t1[1] - t2[1], t1[2] - t2[2], t1[3] - t2[3])
    
def t_eq(t1, t2):
    """Test if two tuples are equal as defined by util.eq()"""
    condition = (
            util.eq(t1[0], t2[0]),
            util.eq(t1[1], t2[1]),
            util.eq(t1[2], t2[2]),
            util.eq(t1[3], t2[3]))
    logging.debug(f"t1 is {t1}")
    logging.debug(f"t2 is {t2}")
    logging.debug(f"Condition is {condition}")
    logging.debug("FOO")
    return False not in condition

    
