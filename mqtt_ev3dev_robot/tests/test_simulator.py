# -*- coding: utf-8 -*-

import unittest
import turtle
from .context import mqtt_ev3dev as api


class BasicTestSuite(unittest.TestCase):

    def setUp(self):
        t = turtle.Turtle()
        t.reset()
        t.clear()
        t.speed(0)
        self.__turtle = t

    def compare_pos(self, pos1, pos2):
        self.assertAlmostEqual(pos1[0], pos2[0], delta=0.01)
        self.assertAlmostEqual(pos1[1], pos2[1], delta=0.01)

    def test_init_default(self):
        sim = api.Simulator()
        self.assertEqual(sim.angle(), 0)
        self.assertEqual(sim.position(), (0, 0))

    def test_init_with_valuesself(self):
        sim = api.Simulator(x=10, y=20, angle=90)
        self.assertEqual(sim.angle(), 90)
        self.assertEqual(sim.position(), (10, 20))

    def test_forward(self):
        sim = api.Simulator()
        distance = 100
        self.__turtle.forward(distance)
        sim.forward(distance)
        self.assertEqual(sim.position(), self.__turtle.position())

    def test_backward(self):
        sim = api.Simulator()
        distance = 180
        self.__turtle.backward(distance)
        sim.backward(distance)
        self.assertEqual(sim.position(), self.__turtle.position())

    def test_right(self):
        sim = api.Simulator()
        distance = 90
        angle = 45
        self.__turtle.right(angle)
        self.__turtle.forward(distance)

        sim.right(angle)
        sim.forward(distance)

        self.compare_pos(sim.position(), self.__turtle.position())

    def test_left(self):
        sim = api.Simulator()
        distance = 180
        angle = 70
        self.__turtle.left(angle)
        self.__turtle.forward(distance)

        sim.left(angle)
        sim.forward(distance)

        self.compare_pos(sim.position(), self.__turtle.position())

    def test_multiple_moves(self):
        sim = api.Simulator()
        distance = 180
        angle = 70
        self.__turtle.left(angle)
        self.__turtle.forward(distance)
        self.__turtle.backward(distance/2)
        self.__turtle.right(angle * 2)

        sim.left(angle)
        sim.forward(distance)
        sim.backward(distance/2)
        sim.right(angle * 2)

        self.compare_pos(sim.position(), self.__turtle.position())

        self.__turtle.backward(distance * 1.5)
        sim.backward(distance * 1.5)

        self.compare_pos(sim.position(), self.__turtle.position())

        self.__turtle.right(angle * 90)
        self.__turtle.forward(distance)

        sim.right(angle * 90)
        sim.forward(distance)

        self.compare_pos(sim.position(), self.__turtle.position())