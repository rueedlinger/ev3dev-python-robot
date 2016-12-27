# -*- coding: utf-8 -*-

import ev3dev.ev3 as ev3
import logging


class Robot:


    def __init__(self):

        logging.debug("Setting up...")

        # motors
        right_motor = ev3.LargeMotor('outA')
        logging.info("motor right connected: %s" % str(right_motor.connected))

        left_motor = ev3.LargeMotor('outB')
        logging.info("motor left connected: %s" % str(right_motor.connected))

        right_motor.reset()
        left_motor.reset()

        self.motors = [left_motor, right_motor]

        self.right_motor = right_motor
        self.left_motor = left_motor

        gyro_sensor = ev3.GyroSensor()
        logging.info("gyro sensor connected: %s" % str(gyro_sensor.connected))
        gyro_sensor.mode = 'GYRO-ANG'
        self.gyro_sensor = gyro_sensor

        try:
            color_sensor = ev3.ColorSensor()
            logging.info("color sensor connected: %s" % str(color_sensor.connected))
            color_sensor.mode = 'COL-REFLECT'
            self.color_sensor = color_sensor

        except Exception as e:
            logging.exception("message")

        try:
            ultrasonic_sensor = ev3.UltrasonicSensor()
            logging.info("ultrasonic sensor connected: %s" % str(ultrasonic_sensor.connected))
            ultrasonic_sensor.mode = 'US-DIST-CM'
            self.ultrasonic_sensor = ultrasonic_sensor

        except Exception as e:
            logging.exception("message")

        try:
            ir_sensor = ev3.InfraredSensor()
            logging.info("ir sensor connected: %s" % str(ir_sensor.connected))
            ir_sensor.mode = 'IR-REMOTE'
            self.ir_sensor = ir_sensor

        except Exception as e:
            logging.exception("message")

    def forward(self, speed=None):

        if speed:
            self.set_speed(abs(speed))
        else:
            self.set_speed(abs(self.right_motor.speed_sp))

        for m in self.motors:
            m.run_forever()

    def backward(self, speed=None):

        if speed:
            self.set_speed(-abs(speed))
        else:
            self.set_speed(-abs(self.right_motor.speed_sp))

        for m in self.motors:
            m.run_forever()

    def brake(self):
        for m in self.motors:
            m.stop()

    def turn(self, degree=90):

        logging.debug(self.right_motor.speed_sp)
        logging.debug(self.right_motor.speed)

        if self.right_motor.speed_sp >= 0:

            self.right_motor.speed_sp *= -1
            self.right_motor.run_forever()
            angle = self.gyro_sensor.value() + degree

            while self.gyro_sensor.value() <= angle:
                pass

            self.right_motor.speed_sp *= -1
            self.right_motor.run_forever()

        else:

            self.left_motor.speed_sp *= -1
            self.left_motor.run_forever()
            angle = self.gyro_sensor.value() + degree

            while self.gyro_sensor.value() <= angle:
                pass

            self.left_motor.speed_sp *= -1
            self.left_motor.run_forever()

    def set_speed(self, speed):
        for m in self.motors:
            m.speed_sp = speed

