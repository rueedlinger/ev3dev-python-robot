#!/usr/bin/python
# -*- coding: utf-8 -*-

from ev3dev.auto import *
import time


class Explorer:

    def __init__(self):
        self.m_right = Motor(OUTPUT_A)
        self.m_left = Motor(OUTPUT_B)

        self.us = UltrasonicSensor()
        self.cs = ColorSensor()
        self.gs = GyroSensor()
        self.ts = TouchSensor()

        self.motors = [self.m_right, self.m_left]
        self.normal_speed = 35
        self.fast_speed = 60

        Sound.speak('5, 4, 3, 2, 1, lets go!')

    def turn(self):
        angle = self.gs.value()
        adjusted = angle + 90
        self.stop()
        self.forward()
        self.m_left.run_direct()

        while self.gs.value() <= adjusted:
            time.sleep(0.5)

        self.stop()
        self.forward()
        self.start()

    def start(self):
        for m in self.motors:
            m.run_direct()

    def set_speed(self, speed):
        for m in self.motors:
            m.duty_cycle_sp = speed

    def stop(self):
        for m in self.motors:
            m.stop()

    def forward(self):
        self.set_speed(self.normal_speed)

    def backward(self):
        self.set_speed(-self.normal_speed)
        self.start()
        time.sleep(1)

    def adjust(self, angle, speed):
        if angle > self.gs.value():
            self.m_right.duty_cycle_sp = speed - 5
            time.sleep(1)
            self.m_right.duty_cycle_sp = speed
        else:
            self.m_left.duty_cycle_sp = speed - 5
            time.sleep(1)
            self.m_left.duty_cycle_sp = speed

        self.set_speed(self.normal_speed)
        self.start()

    def loop(self):

        distance = self.us.value()
        color_reflect = self.cs.value()

        if distance > 250:
            self.set_speed(self.fast_speed)
        else:
            self.set_speed(self.normal_speed)


        #adjust(angle, normal_speed)

        if self.ts.value() == 1:
            self.stop()
            self.backward()
            self.turn()


        if color_reflect <= 7:
            self.stop()
            self.backward()
            self.turn()

        if distance <= 100:
            # break
            self.stop()
            self.backward()
            self.turn()


