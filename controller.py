#!/usr/bin/python
# -*- coding: utf-8 -*-

import ev3robot.robot as r
#import ev3robot.logic as logic
import ev3robot.mock as logic

if __name__ == "__main__":

    explorer = logic.Explorer()

    robot = r.Robot(explorer)
    robot.run()



