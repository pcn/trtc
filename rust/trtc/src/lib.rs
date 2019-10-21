#[macro_use]
extern crate typename;

const EPSILON: f64 = 0.00001;

// A test for "equal enough" for f64 numbers
fn equal(a: f64, b: f64) -> bool {
    f64::abs(a - b) < EPSILON
}

pub mod tuples {
    use std::ops::{Add, Sub};

    #[derive(TypeName, Debug, PartialEq)]
    pub struct Point {
        pub x: f64,
        pub y: f64,
        pub z: f64,
        pub w: i8, // Should this be a 1bit binary instead?
    }

    #[derive(TypeName, Debug, PartialEq)]
    pub struct Vector {
        pub x: f64,
        pub y: f64,
        pub z: f64,
        pub w: i8, // Should this be a 1bit binary instead?
    }

    #[derive(TypeName, Debug, PartialEq)]
    pub struct Tuple {
        pub x: f64,
        pub y: f64,
        pub z: f64,
        pub w: i8, // Should this be a 1bit binary instead?
    }

    trait ToTuple {
        // Can't specialize on struct members, I don't think
        fn to_tuple(&self) -> Tuple;
    }

    pub fn point(x: f64, y: f64, z: f64) -> Point {
        Point {
            x: x,
            y: y,
            z: z,
            w: 1,
        }
    }

    pub fn vector(x: f64, y: f64, z: f64) -> Vector {
        Vector {
            x: x,
            y: y,
            z: z,
            w: 0,
        }
    }

    pub fn tuple(x: f64, y: f64, z: f64, w: i8) -> Tuple {
        Tuple {
            x: x,
            y: y,
            z: z,
            w: w,
        }
    }

    impl Default for Point {
        fn default() -> Point {
            Point {
                x: 0.0,
                y: 0.0,
                z: 0.0,
                w: 1,
            }
        }
    }

    impl ToTuple for Point {
        fn to_tuple(&self) -> Tuple {
            Tuple {
                x: self.x,
                y: self.y,
                z: self.z,
                w: self.w,
            }
        }
    }
    /// Note: a point can't be added to a point, so that should fail
    /// Note: a point subtracted from a point is a vector
    impl Sub<&Point> for &Point {
        type Output = Vector;
        fn sub(self, other: &Point) -> Vector {
            vector(self.x - other.x, self.y - other.y, self.z - other.z)
        }
    }
    impl Sub<&Vector> for &Point {
        type Output = Point;
        fn sub(self, other: &Vector) -> Point {
            point(self.x - other.x, self.y - other.y, self.z - other.z)
        }
    }

    impl Add<&Vector> for &Point {
        type Output = Point;
        fn add(self, other: &Vector) -> Point {
            point(self.x + other.x, self.y + other.y, self.z + other.z)
        }
    }

    impl Default for Vector {
        fn default() -> Vector {
            Vector {
                x: 0.0,
                y: 0.0,
                z: 0.0,
                w: 0,
            }
        }
    }

    impl Add<&Point> for &Vector {
        type Output = Point;
        fn add(self, other: &Point) -> Point {
            point(self.x + other.x, self.y + other.y, self.z + other.z)
        }
    }
    impl Add<&Vector> for &Vector {
        type Output = Vector;
        fn add(self, ref other: &Vector) -> Vector {
            vector(self.x + other.x, self.y + other.y, self.z + other.z)
        }
    }
    impl Sub<&Vector> for &Vector {
        type Output = Vector;
        fn sub(self, other: &Vector) -> Vector {
            vector(self.x - other.x, self.y - other.y, self.z - other.z)
        }
    }

    impl ToTuple for Vector {
        fn to_tuple(&self) -> Tuple {
            Tuple {
                x: self.x,
                y: self.y,
                z: self.z,
                w: self.w,
            }
        }
    }
}
