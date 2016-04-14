#!/usr/bin/python
# -*- coding: utf-8 -*-

from ev3dev.auto import *

import ev3robot.logic as logic
import ev3robot.robot as r

import time

if __name__ == "__main__":

    class SumoController(logic.Controller):

        def setup(self):
            self.ptc_color = self.color()

        def loop(self):
            self.normal_speed()
            self.turn(degree=90)
            self.brake()

            if self.has_obstacle(range=200):
                self.forward()
            else:
                self.brake()
                self.turn(degree=10)

            # 0 black -> 100 white
            if self.color() + 10 < self.ptc_color:
                self.turn(degree=90)
                self.forward()
                # drive for 1 sec
                time.sleep(1)



    controller = SumoController(right_motor=LargeMotor('outA'), left_motor=LargeMotor('outB'),
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