#!/usr/bin/python
# -*- coding: utf-8 -*-

class Motor:

    def __init__(self):
        self.duty_cycle_sp = 0
        self._running = False
        self.position = 0

    def run_direct(self):
        self._running = True
        pass

    def run_to_rel_pos(self, position_sp):
        self.position += position_sp

    def stop(self):
        self.duty_cycle_sp = 0
        self._running = False


class UltrasonicSensor:

    def __init__(self):
        pass

    def value(self):
        return 100

class GyroSensor:

    def __init__(self):
        pass

    def value(self):
        return 10