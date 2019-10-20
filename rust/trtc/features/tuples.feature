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

  #  I don't think these two scenarios make sense with
  #  what I'm doing in rustlang
  Scenario: "Point" describes a tuple with type "trtc::tuples::Point" and w=1
    Given p = point(4.0, -4.0, 3)
    Then p == tuple(4, -4, 3, 1)


  Scenario: "vector" describes tuples with w=0
    Given v = vector (4, -4, 3)
    Then v == tuple(4, -4, 3, 0)


  Scenario: Adding two tuples
    Given a1 <- point(3, -2, 5)
    And a2 <- vector(-2, 3, 1)
    Then a1 + a2 == point(1, 1, 6)
