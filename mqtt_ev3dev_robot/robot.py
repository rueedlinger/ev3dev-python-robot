#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import ev3dev.ev3 as ev3


class Robot:

    DEFAULT_SPEED = 400
    TURN_SPEED = 100

    def __init__(self):

        right_motor = ev3.LargeMotor('outA')
        logging.info("motor right connected: %s" % str(right_motor.connected))

        left_motor = ev3.LargeMotor('outB')
        logging.info("motor left connected: %s" % str(right_motor.connected))

        right_motor.reset()
        left_motor.reset()

        gyro_sensor = ev3.GyroSensor()
        logging.info("gyro sensor connected: %s" % str(gyro_sensor.connected))
        gyro_sensor.mode = 'GYRO-ANG'
        self.gyro_sensor = gyro_sensor

        self.motors = [left_motor, right_motor]
        self.right_motor = right_motor
        self.left_motor = left_motor

    def forward(self, distance):
        self.stop()
        for m in self.motors:
            m.run_to_rel_pos(position_sp=distance, speed_sp=self.DEFAULT_SPEED)

    def backward(self, distance):
        self.stop()
        for m in self.motors:
            m.run_to_rel_pos(position_sp=-distance, speed_sp=self.DEFAULT_SPEED)

    def right(self, angle):

        self.right_motor.speed_sp = -self.TURN_SPEED
        self.left_motor.speed_sp = self.TURN_SPEED
        self.right_motor.run_forever()
        self.left_motor.run_forever()
        moveto = self.gyro_sensor.value() + angle

        while self.gyro_sensor.value() < moveto:
            # todo check interrupt
            pass

        #print(moveto - self.gyro_sensor.value())

        self.stop()

    def left(self, angle):
        self.right_motor.speed_sp = self.TURN_SPEED
        self.left_motor.speed_sp = -self.TURN_SPEED
        self.right_motor.run_forever()
        self.left_motor.run_forever()
        moveto = self.gyro_sensor.value() - angle

        while self.gyro_sensor.value() > moveto:
            # todo check interrupt
            pass

        #print(moveto - self.gyro_sensor.value())

        self.stop()

    def stop(self):
        for m in self.motors:
            m.stop()