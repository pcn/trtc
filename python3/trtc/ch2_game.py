#!/usr/bin/env python

from tuples import Point, Vector, normalize
from ch1_game import Projectile, World, tick

def tryit():
    start = Point(0, 1, 0)
    velocity = normalize(Vector(1, 1.8, 0)) * 11.25
    p = Projectile(start, velocity)
    
    gravity = Vector(0, -0.1, 0)
    wind = Vector(-0.1, 0, 0)
    w = World(gravity, wind)
    
    c = Canvas(900, 550)
    
    while True:
        if p.position.y <= 0.0:
            break
        p = tick(w, p)
        print p
    
