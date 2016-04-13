# Robot challenges (ev3dev python code)

The following ev3dev python examples will give you good start for
a simple autonomous driving robot. The examples in this project are for different robot challenges like:

- hide and seek
- robot sumo
- follow a line
- avoid obstacles (or simple maze runner)


## Get started
All the code examples are based on a simple abtsratcion framework for ev3dev. You can use these examples to get started quickly. 
We provide you in this project the *ev3robot* python module. This module is a simple abstraction for a  simple 
autonomous driving robot. This module contains simple
commands like turn, forward, backward, brake, etc.

```python

    from ev3dev.auto import *

    import python.ev3robot.logic as logic
    from python import ev3robot as r

    class ExplorerController(logic.Controller):

        def stop(self):
            self.brake()

        def loop(self):
            self.max_speed()
            self.forward()
            if self.has_obstacle():
                self.normal_speed()
                self.turn()

    controller = ExplorerController(LargeMotor('outA'), LargeMotor('outB'), GyroSensor(), UltrasonicSensor())

    robot = r.Robot(controller)
    robot.start()
```

## Example code

So there are the following basic robot examples for different challenges:

- *explorer.py* is a python scripts for a simple obstacle avoiding robot.
- ..