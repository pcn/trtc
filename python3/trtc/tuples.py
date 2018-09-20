from collections import namedtuple

p = namedtuple('Point', ['x', 'y', 'z', 'w'])
v = namedtuple('Vector', ['x', 'y', 'z', 'w'])

def Point(x, y, z):
    return p(x, y, z, 1.0)

    
def Vector(x, y, z):
    return v(x, y, z, 0.0)

