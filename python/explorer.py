#!/usr/bin/python
# -*- coding: utf-8 -*-

from ev3dev.auto import *

import python.ev3robot.logic as logic
from python import ev3robot as r

if __name__ == "__main__":

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

    try:
        # wait
        name = raw_input("Press Enter to exit: ")
    except (KeyboardInterrupt, SystemExit):
        robot.kill()






