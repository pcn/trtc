from behave import given, when, then, step

import tuples
import util

"""
Copy the below with `C-c a y w` (or M-x aya-create) to get an
auto-yasnippet of a test given with vectors/points/tuples
@given('v is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.v = tuples.Vector(x, y, z)

@given('~a is a ~tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    context.~a = ~tuple((x, y, z, w))

@given('`a' is a `tuple'({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    context.`a' = `tuple'((x, y, z, w))


"""


@given('a is a tuple of "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
    # a == (4.3, -4.2, 3.1, 1.0)
    context.a = tuples.Point(x, y, z)
    # context.a = a
    # return context.a == (4.3, -4.2, 3.1, 1.0)

@then(u'a.x = 4.3')
def step_impl(context):
    assert util.eq(context.a.x, 4.3)

@then(u'a.y = -4.2')
def step_impl(context):
    assert util.eq(context.a.y, -4.2)


@then(u'a.z = 3.1')
def step_impl(context):
    assert util.eq(context.a.z, 3.1)


@then(u'a.w = 1.0')
def step_impl(context):
    assert util.eq(context.a.w, 1.0)


@then(u'a is a point')
def step_impl(context):
    assert type(context.a) == type(tuples.Point(0,0,0))


@then(u'a is not a vector')
def step_impl(context):
    assert type(context.a) != type(tuples.Vector(0,0,0))



@given('b is a tuple of "{x}", "{y}", "{z}", "{w}"')
def step_impl(context, x, y, z, w):
    context.b = tuples.Vector(4.3, -4.2, 3.1)

@then(u'b.x = 4.3')
def step_impl(context):
    assert util.eq(context.b.x, 4.3)


@then(u'b.y = -4.2')
def step_impl(context):
    assert util.eq(context.b.y, -4.2)


@then(u'b.z = 3.1')
def step_impl(context):
    assert util.eq(context.b.z, 3.1)


@then(u'b.w = 0.0')
def step_impl(context):
    assert util.eq(context.b.w, 0.0)


@then(u'b is not a point')
def step_impl(context):
    assert type(context.b) != type(tuples.Point(0,0,0))


@then(u'b is a vector')
def step_impl(context):
    assert type(context.b) == type(tuples.Vector(0,0,0))


@given('p is a Point of "{x:f}", "{y:f}", "{z:f}"')
def step_impl(context, x, y, z):
    context.p = tuples.Point(x, y, z)

@then(u'p = tuple "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
    assert tuples.t_eq(context.p, (x, y, z, w))


@given('v is a Vector of "{x:f}", "{y:f}", "{z:f}"')
def step_impl(context, x, y, z):
    context.p = tuples.Vector(x, y, z)

@then(u'v = tuple "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
    assert tuples.t_eq(context.p, (x, y, z, w))

@given('a1 is a tuple of "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
    context.a1 = (x, y, z, w)

@given(u'a2 is a tuple of "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
    context.a2 = (x, y, z, w)
    
@then('a1 + a2 is a tuple of "{x:f}", "{y:f}", "{z:f}", "{w:f}"')
def step_impl(context, x, y, z, w):
    result = tuples.t_add(context.a1, context.a2)
    assert tuples.t_eq(result, (x, y, z, w))
    

@given('p1 is a point of "{x:f}", "{y:f}", "{z:f}"')
def step_impl(context, x, y, z):
    context.p1 = tuples.Point(x, y, z)

@given('p2 is a point of "{x:f}", "{y:f}", "{z:f}"')
def step_impl(context, x, y, z):
    context.p2 = tuples.Point(int(x), int(y), int(z))
    
@then('p1 - p2 == vector("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    result = tuples.t_sub(context.p1, context.p2)
    assert tuples.t_eq(result, tuples.Vector(x, y, z))


@given('p is a point("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    context.p = tuples.Point(x, y, z)

@given('v is a vector("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    context.v = tuples.Vector(x, y, z)

@then('p - v == point("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    result = tuples.t_sub(context.p, context.v)
    should_equal = tuples.Point(x, y, z)
    assert(result == should_equal)

    
@given('v1 is a vector("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    context.v1 = tuples.Vector(x, y, z)

@given('v2 is a vector("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    context.v2 = tuples.Vector(x, y, z)

@then('v1 - v2 == vector("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    result = tuples.t_sub(context.v1, context.v2)
    should_equal = tuples.Vector(x, y, z)
    assert(result == should_equal)

@given('zero is a vector("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    context.zero = tuples.Vector(x, y, z)

@given('v is a vector("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    context.v = tuples.Vector(x, y, z)

@then('zero - v == vector("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    result = tuples.t_sub(context.zero, context.v)
    should_equal = tuples.Vector(x, y, z)
    assert(result == should_equal)
    

@given('a is a tuple("{x:f}", "{y:f}", "{z:f}", "{w:f}")')
def step_impl(context, x, y, z, w):
    context.a = (x, y, z, w)
    

@then('-a == tuple("{x:f}", "{y:f}", "{z:f}", "{w:f}")')
def step_impl(context, x, y, z, w):
    assert tuples.t_neg(context.a) == (x, y, z, w)


@given('a is a tuple("{x:f}", "{y:f}", "{z:f}", "{w:f}")')
def step_impl(context, x, y, z, w):
    context.a = tuple(x, y, z, w)

@then('a * {sc:f} == tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, sc, x, y, z, w):
    assert tuples.t_mul(context.a, sc) == tuple([x, y, z, w,])
    

@given('b is a tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    context.b = tuple((x, y, z, w))

@then('b * {sc:f} == tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, sc, x, y, z, w):
    assert tuples.t_mul(context.b, sc) == tuple([x, y, z, w,])
    
    
@given('d is a tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, x, y, z, w):
    context.d = tuple((x, y, z, w))

@then('d / {sc:f} == tuple({x:f}, {y:f}, {z:f}, {w:f})')
def step_impl(context, sc, x, y, z, w):
    assert tuples.t_div(context.d, sc) == tuple((x, y, z, w))
    

# Magnitude of vector tests
@given('v1 is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.v1 = tuples.Vector(x, y, z)
    
@then('magnitude(v1) == {mag:f}')
def step_impl(context, mag):
    assert util.eq(
        tuples.magnitude(context.v1), mag)

@given('v2 is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.v2 = tuples.Vector(x, y, z)

@then('magnitude(v2) == {mag:f}')
def step_impl(context, mag):
    assert util.eq(
        tuples.magnitude(context.v2), mag)


@given('v3 is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.v3 = tuples.Vector(x, y, z)

@then('magnitude(v3) == {mag:f}')
def step_impl(context, mag):
    assert util.eq(
        tuples.magnitude(context.v3), mag)

@given('v4 is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.v4 = tuples.Vector(x, y, z)

@then('magnitude(v4) == {mag:f}')
def step_impl(context, mag):
    assert util.eq(
        tuples.magnitude(context.v4), mag)
    

@given('v5 is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.v5 = tuples.Vector(x, y, z)

@then('magnitude(v5) == {mag:f}')
def step_impl(context, mag):
    assert util.eq(
        tuples.magnitude(context.v5), mag)
    

# Normalizing
@given('v1 is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.v1 = tuples.Vector(x, y, z)

@then('normalize(v1) == approximately vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    assert tuples.t_eq(
        tuples.normalize(context.v1), tuples.Vector(x, y, z))

@given('v2 is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.v2 = tuples.Vector(x, y, z)

@then('normalize(v2) == approximately vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    normalized = tuples.normalize(context.v2)
    print(f"normalized is {normalized}")
    assert tuples.t_eq(
        tuples.normalize(context.v2), tuples.Vector(x, y, z), epsilon=0.00001)
    
    
@given('v3 is a is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.v3 = tuples.Vector(x, y, z)

@when('norm is normalize(v3)')
def step_impl(context):
    context.norm = tuples.normalize(context.v3)

@then('magnitude(norm) == {mag:f}')
def step_impl(context, mag):
    assert util.eq(tuples.magnitude(context.norm), mag)


@given('a is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.a = tuples.Vector(x, y, z)

@given('b is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.b = tuples.Vector(x, y, z)

@then('dot(a, b) == {result:f}')
def step_impl(context, result):
    assert util.eq(tuples.dot(context.a, context.b), result)
    

@given('a is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.a = tuples.Vector(x, y, z)
    
@given('b is a vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.b = tuples.Vector(x, y, z)

    
@then('cross(a, b) == vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    assert tuples.t_eq(
        tuples.cross(context.a, context.b),
        tuples.Vector(x, y, z))

    
@then('cross(b, a) == vector({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    assert tuples.t_eq(
        tuples.cross(context.b, context.a),
        tuples.Vector(x, y, z))

    
@given('c is a color({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.c = tuples.Color(x, y, z)
    
    
@then('c.red == {color:f}')
def step_impl(context, color):
    assert util.eq(context.c.red, color)
    
@then('c.green == {color:f}')
def step_impl(context, color):
    assert util.eq(context.c.green, color)
    
@then('c.blue == {color:f}')
def step_impl(context, color):
    assert util.eq(context.c.blue, color)

# Adding colors
@given('c1 is a color({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.c1 = tuples.Color(x, y, z)

@given('c2 is a color({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.c2 = tuples.Color(x, y, z)

@then('c1 + c2 == color({r:f}, {g:f}, {b:f})')
def step_impl(context, r, g, b):
    assert  tuples.t_eq(
        tuples.t_add(context.c1, context.c2),
        tuples.Color(r, g, b))
        
# Subtracting colors
@given('c1 is a color({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.c1 = tuples.Color(x, y, z)

@given('c2 is a color({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.c2 = tuples.Color(x, y, z)

@then('c1 - c2 == color({r:f}, {g:f}, {b:f})')
def step_impl(context, r, g, b):
    assert  tuples.t_eq(
        tuples.t_sub(context.c1, context.c2),
        tuples.Color(r, g, b))

# multiplying a color by a scalar
@given('c1 is a color({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.c1 = tuples.Color(x, y, z)

@then('c1 * {sc:f} == color({r:f}, {g:f}, {b:f})')
def step_impl(context, sc, r, g, b):
    assert tuples.t_eq(
        tuples.t_mul(context.c1, sc),
        tuples.Color(r, g, b))
    
    
    
    
@given('c1 = color({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.c1 = tuples.Color(x, y, z)

@given('c2 = color({x:f}, {y:f}, {z:f})')
def step_impl(context, x, y, z):
    context.c2 = tuples.Color(x, y, z)

@then('c1 * c2 == color({r:f}, {g:f}, {b:f})')
def step_impl(context, r, g, b):
    assert tuples.t_eq(
        tuples.hadamard_product(context.c1, context.c2),
        tuples.Color(r, g, b))
    
    

