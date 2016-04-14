#!/usr/bin/python
# -*- coding: utf-8 -*-

from ev3dev.auto import *

import ev3robot.logic as logic
import ev3robot.robot as r

import time

if __name__ == "__main__":

    class TestController(logic.Controller):

        def setup(self):
            print('setup')

        def teardown(self):
            print('teardown')

        def loop(self):

            self.forward()
            time.sleep(3)
            self.turn(90)
            time.sleep(3)
            self.backward()
            time.sleep(3)
            self.brake()
            time.sleep(3)


    controller = TestController(right_motor=LargeMotor('outA'), left_motor=LargeMotor('outB'),
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