from behave import given, when, then, step

import tuples

@given('a is a tuple of "{x}", "{y}", "{z}", "{w}"')
def step_impl(context, x, y, z, w):
    # a == (4.3, -4.2, 3.1, 1.0)
    context.a = tuples.p(x, y, z, w)
    # context.a = a
    return context.a == (4.3, -4.2, 3.1, 1.0)

@then(u'a.x = 4.3')
def step_impl(context):
    return context.a.x == 4.3

@then(u'a.y = -4.2')
def step_impl(context):
    return context.a.y == -4.2


@then(u'a.z = 3.1')
def step_impl(context):
    return context.a.z == 3.1


@then(u'a.w = 1.0')
def step_impl(context):
    return context.a.w == 1.0


@then(u'a is a point')
def step_impl(context):
    type(context.a) == 'Point'    


@then(u'a is not a vector')
def step_impl(context):
    type(context.a) != 'Vector'



@given('b is a tuple of "{x}", "{y}", "{z}", "{w}"')
def step_impl(context, x, y, z, w):
    context.b = tuples.v(4.3, -4.2, 3.1, 0.0)

@then(u'b.x = 4.3')
def step_impl(context):
    return context.b.x == 4.3


@then(u'b.y = -4.2')
def step_impl(context):
    return context.b.y == -4.2    


@then(u'b.z = 3.1')
def step_impl(context):
    return context.b.z == 3.1


@then(u'b.w = 0.0')
def step_impl(context):
    return context.b.w == 0.0


@then(u'b is not a point')
def step_impl(context):
    return type(context.b) != 'Point'


@then(u'b is a vector')
def step_impl(context):
    return type(context.b) == 'Vector'


@given('p is a Point of "{x}", "{y}", "{z}"')
def step_impl(context, x, y, z):
    context.p = tuples.Point(x, y, z)

@then(u'p = tuple "{x}", "{y}", "{z}", "{w}"')
def step_impl(context, x, y, z, w):
    return context.p == (x, y, z, w)


@given('v is a Vector of "{x}", "{y}", "{z}"')
def step_impl(context, x, y, z):
    context.p = tuples.Point(x, y, z)
    return context.p == (x, y, z, 0.0)

@then(u'v = tuple "{x}", "{y}", "{z}", "{w}"')
def step_impl(context, x, y, z, w):
    return context.p == (x, y, z, w)

@given('a1 is a tuple of "{x}", "{y}", "{z}", "{w}"')
def step_impl(context, x, y, z, w):
    context.a1 = (int(x), int(y), int(z), int(w))

@given('a2 is a tuple of "{a}", "{b}", "{c}", "{d}"')
def step_impl(context, a, b, c, d):
    context.a2 = (int(a), int(b), int(c), int(d))

@given(u'a2 is a tuple of "-2", "3, "1", "0"')
def step_impl(context):
    context.a2 = (int(-2), int(3), int(1), int(0))

    
@then('a1 + a2 is a tuple of "{x}", "{y}", "{z}", "{w}"')
def step_impl(context, x, y, z, w):
    return tuples.t_add(context.a1, context.a2) == (x, y, z, w)
    
