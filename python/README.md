# Robot challenges (ev3dev python code)

The following ev3dev python examples will give you good start for
a simple autonomous driving robot. The examples in this project are for different robot challenges like:

- hide and seek
- robot sumo
- follow a line
- avoid obstacles (or simple maze runner)


## Get started
All the code examples are based on the ev3dev python module and you can use these examples to get started quickly 
with a simple ev3 robot. To get started you can use the *ev3robot* python module. This module is a abstraction for a simple 
autonomous driving robot. This module contains simple 
commands like turn, forward, backward, brake, etc.

The following code snippets shows how you can use the ev3robot module. Feel free to change and adapted the code to 
your needs to compete in the challenges.

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