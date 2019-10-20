// #![feature(core_intrinsics)]  // for type_of
extern crate cucumber;
extern crate typename;
use cucumber::{cucumber, steps, before, after};
use typename::TypeName;

extern crate trtc;
use trtc::tuples::{Point, Vector};
use trtc::tuples::point;
use trtc::tuples::vector;

#[derive(TypeName)]    
pub struct MyWorld {
    // this struct contains mutable context
    apoint: trtc::tuples::Point,
    bvec: trtc::tuples::Vector,
}

impl cucumber::World for MyWorld {}
impl std::default::Default for MyWorld {
    fn default() -> MyWorld {
        // This function is called every time a scenario is  started
        MyWorld {
            apoint: trtc::tuples::Point{ ..Default::default() },
            bvec: trtc::tuples::Vector{ ..Default::default() }
        }
    }
}


// fn type_of<T>(_: &T) -> &'static str {
    // unsafe { std::intrinsics::type_name::<T>() }
// }

mod tuples_steps {
    // Any type that implements cucumber_rust::World + Default can be the world
    use cucumber::steps;
    use typename::TypeName;
    // use trtc::tuples::Point;
    steps!(::MyWorld => {
        // Scenario: A tuple with w=1 is a point
        given regex r#"a is a tuple of ([-0-9.]+), ([-0-9.]+), ([-0-9.]+), ([-0-9.]+)"# (f64, f64, f64, i8) | world, x, y , z, w, step| {
            world.apoint = trtc::tuples::Point{x: x, y: y, z: z, w: w}
        };
        then regex r#"a.x = ([-0-9.]+)"# (f64) | world, x, step| {
            assert_eq!(world.apoint.x, x)
        };
        then regex r#"a.y = ([-0-9.]+)"# (f64) | world, y, step| {
            assert_eq!(world.apoint.y, y)
        };
        then regex r#"a.z = ([-0-9.]+)"# (f64) | world, z, step| {
            assert_eq!(world.apoint.z, z)
        };
        then regex r#"a.w = ([-0-9.]+)"# (i8) | world, w, step| {
            assert_eq!(world.apoint.w,  w)
        };
        then r#"a is a point"# | world, step| {
            // assert_eq!(::type_of(&world.a), "trtc::tuples::Point")
            assert_eq!(world.apoint.type_name_of(), "trtc::tuples::Point")
        };
        then r#"a is not a vector"# | world, step| {
            // assert!(::type_of(&world.a) != "trtc::tuples::Vector")
            assert!(world.apoint.type_name_of() != "trtc::tuples::Vector")
        };

        // Scenario: A tuple with w=0 is a vector
        given regex r#"b is a tuple of ([-0-9.]+), ([-0-9.]+), ([-0-9.]+), ([-0-9.]+)"# (f64, f64, f64, i8) | world, x, y , z, w, step| {
            world.bvec = trtc::tuples::Vector{x: x, y: y, z: z, w: w}
        };
        then regex r#"b.x = ([-0-9.]+)"# (f64) | world, x, step| {
            assert_eq!(world.bvec.x, x)
        };
        then regex r#"b.y = ([-0-9.]+)"# (f64) | world, y, step| {
            assert_eq!(world.bvec.y, y)
        };
        then regex r#"b.z = ([-0-9.]+)"# (f64) | world, z, step| {
            assert_eq!(world.bvec.z, z)
        };
        then regex r#"b.w = ([-0-9.]+)"# (i8) | world, w, step| {
            assert_eq!(world.bvec.w,  w)
        };
        then r#"b is a vector"# | world, step| {
            // assert_eq!(::type_of(&world.b), "trtc::tuples::Vector")
            assert_eq!(world.bvec.type_name_of(), "trtc::tuples::Vector")
        };
        then r#"b is not a point"# | world, step| {
            // assert!(::type_of(&world.b) != "trtc::tuples::Point")
            assert!(world.bvec.type_name_of() != "trtc::tuples::Point")
        };

        // Scenario: "Point" describes tuples with w=1
        // given regex r#""Point" describes a tuple with type ([A-Za-z0-9:]+)"# (str) | world, t_type, step| {
        //     assert!(world.a.type_name_of() == trtc::tuples::Vector{x: x, y: y, z: z, w: w})
        // };

        given regex r#"p = point\(([\-0-9.]+), ([\-0-9.]+), ([\-0-9.]+)\)"# (f64, f64, f64) | world, x, y, z, step| {
            world.apoint = trtc::tuples::point(x, y, z)
        };

        //   Scenario: Adding two tuples
        given regex r#"a1 <- point\(([\-0-9.]+), ([\-0-9.]+), ([\-0-9.]+)\)"# (f64, f64, f64) | world, x, y, z, step | {
            world.apoint = trtc::tuples::point(x, y, z)
        };

        given regex r#"a2 <- vector\(
([\-0-9.]+), ([\-0-9.]+), ([\-0-9.]+)\)"# (f64, f64, f64) | world, x, y, z, step | {
            world.bvec = trtc::tuples::vector(x, y, z)
        };

        then r#"a1 + a2 == point\(([\-0-9.]+), ([\-0-9.]+), ([\-0-9.]+)\)"# (f64, f64, f64) | world, x, y, z, step| {
        // then r#"a1 + a2 == point(1, 1, 6)"# | world, step | {
            // let x = 1.0;
            // let y = 1.0;
            // let z = 6.0;
            // XXX: Need to pass the reference to add. OK, ergonomically awwwwkard
            assert!((&world.apoint + &world.bvec) == trtc::tuples::point(x, y, z))
        };
    });
}


cucumber! {
    features: "./features", // Path to our feature files
    world: ::MyWorld, // The world needs to be the same for steps and the main cucumber call
    steps: &[
        tuples_steps::steps // the `steps!` macro creates a `steps` function in a module
    ]
    // setup: setup, // Optional; called once before everything
    // before: &[
    //     a_before_fn // Optional; called before each scenario
    // ], 
    // after: &[
    //     an_after_fn // Optional; called after each scenario
    // ls] 
}    
