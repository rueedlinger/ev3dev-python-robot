#!/usr/bin/python
# -*- coding: utf-8 -*-


class Controller:

    _slow_speed = 30
    _normal_speed = 60
    _max_speed = 100
    _default_distance = 600

    def __init__(self, right_motor, left_motor, gyro_sensor):

        self.right_motor = right_motor
        self.left_motor = left_motor
        self.gyro_sensor = gyro_sensor
        self.motors = [right_motor, left_motor]
        self.speed = 50

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

    def backward(self):

        for m in self.motors:
            speed = m.duty_cycle_sp

            if speed > 0:
                m.duty_cycle_sp = speed * -1

        for m in self.motors:
            m.run_direct()

    def backward(self, distance):
        pos = self.right_motor.position + distance

        for m in self.motors:
            m.run_to_rel_pos(position_sp=distance)

        while self.right_motor.position >= pos:
            pass

    def forward(self):

        for m in self.motors:
            speed = m.duty_cycle_sp

            if speed < 0:
                m.duty_cycle_sp = speed * -1

        for m in self.motors:
            m.run_direct()

    def forward(self, distance):
        pos = self.right_motor.position + distance

        for m in self.motors:
            m.run_to_rel_pos(position_sp=distance)

        while self.right_motor.position >= pos:
            pass

    def turn(self, degree=90):
        self.left_motor.duty_cycle_sp *= -1
        angle = self.gyro_sensor.value() + degree

        while self.right_motor.position >= angle:
            pass

        self.left_motor.duty_cycle_sp *= -1

