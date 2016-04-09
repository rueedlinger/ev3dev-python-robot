#!/usr/bin/python
# -*- coding: utf-8 -*-
import time



class Controller:

    _slow_speed = 30
    _normal_speed = 60
    _max_speed = 100

    def __init__(self, right_motor, left_motor, gyro_sensor, ultrasonic_sensor):

        self.right_motor = right_motor
        self.left_motor = left_motor
        self.gyro_sensor = gyro_sensor
        self.ultrasonic_sensor = ultrasonic_sensor
        self.motors = [right_motor, left_motor]

        self._set_sensor_modes()

    def _set_sensor_modes(self):

        self.ultrasonic_sensor.mode = 'US-DIST-CM'
        self.gyro_sensor.mode = 'GYRO-ANG'

    def max_speed(self):
        self.set_speed(self._max_speed)

    def slow_speed(self):
        self.set_speed(self._slow_speed)

    def normal_speed(self):
        self.set_speed(self._normal_speed)

    def set_speed(self, speed):
        for m in self.motors:
            m.duty_cycle_sp = speed

    def brake(self):

        for m in self.motors:
            m.stop()

    def angle(self):
        return self.gyro_sensor.value()

    def distance(self):
        return self.ultrasonic_sensor.value()

    def has_obstacle(self, range=100):

        if self.distance() <= range:
            return True
        else:
            return False

    def backward(self):

        if self.right_motor.duty_cycle == 0:
            self.normal_speed()

        for m in self.motors:
            speed = m.duty_cycle_sp

            if speed > 0:
                m.duty_cycle_sp = speed * -1

        for m in self.motors:
            m.run_direct()

    def drive_distance(self, distance):

        for m in self.motors:
            m.run_to_rel_pos(position_sp=distance)


    def forward(self):

        if self.right_motor.duty_cycle == 0:
            self.normal_speed()

        for m in self.motors:
            speed = m.duty_cycle_sp

            if speed < 0:
                m.duty_cycle_sp = speed * -1

        for m in self.motors:
            m.run_direct()


    def turn(self, degree=90):

        if self.right_motor.duty_cycle == 0:
            self.forward()

        # forward
        if self.right_motor.duty_cycle_sp >= 0:

            self.right_motor.duty_cycle_sp *= -1

            angle = self.gyro_sensor.value() + degree

            while self.gyro_sensor.value() <= angle:
                pass

            self.right_motor.duty_cycle_sp *= -1

        else:
            self.left_motor.duty_cycle_sp *= -1

            angle = self.gyro_sensor.value() + degree

            while self.gyro_sensor.value() <= angle:
                pass

            self.left_motor.duty_cycle_sp *= -1

