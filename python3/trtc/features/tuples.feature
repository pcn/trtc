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
     Then p - v = point("-2.0", "-4.0", "-6.0")