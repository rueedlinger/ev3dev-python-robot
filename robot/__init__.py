# -*- coding: utf-8 -*-

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor, ColorSensor, InfraredSensor, UltrasonicSensor
import logging

class Robot:

    def __init__(self):

        logging.debug("Setting up...")

        # motors
        right_motor = LargeMotor(OUTPUT_A)
        logging.info("motor right connected: %s" % str(right_motor))
        logging.info("motor right max speed: %s" % str(right_motor.max_speed))

        left_motor = LargeMotor(OUTPUT_B)
        logging.info("motor left connected: %s" % str(right_motor))
        logging.info("motor left max speed: %s" % str(left_motor.max_speed))

        right_motor.reset()
        left_motor.reset()

        self.motors = [left_motor, right_motor]

        self.right_motor = right_motor
        self.left_motor = left_motor

        try:

            gyro_sensor = GyroSensor()
            logging.info("gyro sensor connected: %s" % str(gyro_sensor.num_values))
            
            gyro_sensor.mode = GyroSensor.MODE_GYRO_ANG
            self.gyro_sensor = gyro_sensor

        except Exception:
            logging.exception("message")

        try:
            color_sensor = ColorSensor()
            logging.info("color sensor connected: %s" % str(color_sensor))
            color_sensor.mode = 'COL-REFLECT'
            self.color_sensor = color_sensor

        except Exception:
            logging.exception("message")

        try:
            ultrasonic_sensor = UltrasonicSensor()
            logging.info("ultrasonic sensor connected: %s" % str(ultrasonic_sensor))
            ultrasonic_sensor.mode = 'US-DIST-CM'
            self.ultrasonic_sensor = ultrasonic_sensor

        except Exception:
            logging.exception("message")

        try:
            ir_sensor = InfraredSensor()
            logging.info("ir sensor connected: %s" % str(ir_sensor))
            ir_sensor.mode = 'IR-REMOTE'
            self.ir_sensor = ir_sensor

        except Exception:
            logging.exception("message")

    def forward(self, speed=None):

        if speed:
            self.set_speed(abs(speed))

        for m in self.motors:
            m.run_forever()

    def backward(self, speed=None):
        
        if speed:
            self.set_speed(abs(speed) * -1)

        for m in self.motors:
            m.run_forever()

    def brake(self):
        for m in self.motors:
            m.stop()

    def turn(self, degree=90):

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

        logging.debug('speed sp (right_motor): %s' % str(self.right_motor.speed_sp))
        logging.debug('speed sp (left_motor): %s' % str(self.left_motor.speed_sp))

        logging.debug('speed (right_motor): %s' % str(self.right_motor.speed))
        logging.debug('speed (left_motor): %s' % str(self.left_motor.speed))

        logging.debug('max speed (right_motor): %s' % str(self.right_motor.max_speed))
        logging.debug('max speed (left_motor): %s' % str(self.left_motor.max_speed))

    
    

