# Post load cell test library

The library is the design to post process data from a load cell and output significant data

## Tests

- Endurance test

### Endurance test

The endurance test is designed to find the critical force and the anaerobic capacity or W' as impulse. Critical force shows the force at which the athlete can produce for an infinite amount of time (theoretically). The anaerobic capacity is the amount force that the athlete can produce above the critical force

The test is done by using a load force and with one arm doing 7 seconds on and 3 seconds off for 4 minutes.

There is an example test by running `test/long_endurance.py`. This will output max force, critical force and anaerobic capacity