# Putting it together, a vitual projectile firing thing

import logging
from collections import namedtuple
import tuples

_p = namedtuple('Projectile', ['position', 'velocity'])
_w = namedtuple('World', ['gravity', 'wind'])

def Projectile(position, velocity):
    """
    position is a point, velocity is a vector)
    """
    return _p(position, velocity)


def World(gravity, wind):
    """
    gravity is a vector, wind is a vector
    """
    return _w(gravity, wind)


def tick(world, p):
    """ 
    p is a projectile, which is a point that has a velocity
    world has, among other things, gravity,
      which is a vector
    """
    position = tuples.t_add(p.position, p.velocity)
    velocity = tuples.t_add(p.velocity, tuples.t_add(world.gravity,  world.wind))
    return Projectile(position, velocity)


def tryit(world, p):
    while True:
        print(f"Position is {p.position}")
        if p.position.y <= 0.0:
            break
        p = tick(world, p)

    

    
