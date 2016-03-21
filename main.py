#!/usr/bin/python
# -*- coding: utf-8 -*-

import ev3robot.robot as r
import ev3robot.logic as logic
#import ev3robot.mock as mock

from ev3dev.auto import *

import time


if __name__ == "__main__":

    class MyController(logic.Controller):

        def stop(self):
            self.brake()

        def loop(self):
            self.max_speed()
            self.forward()
            if self.should_stop():
                self.normal_speed()
                self.turn()



    controller = MyController(LargeMotor('outA'), LargeMotor('outB'), GyroSensor(), UltrasonicSensor())

    robot = r.Robot(controller)
    robot.start()

    name = raw_input("Exit: ")
    robot.kill()



