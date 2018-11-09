import itertools
import tuples
import canvas

@given('c = canvas({h:d}, {w:d})')
def step_impl(context, h, w):
    context.c = canvas.Canvas(h, w)

@then('c.width == {width:d}')
def step_impl(context, width):
    assert context.c.width == width

@then('c.height == {height:d}')
def step_impl(context, height):
    assert context.c.height == height
    
@then('every pixel of c is color({r:d}, {g:d}, {b:d})')
def step_impl(context, r, g, b):
    every_pixel = tuples.Color(r, g, b)
    assert False not in [
        tuples.t_eq(every_pixel, this_pixel) for this_pixel in
        itertools.chain(*context.c.pixels)]
    
 
@given('c = canvas({width:d}, {height:d})')
def step_impl(context, width, height):
    context.c = canvas.Canvas(width, height)

@given('red = color({r:f}, {g:f}, {b:f})')
def step_impl(context, r, g, b):
    context.red = tuples.Color(r, g, b)

@when('write_pixel({can:w}, {h:d}, {w:d}, {color:w})')
def step_impl(context, can, h, w, color):
    canvas.write_pixel(getattr(context, can), h, w, getattr(context, color))

@then('pixel_at({can:w}, {h:d}, {w:d}) == {color:w}')
def step_impl(context, can, h, w, color):
    assert canvas.pixel_at(getattr(context, can), h, w) == getattr(context, color)


@given('c = canvas({width:d}, {height:d})')
def step_impl(context, width, height):
    context.c = canvas.Canvas(width, height)

@when('ppm = canvas_to_ppm(c)')
def step_impl(context):
    context.ppm = list(canvas.canvas_to_ppm(context.c))

@then('lines 1-3 of ppm are')
def step_impl(context):
    print(f'{"".join(context.ppm[0:3])}')
    print(f'{context.text}')
    assert "".join(context.ppm[0:3]) == context.text    
     
