Feature: A tuple 2 different ways gives us either a point or a vector

  Scenario: A tuple with w=1.0 is a point
    Given a is a tuple of "4.3", "-4.2", "3.1", "1.0"
    Then a.x = 4.3
     And a.y = -4.2
     And a.z = 3.1
     And a.w = 1.0
     And a is a point
     And a is not a vector

  Scenario: A tuple with w=0 is a vector
    Given b is a tuple of "4.3", "-4.2", "3.1", "0.0"
    Then b.x = 4.3
     And b.y = -4.2
     And b.z = 3.1
     And b.w = 0.0
     And b is not a point
     And b is a vector


  Scenario: 'Point' describes tuples with w=1
    Given p is a Point of "4.0", "-4.0", "3.0"
    Then p = tuple "4.0", "-4.0", "3.0", "1.0"

  Scenario: 'Vector' describes tuples with w=0
    Given v is a Vector of "4.0", "-4.0", "3.0"
    Then v = tuple "4.0", "-4.0", "3.0", "0.0"

  Scenario: Adding two tuples
    Given a1 is a tuple of "3.0", "-2.0", "5.0", "1.0"
      And a2 is a tuple of "-2.0", "3.0", "1.0", "0.0"
     Then a1 + a2 is a tuple of "1.0", "1.0", "6.0", "1.0"


  Scenario: Subtracting two points
    Given p1 is a Point of "3.0", "2.0", "1.0"
      And p2 is a point of "5.0", "6.0", "7.0"
     Then p1 - p2 == vector("-2.0", "-4.0", "-6.0")


  Scenario: Subtracting a vector from a point
    Given p is a point("3.0", "2.0", "1.0")
      And v is a vector("5.0", "6.0", "7.0")
     Then p - v == point("-2.0", "-4.0", "-6.0")


 Scenario: Subtracting two vectors
    Given v1 is a vector("3.0", "2.0", "1.0")
      And v2 is a vector("5.0", "6.0", "7.0")
     Then v1 - v2 == vector("-2.0", "-4.0", "-6.0")


 Scenario: Subtracting a vector from the zero vector
    Given zero is a vector("0.0", "0.0", "0.0")
      And v is a vector("1.0", "-2.0", "3.0")
     Then zero - v == vector("-1.0", "2.0", "-3.0")


 Scenario: Negating a tuple
    Given a is a tuple("1.0", "-2.0", "3.0", "-4.0")
     Then -a == tuple("-1.0", "2.0", "-3.0", "4.0")


 Scenario: Multipying a tuple by a scalar
    Given a is a tuple("1.0", "-2.0", "3.0", "-4.0")
     Then a * 3.5 == tuple(3.5, -7.0, 10.5, -14.0)


 Scenario: Multiplying a tuple by a fraction
    Given b is a tuple(1.0, -2.0, 3.0, -4.0)
     Then b * 0.5 == tuple(0.5, -1.0, 1.5, -2.0)


 Scenario: Dividing a tuple by a scalar
    Given d is a tuple(1.0, -2.0, 3.0, -4.0)
     Then d / 2.0 == tuple(0.5, -1.0, 1.5, -2.0)


# Tests for magnitude of vectors
 Scenario: Magnitude of vector(1.0, 0.0, 0.0)
   Given v1 is a vector(1.0, 0.0, 0.0)
   Then magnitude(v1) == 1.0

 Scenario: Magnitude of vector(0.0, 1.0, 0.0)
   Given v2 is a vector(0.0, 1.0, 0.0)
   Then magnitude(v2) == 1.0

 Scenario: Magnitude of vector(0.0, 0.0, 1.0)
   Given v3 is a vector(0.0, 0.0, 1.0)
   Then magnitude(v3) == 1.0


# >>> math.sqrt(14)
# 3.7416573867739413

 Scenario: Magnitude of vector(1.0, 2.0, 3.0)
   Given v4 is a vector(1.0, 2.0, 3.0)
   Then magnitude(v4) == 3.7416573867739413

 Scenario: Magnitude of vector(-1.0, -2.0, -3.0)
   Given v5 is a vector(1.0, 2.0, 3.0)
   Then magnitude(v5) == 3.7416573867739413

# Normalization

 Scenario: Normalizing vector(4.0, 0.0, 0.0) gives (1.0, 0.0, 0.0)
   Given v1 is a vector(4.0, 0.0, 0.0)
   Then normalize(v1) == approximately vector(1.0, 0.0, 0.0)

 Scenario: Normalizing vector(1.0, 2.0, 3.0)
   Given v2 is a vector(1.0, 2.0, 3.0)
   Then normalize(v2) == approximately vector(0.26726, 0.53452, 0.80178)
  # approximately 1/sqrt(14), 2/sqrt(14), 3/sqrt(14)
   
 Scenario: The magnitude of a normalized vector
  Given v3 is a vector(1.0, 2.0, 3.0)
  When norm is normalize(v3)
  Then magnitude(norm) == 1.0


 Scenario: The dot product of two tuples
   Given a is a vector(1.0, 2.0, 3.0)
   And b is a vector(2.0, 3.0, 4.0)
   Then dot(a, b) == 20.0


 Scenario: The cross product of two tuples
   Given a is a vector(1.0, 2.0, 3.0)
   And b is a vector(2.0, 3.0, 4.0)
   Then cross(a, b) == vector(-1.0, 2.0, -1.0)
   And cross(b, a) == vector(1.0, -2.0, 1.0)


# Color tuples now

 Scenario: Colors are (red, green, blue) tuples
   Given c is a color(-0.5, 0.4, 1.7)
   Then c.red == -0.5
   And c.green == 0.4
   And c.blue == 1.7


 Scenario: Adding Colors
   Given c1 is a color(0.9, 0.6, 0.75)
   And c2 is a color(0.7, 0.1, 0.25)
   Then c1 + c2 == color(1.6, 0.7, 1.0)

 Scenario: Subtracting Colors
   Given c1 is a color(0.9, 0.6, 0.75)
   And c2 is a color(0.7, 0.1, 0.25)
   Then c1 - c2 == color(0.2, 0.5, 0.5)

 Scenario: Multiplying a colors by a scalar
   Given c1 is a color(0.2, 0.3, 0.4)
   Then c1 * 2.0 == color(0.4, 0.6, 0.8)

 Scenario: Multiplying colors
   Given c1 = color(1.0, 0.2, 0.4)
   And c2 = color(0.9, 1.0, 0.1)
   Then c1 * c2 == color(0.9, 0.2, 0.04)




