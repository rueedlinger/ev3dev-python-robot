# Python

The following examples will give you good start for a simple autonomous driving robot with the python ev3dev module. 
The code examples in this project are for different robot challenges like:

- hide and seek
- robot sumo
- follow a line
- avoid obstacles (or simple maze runner)


## Get started
You can use these examples to get started  with a simple ev3 robot. In this project we build the *ev3robot* python module. 
This module is a simple framework to create a autonomous driving robot. The ev3robot framework contains simple 
commands like turn, forward, backward, brake, etc. You can use this command to build your own driving robot.

In the following code snippet you can see how to use the ev3robot module. Feel free to change and adapted the code to 
your needs to compete in the robot challenges.

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

We provide you some of the basic implementation for the following robot challenges:

- *explorer.py* a simple obstacle avoiding robot or simple maze runner.
- ..