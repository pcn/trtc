from behave import given, when, then, step

import tuples
import util

"""
Copy the below with `C-c a y w` (or M-x aya-create) to get an
auto-yasnippet of a test given with vectors/points/tuples
@given('v is a vector("{x:f}", "{y:f}", "{z:f}")')
def step_impl(context, x, y, z):
    context.v = tuples.Vector(x, y, z)
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
