import logging
import math
from collections import namedtuple
from functools import reduce

import util

_c = namedtuple('Color', ['red', 'green', 'blue'])
_p = namedtuple('Point', ['x', 'y', 'z', 'w'])
_v = namedtuple('Vector', ['x', 'y', 'z', 'w'])

def Color(r, g, b):
    # if float(r) > 1.0 or float(r) < 0.0 \
    #   or float(g) > 1.0 or float(g) < 0.0 \
    #   or float(b) > 1.0 or float(b) < 0.0:
    #     raise ValueError(f"Color values must be between 0.0 and 1.0 vs r: {r} g: {g}: b {b}")
    return _c(float(r), float(g), float(b))

def Point(x, y, z):
    return _p(x, y, z, 1.0)


def Vector(x, y, z):
    return _v(x, y, z, 0.0)


def t_add(t1, t2):
    """This function can raise an IndexError or a TypeError Both arguments
    should be tuples that conform to being either a vector or a point.
    If both are points, a TypeError is raised.  
    """
    # if t1[3] + t2[3] > 1 or t1[3] + t2[3] < 0:
    #     raise TypeError(f"Can't add two points, or arbitrary tuples: ({t1}, {t2})")
    # if t1[3] + t2[3] == 1:
    #     return Point(t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])
    # elif t1[3] + t2[3] == 0:
    #     return Vector(t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])
    # else:
    #     raise TypeError(f"Something with an incorrect value made it here: {t1} {t2}")
    def bare_add():
        return tuple([t1[count] + t2[count] for count in range(len(t1))])
    # Poor man's very problematic polymorphism    
    if type(t1) == type(Vector(0, 0, 0)):
        return _v(*bare_add())
    elif type(t1) == type(Color(0, 0, 0)):
        return _c(*bare_add())
    elif type(t1) == type(Point(0, 0, 0)):
        # print("Adding to a point")
        return Point(*[t1[count] + t2[count] for count in range(len(t1) - 1)])
    else:
        return bare_add()
    
def t_sub(t1, t2):
    """This function can raise an IndexError or a TypeError Both arguments
    should be tuples that conform to being either a vector or a point.
    If both are points, a TypeError is raised.  
    """
    def bare_sub():
        return tuple([t1[count] - t2[count] for count in range(len(t1))])

    # Poor man's very problematic polymorphism
    if type(t1) == type(Vector(0, 0, 0)):
        return _v(*bare_sub())
    elif type(t1) == type(Color(0, 0, 0)):
        return _c(*bare_sub())
    # A point minus a point is a vector
    elif type(t1) == type(Point(0, 0, 0)):
        return _v(*bare_sub())
    else:
        return bare_sub()

    
def t_eq(t1, t2, epsilon=.000001):
    """Test if two tuples are equal as defined by util.eq().  This compares any two 
    tuples where len(t1) <= len(t2)"""
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(f"t1 is {t1}")
    logging.debug(f"t2 is {t2}")
    condition = [
        util.eq(t1[count], t2[count], epsilon=epsilon) for count in range(len(t1))]
    logging.debug(f"Condition is {condition}")
    return False not in condition

    
def t_neg(t1):
    "Negates a tuple"
    val = t_sub((0, 0, 0, 0), t1)
    # Poor man's very problematic polymorphism
    return _poor_poly(val, t1)

def t_mul(t1, sc):
    val = tuple([val * sc for val in t1])    
    # Poor man's very problematic polymorphism
    return _poor_poly(val, t1)

def t_div(t1, sc):
    val = tuple([val / sc for val in t1])
    return _poor_poly(val, t1)

def _poor_poly(val, t1):
    """Multiplication, divsion and negation should
    follow these same rules, so just codify them here.

    Subtraction doesn not, though.
    """
    if type(t1) == type(Vector(0, 0, 0)):
        return Vector(*val[:3])
    elif type(t1) == type(Color(0, 0, 0)):
        return Color(*val)
    elif type(t1) == type(Point(0, 0, 0)):
        return Point(*val[:3])
    else:
        return val


# The magnitude, normalize, and cross and dot products aren't generic to tuples
# they require vectors to make sense.
def magnitude(v):
    """
    Magnitude of the vector is pythagoras' theorem applied to 
    3d
    """
    if v[3] != 0:
        raise TypeError("This isn't a vector, and it doesn't quack like a vector")
    return math.sqrt(
        reduce(lambda x, y: x + y, [v[0]**2, v[1]**2, v[2]**2, v[3]**2]))
    
def normalize(v):
    if v[3] != 0:
        raise TypeError("This isn't a vector, and it doesn't quack like a vector")
    mag = magnitude(v)
    return Vector(v[0]/mag, v[1]/mag, v[2]/mag)

def dot(a, b):
    if a[3] != 0 or b[3] != 0:
        raise TypeError("a or b isn't a vector, and doesn't quack like a vector")
    def dot_it():
        for count, elem in enumerate(a):
            yield elem * b[count]

    return sum(dot_it())

def cross(a, b):
    if a[3] != 0 or b[3] != 0:
        raise TypeError("a or b isn't a vector, and doesn't quack like a vector")
    # This stuff always seems magical
    return Vector(
        (a.y * b.z) - (a.z * b.y),
        (a.z * b.x) - (a.x * b.z),
        (a.x * b.y) - (a.y * b.x))


# Colors
def hadamard_product(c1, c2):
    return Color(
        c1.red * c2.red,
        c1.green * c2.green,
        c1.blue * c2.blue)

                 
