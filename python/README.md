# ev3dev python code

This are the ev3dev python examples which gives you a basic abstraction for
a driving robot. The examples are for different challenges.

The *ev3robot* module is a simple abstraction for a baisc robot. This module conatins simple
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

So there are the following basic robot examples for different challenges:

- *explorer.py* is a python scripts for a simple obstacle avoiding robot.
- ..