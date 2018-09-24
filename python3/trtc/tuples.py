from collections import namedtuple

p = namedtuple('Point', ['x', 'y', 'z', 'w'])
v = namedtuple('Vector', ['x', 'y', 'z', 'w'])

def Point(x, y, z):
    return p(x, y, z, 1.0)


def Vector(x, y, z):
    return v(x, y, z, 0.0)


def tuple_add(t1, t2):
    """This function can raise an IndexError or a TypeError Both arguments
    should be tuples that conform to being either a vector or a point.
    If both are points, a TypeError is raised.  
    """
    if t1[3] + t2[3] == 2:
        raise TypeError(f"Can't add two points: ({t1}, {t2})")
    return (t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2], t1[3] + t1[3])
    
