# Post load cell test library

The library is the design to post process data from a load cell and output significant data

## Index

- [Test]()
    - [General body strenght]()
    - [Max pull up at 120 deg]()
    - [Max 20mm pull]()
    - [DSI at 200ms]()
    - [Speed pull up @60%]()
    - [Critical force]()
- [Todo list]()

# Test

## Endurance test

The endurance test is designed to find the critical force and the anaerobic capacity or W' as impulse. Critical force shows the force at which the athlete can produce for an infinite amount of time (theoretically). The anaerobic capacity is the amount force that the athlete can produce above the critical force

The test is done by using a load force and with one arm doing 7 seconds on and 3 seconds off for 4 minutes.

There is an example test by running `test/long_endurance.py`. This will output max force, critical force and anaerobic capacity.

# Todo list:

- [ ] Endurance test
    - [x] Create a class that will encapsulate the test output per hand
    - [x] Create a test file to test class
        - [ ] Output in a table format
    - [ ] Build a CI for regression test
    - [ ] Compare results with peer-review papers and estimate test

- [ ] Rate of force development