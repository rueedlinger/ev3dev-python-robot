#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import logging
from random import randint

from robot import Robot

# default sleep timeout in sec
DEFAULT_SLEEP_TIMEOUT_IN_SEC = 0.1

# default speed
DEFAULT_SPEED = 100

# default threshold distance
DEFAULT_THRESHOLD_DISTANCE = 90

# config logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def main():

    logging.debug('Run robot, run!')
    robot = Robot()

    robot.set_speed(DEFAULT_SPEED)
    robot.forward()

    try:

        while True:
            time.sleep(DEFAULT_SLEEP_TIMEOUT_IN_SEC)

            logging.debug('color value: %s' % str(robot.color_sensor.value()))
            logging.debug('ultrasonic value: %s' % str(robot.ultrasonic_sensor.value()))
            logging.debug('gyro value: %s' % str(robot.gyro_sensor.value()))
            logging.debug('motor positions (r, l): %s, %s' % (str(robot.right_motor.position),
                                                              str(robot.left_motor.position)))
            logging.debug('motor speed (r, l): %s, %s' % (str(robot.right_motor.speed),
                                                              str(robot.left_motor.speed)))

            if robot.ultrasonic_sensor.value() < DEFAULT_THRESHOLD_DISTANCE:
                logging.debug('object found: %s' % str(robot.ultrasonic_sensor.value()))

                robot.forward(DEFAULT_SPEED * 0.5)
                robot.turn(randint(90, 180))
                robot.forward(DEFAULT_SPEED)

    # doing a cleanup action just before program ends
    # handle ctr+c and system exit
    except (KeyboardInterrupt, SystemExit) as e:
        logging.exception("message")

    # handle exceptions
    except Exception as e:
        logging.exception("message")

    finally:
        teardown(robot)
        logging.shutdown()


def teardown(robot):
    robot.brake()

if __name__ == "__main__":
    main()
