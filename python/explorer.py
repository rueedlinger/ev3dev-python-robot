#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        # stop robot
        robot.kill()






