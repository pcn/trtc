#!/usr/bin/env python

from tuples import Point, Vector, normalize, t_mul, Color
from canvas import Canvas, write_pixel, canvas_to_ppm
from ch1_game import Projectile, World, tick
import logging
logging.basicConfig()

def tryit():
    start = Point(0, 1, 0)
    velocity = t_mul(normalize(Vector(1, 1.8, 0)), 11.25)
    p = Projectile(start, velocity)
    
    gravity = Vector(0, -0.1, 0)
    wind = Vector(-0.1, 0, 0)
    w = World(gravity, wind)
    
    c = Canvas(900, 550)
    new_color = Color(1, 1, 1)
    while True:
        projectile_y = c.height - p.position.y
        logging.warning(f"x: {p.position.x}, y: {p.position.y}, projectile_y: {projectile_y}")
        logging.warning(f"width: {c.width}, height: {c.height}")
        write_pixel(c, int(p.position.x), projectile_y, new_color)
        if p.position.y <= 0.0:
            break
        p = tick(w, p)
    print("".join(canvas_to_ppm(c)))
        
tryit()
