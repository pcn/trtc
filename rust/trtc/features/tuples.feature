Feature: A tuple 2 different ways gives us either a point or a vector
  Scenario: A tuple with w=1 is a point
    Given a is a tuple of 4.3, -4.2, 3.1, 1
    Then a.x = 4.3
     And a.y = -4.2
     And a.z = 3.1
     And a.w = 1
     And a is a point
     And a is not a vector

  Scenario: A tuple with w=0 is a vector
    Given b is a tuple of 4.3, -4.2, 3.1, 0
    Then b.x = 4.3
     And b.y = -4.2
     And b.z = 3.1
     And b.w = 0
     And b is a vector
     And b is not a point

  # #  I don't think these two scenarios make sense with
  # #  what I'm doing in rustlang
  # Scenario: Point describes a tuple with type trtc::tuples::Point and w=1
  #   Given p = point(4.0, -4.0, 3)
  #   Then p == tuple(4, -4, 3, 1)

  # Scenario: "vector" describes tuples with w=0
  #   Given v = vector (4, -4, 3)
  #   Then v == tuple(4, -4, 3, 0)


  Scenario: Adding two tuples - one point and one vector
    Given a1 <- point(3, -2, 5)
    And a2 <- vector(-2, 3, 1)
    Then a1 + a2 == point(1, 1, 6)

  Scenario: Subtracting two points
    Given p1 <- point(3, 2, 1)
    And p2 <- point(5, 6, 7)
    Then p1 - p2 == vector(-2, -4, -6)

  Scenario: Subtacting a vector from a point
    Given p <- point(3, 2, 1)
    And v <- vector(5, 6, 7)
    Then p - v == point(-2, -4, -6) 

  Scenario: Subtacting two vectors
    Given v1 <- vector(3, 2, 1)
    And v2 <- vector(5, 6, 7)
    Then v1 - v2 == vector(-2, -4, -6) 

  Scenario: Subracting a vector from the zero vector
    Given zero <- vector(0, 0, 0)
    And v_sub <- vector(1, -2, 3)
    Then zero - v == vector(-1, 2, -3)

  # XXX: Is this going to be best handled by having a negation operator for both
  # vectors and points, or is there a reason to do something like convert to a tuple here?
  # Scenario: Negating a tuple
  #   Given a <- vector(1, -2, 3
