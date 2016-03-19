#!/usr/bin/python
# -*- coding: utf-8 -*-

class Motor:

    def __init__(self):
        self.duty_cycle_sp = 0
        self._running = False
        self.position = 0

    def run_direct(self):
        self._running = True
        print('run')
        pass

    def run_to_rel_pos(self, position_sp):
        self.position += position_sp

    def stop(self):
        self.duty_cycle_sp = 0
        self._running = False

