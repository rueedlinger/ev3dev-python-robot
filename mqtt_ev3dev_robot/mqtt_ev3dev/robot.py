#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import ev3dev.ev3 as ev3


class Robot:
    """
    The ev3dev robot
    """

    DEFAULT_SPEED = 200
    TURN_SPEED = 100

    def __init__(self):
        """
        Initialize the ev3dev robot
        """

        right_motor = ev3.LargeMotor('outA')
        logging.info("motor right connected: %s" % str(right_motor.connected))

        left_motor = ev3.LargeMotor('outB')
        logging.info("motor left connected: %s" % str(right_motor.connected))

        right_motor.reset()
        left_motor.reset()

        gyro_sensor = ev3.GyroSensor()
        logging.info("gyro sensor connected: %s" % str(gyro_sensor.connected))
        gyro_sensor.mode = 'GYRO-ANG'

        gyro_sensor.mode = 'GYRO-G&A'

        self.gyro_sensor = gyro_sensor

        self.motors = [left_motor, right_motor]
        self.right_motor = right_motor
        self.left_motor = left_motor

    def forward(self, distance):
        """
        Move the robot forward by a given distance.
        :param distance: the distance the robot should move forward.
        :return: None
        """
        self.stop()
        for m in self.motors:
            m.run_to_rel_pos(position_sp=distance, speed_sp=self.DEFAULT_SPEED)

    def backward(self, distance):
        """
        Move the robot backward by a given distance.
        :param distance: the distance the robot should move backward.
        :return: None
        """
        self.stop()
        for m in self.motors:
            m.run_to_rel_pos(position_sp=-distance, speed_sp=self.DEFAULT_SPEED)

    def right(self, angle):
        """
        Turn the robot right by a given angle (degrees).
        :param angle: the angle in degrees.
        :return: None
        """
        self.right_motor.speed_sp = -self.TURN_SPEED
        self.left_motor.speed_sp = self.TURN_SPEED
        self.right_motor.run_forever()
        self.left_motor.run_forever()
        moveto = self.gyro_sensor.value() + angle

        while self.gyro_sensor.value() < moveto:
            # todo check interrupt
            pass

        self.stop()

    def left(self, angle):
        """
        Turn the robot left by a given angle (degrees).
        :param angle: the angle in degrees.
        :return: None
        """
        self.right_motor.speed_sp = self.TURN_SPEED
        self.left_motor.speed_sp = -self.TURN_SPEED
        self.right_motor.run_forever()
        self.left_motor.run_forever()
        moveto = self.gyro_sensor.value() - angle

        while self.gyro_sensor.value() > moveto:
            # todo check interrupt
            pass

        self.stop()

    def stop(self):
        """
        Stops the robot
        :return: None
        """
        for m in self.motors:
            m.stop()

    def state(self):
        """
        Returns the state of the robot (distance right / left motor and angle)
        :return: map {'right_motor', 'lef_motor', 'angle'} with the current values distance
        left motor, distance right motor and current angle in degrees of the robot
        """
        out = {
            'right_motor': self.right_motor.position,
            'lef_motor': self.left_motor.position,
            'angle': self.gyro_sensor.value()
        }

        return out

