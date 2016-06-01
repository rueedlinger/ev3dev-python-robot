# ev3dev python robot API
This project contains a simple python robot API for the EV3 intelligent brick. The API uses 
the [ev3dev](http://www.ev3dev.org/) python module. You can use these examples to get started with 
your ev3dev powered self driving robot.




## Get started
In the following code snippet you can see how to use the ev3robot module. Feel free to change and adapted the code to 
your needs to compete in the robot challenges.

```python

from ev3dev.auto import *

import ev3robot.logic as logic
import ev3robot.robot as r

if __name__ == "__main__":

    class ExplorerController(logic.Controller):

        def loop(self):
            self.max_speed()
            self.forward()
            if self.has_obstacle():
                self.normal_speed()
                self.turn()

    controller = ExplorerController(right_motor=LargeMotor('outA'), left_motor=LargeMotor('outB'),
                                    gyro=GyroSensor(), ultrasonic=UltrasonicSensor())

    robot = r.Robot(controller)
    robot.start()

    try:
        # wait for input
        name = raw_input("Press Enter to exit: ")
    except (KeyboardInterrupt, SystemExit):
        pass

    # stop robot
    robot.kill()

   
```

## The API
The API contains the following classes:
- __controller__ - the main API to control the self driving robot.
- __robot__ - The robot class is responsible for starting the main logic of the robot in an new thread
- __strategy_XYZ__ - your own class which inherits from the controller class and implements the _loop_ method.

### Class controller

- __init__(right_motor, left_motor, gyro, ultrasonic, color=None):
- max_speed
- slow_speed
- normal_speed
- set_speed(speed)
- brake
- angle
- color
- distance
- has_obstacle(range=100)
- backward
- forward
- turn(degree=90)

### Class robot
- __init__(self, strategy, timeout=0.1):
- run
- kill


## Example code
For more code examples have a look at the [examples](examples) directory.
